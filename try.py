# load the library
from bs4 import BeautifulSoup as Soup
import urllib, requests, re, pandas as pd

# indeed.com url
base_url = 'http://www.indeed.com/jobs?q=data+scientist&jt=fulltime&sort='
sort_by = 'date'          # sort by data
start_from = '&start='    # start page number

pd.set_option('max_colwidth',500)    # to remove column limit (Otherwise, we'll lose some info)
df = pd.DataFrame()   # create a new data frame


for page in range(1,101): # page from 1 to 100 (last page we can scrape is 100)
    page = (page-1) * 10
    url = "%s%s%s%d" % (base_url, sort_by, start_from, page) # get full url
    target = Soup(urllib.urlopen(url), "lxml")

    targetElements = target.findAll('div', attrs={'class' : '  row  result'}) # we're interested in each row (= each job)

    # trying to get each specific job information (such as company name, job title, urls, ...)
    for elem in targetElements:
        comp_name = elem.find('span', attrs={'itemprop':'name'}).getText().strip()
        job_title = elem.find('a', attrs={'class':'turnstileLink'}).attrs['title']
        home_url = "http://www.indeed.com"
        job_link = "%s%s" % (home_url,elem.find('a').get('href'))
        job_addr = elem.find('span', attrs={'itemprop':'addressLocality'}).getText()
        job_posted = elem.find('span', attrs={'class': 'date'}).getText()

        comp_link_overall = elem.find('span', attrs={'itemprop':'name'}).find('a')
        if comp_link_overall != None: # if company link exists, access it. Otherwise, skip.
            comp_link_overall = "%s%s" % (home_url, comp_link_overall.attrs['href'])
        else: comp_link_overall = None

				# add a job info to our data frame
        df = df.append({'comp_name': comp_name, 'job_title': job_title,
                        'job_link': job_link, 'job_posted': job_posted,
                        'overall_link': comp_link_overall, 'job_location': job_addr,
                        'overall_rating': None, 'wl_bal_rating': None,
                        'benefit_rating': None, 'jsecurity_rating': None,
                        'mgmt_rating': None, 'culture_rating': None
                       }, ignore_index=True)

df

print df
