# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:26:18 2019

@author: Student
"""

#prepare resources, bring in Beautiful Soup to handle parsing
import requests, re
from bs4 import BeautifulSoup

l=[]
#loading page in 'r'
r=requests.get("https://www.gannett.com/news/")
#storing page source in 'c'
c=r.content

#parsing 'c' into soup using BS4 html parser
soup=BeautifulSoup(c,"html.parser")

#storing scraping target in 'all', each press release ITC
all=soup.find_all("div",{"class":"col-xs-24"}) 

#scrape dates, titles, preview of press release into 'l'
for item in all: # but first iterate through 'd' to build 'l'
    d={}    
    try:
        d["Date"]=item.find_all("p",{"class","gmm-pre-title"})[0].text
    except:
        d["Date"]=None        
    try:
        d["Title"]=item.find_all("h2",{"class","gmm-title"})[0].text
    except:
        d["Title"]=None    
    try:
        d["Preview"]=item.find_all("div",{"class","gmm-text-content"})[0].text
    except:
        d["Preview"]=None
    l.append(d)

import pandas
df=pandas.DataFrame(l)
df.to_csv("OutputWebscrape.csv")
    