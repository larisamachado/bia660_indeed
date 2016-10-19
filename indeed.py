
# coding: utf-8

# In[12]:

from bs4 import BeautifulSoup
import re
import urllib2
from operator import itemgetter
import time
import sys
import requests
import os


# In[13]:

def run(url):
    #goal: take the URL to be searched on indeed and return the BS4 format
    #url = http://www.indeed.com/jobs?q=data+scientist&l=NYC,+NY&rbl=New+York,+NY&jlid=45f6c4ded55c00bf&jt=fulltime&explvl=entry_level

    pageNum=1 #try 1 page for now
    for p in range(1,pageNum+1): # for each page
        html=None
        if p==1:
            pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print 'failed attempt',i
                time.sleep(2) # wait 2 secs
            if not html:
                continue # couldnt get the page, ignore
            soup = BeautifulSoup(html, "lxml") # parse the html
    return soup


# In[14]:

def jobAd(soup):
    #goal: take the SOUP format from function run and make a dict for each Job,
    #where the key is the url & the value is the Job Title
    jobNameURLs = {}


    return jobNameURLs


# In[15]:

def jobDescription(jobNameURL):
    #goal: take just 1 URL from the dict from function JobAd,
    #and download the webpage with the job description from the hyperlink

    return webpage


# In[16]:

def makeFolder(jobNameURL, webpage):
    #goal: Make a folder with a title of JobName from the Dict, and paste the webpage in there


    return "success"


# In[17]:

if __name__ == "__main__":
    url = 'http://www.indeed.com/jobs?q=data+scientist&l=NYC,+NY&rbl=New+York,+NY&jlid=45f6c4ded55c00bf&jt=fulltime&explvl=entry_level'

    soup = run(url)
    jobNameURLS = jobAd(soup) #DICT of all the job URLS and job Names

    os.makedirs("\DSNYCFTEL")
    os.chdir("\DSNYCFTEL") #change the directory so any new folders are made into DSNYCFTEL

    for jobNameURL in jobNameURLS: #for each URL in the dict
        webpage = jobDescription(jobNameURL) #obtain the webpage
        makeFolder(webpage) #make a folder and paste the webpage there



# In[ ]:
