# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 08:56:57 2017

@author: nikhil
"""

import requests,csv
from bs4 import BeautifulSoup

slist = ['mitsubishi-ufj-financial','sberbank','state-bank-of-india','krung-thai-bank','maybank','bank-central-asia','qatar-national-bank','societe-generale','barclays','deutsche-bank','citigroup','bank-of-china','hsbc-holdings','wells-fargo','jpmorgan-chase','bnp-paribas','bank-of-america','standard-bank-group','dbs-group']
wlist = ['Mitsubishi_UFJ_Financial_Group','Sberbank_of_Russia','State_Bank_of_India','Krung_Thai_Bank','Maybank','Bank_Central_Asia','QNB_Group','Société_Générale','Barclays','Deutsche_Bank','Citigroup','Bank_of_China','HSBC','Wells_Fargo','JPMorgan_Chase','BNP_Paribas','Bank_of_America','Standard_Bank','DBS_Bank']
global flist
flist = dict(zip(slist,wlist))

class WSscrape(object):
        
    url = "https://www.forbes.com/companies/"
    wurl = "https://en.wikipedia.org/wiki/"
    sdata = None
    wdata = None
    def __init__(self,bank_name):
        self.name = bank_name
        r = requests.get(self.url + self.name)
        ssoup = BeautifulSoup(r.content,'lxml')
        self.sdata = ssoup.find_all("div", {"class": "main-info"})[0]
        
        w = requests.get(self.wurl + flist[self.name])
        wsoup = BeautifulSoup(w.content,'lxml')
        self.wdata = wsoup.find_all("table", {"class": "infobox vcard"})
        
    @property
    def industry(self):
        try:
            return self.sdata.find(text = 'Industry').parent.nextSibling.nextSibling.text
        except:
            return None    
    
    @property
    def mcap(self):
        try:
            return self.sdata.find('li',{"class":"market-cap"}).nextSibling.nextSibling.text
        except:
            return None
    @property
    def founded(self):
        try:
            return self.sdata.find(text = 'Founded').parent.nextSibling.nextSibling.text
        except:
            return None
    @property
    def country(self):
        try:
            return self.sdata.find(text = 'Country').parent.nextSibling.nextSibling.text
        except:
            return None
    
    @property
    def employees(self):
        try:
            return self.sdata.find(text = 'Employees').parent.nextSibling.nextSibling.text
        except:
            return None
    @property
    def sales(self):
        try:
            return self.sdata.find(text = 'Sales').parent.nextSibling.nextSibling.text
        except:
            return None
        
    @property
    def comp_type(self):
        try:
            return [t.parent.parent.parent.next_sibling.next_sibling.text for t in self.wdata[0].findAll(text='Type')][0]
        except:
            return None
        
    @property
    def ISIN(self):
        try:
            return [t.parent.parent.nextSibling.next_sibling.text for t in self.wdata[0].findAll(text='ISIN')][0]
        except:
            return str(0)*8
        
    @property
    def web_site(self):
        try:
            return self.wdata[0].find(text="Website").parent.nextSibling.nextSibling.a['href']
        except:
            return None

def start_here():
    
    header = ['Name','Type','Industry','MarketCap','Sales','Founded','ISIN','Employees','Country','WebSite']
    tofile = open('companies_data.csv','w',newline='')
    writer = csv.writer(tofile)
    writer.writerow(header)
    for comp in slist:
        try:
            a = WSscrape(comp)
            a.mcap1 = a.mcap.split(' ')[0]
            a.sales1 = a.sales.split(' ')[0]
            writer.writerow([a.name,a.comp_type,a.industry,a.mcap1,a.sales1,a.founded,a.ISIN,a.employees,a.country,a.web_site])
            #print ([a.name,a.comp_type,a.industry,a.mcap1,a.sales1,a.founded,a.ISIN,a.employees,a.country,a.web_site])
            #break
        except:
            print (a.name)
            continue
    tofile.close()

if __name__ == "__main__":
    start_here()
    

    
