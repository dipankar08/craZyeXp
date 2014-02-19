import requests
from bs4 import BeautifulSoup
import string
import re
import urlparse
import pickle
from sms import getSmsHandaler
import pdb

DEBUG = True

# Help Function for Save and Restore WebSite Data ########
def getSiteKey(url):
  " return Site key as a domain name"
  netloc =  urlparse.urlparse(url).netloc
  netloc = netloc.replace("www.", "")
  return netloc

def save_site_data(url,data):
  file_name =  getSiteKey(url)+'.pkl'
  pickle.dump( data, open( file_name, "wb" ))

def load_site_data(url):
  file_name =  getSiteKey(url)+'.pkl'
  try:
    return pickle.load( open( file_name, "rb" ) )
  except:
    print 'No store data found for '+file_name
    return None

# Helper Function for makeing clean HTML data
def clean_text(s):
  """ Helper function remove all \n \t \r etc"""
  s = re.sub( '[\n\t\r\s]+', ' ', s ).strip()
  s.decode('unicode_escape').encode('ascii','ignore')
  return s


# HElper function for multiple way of site grabbing

def getHTMLMenuContent(first_url,max_menu=100):
  """
  This code return the list of menu or cetegories url.
  For example for a sms site it will return a base link of each categories.
  """
  cat_url_list = []
  if DEBUG: print '>>> Reading '+first_url+'...'
  resp = requests.get(first_url)
  html = resp.text
  soup = BeautifulSoup(html)
  
  # Get list of Contents
  if getSiteKey(first_url) == 'g10sms.com':
    for a in soup.find('ul',{'class':'menu'}).find_all('a'):
      cat_url_list.append((clean_text(a.text).strip(),a['href']))

  if getSiteKey(first_url) == '140wordsms.com':
    for a in soup.find('ul',{'id':'cat-nav'}).find_all('a'):
      cat_url_list.append((clean_text(a.text).strip(),a['href']))

  if getSiteKey(first_url) == 'latestsms.in':
    for a in soup.find('div',{'id':'vertmenu'}).ul.find_all('a'):
      cat_url_list.append((clean_text(a.text).strip(),'http://www.latestsms.in/'+a['href']))
  return cat_url_list


def getHTMLPaginationContent(first_url,max_count=999999):
  """
  The Logrithm is so smple like this.
  1. Take the first url as input
  2. we make a msg_list aas global.
  while( tehere is no next url)
  {
    1.Grap the site and pupulate global list
    2.Parse pagination and find next url if exist
  }
  """
  SITE_KEY = getSiteKey(first_url)
  msg_list=[]
  cur_count =0;
  while(first_url):
    if DEBUG: print '>>> Reading '+first_url+'...'
    resp = requests.get(first_url)
    html = resp.text
    soup = BeautifulSoup(html)
    ######## Step1: Dig the Content and Populate the list ###
    if SITE_KEY == 'g10sms.com':
      content = soup.find('div',{'class':'blog'}).find_all('div',{'class':'article_column'})
      for c in content:
        msg_list.append(c.find_all('p')[1].text)
        cur_count +=1
        if cur_count == max_count:
          return msg_list
    if SITE_KEY == '140wordsms.com':
      content = soup.find('div',{'id':'content'}).find_all('div',{'class':'entry-box'})
      for c in content:
        #pdb.set_trace()
        sub_url = c.a['href'] # We have a concept of sub url here
        sub_soup = BeautifulSoup(requests.get(sub_url).text) 
        try:
          msg_list.append(sub_soup.find('div',{'class':'entry'}).find('h5').text)
        except:
          try:
            msg_list.append(sub_soup.find('div',{'class':'entry'}).p.text)
          except:
            pass
        cur_count +=1
        if cur_count == max_count:
          return msg_list
    if SITE_KEY == 'latestsms.in':
      try:
        content = soup.find('div',{'id':'maincontent'}).find_all('p',{'class':'maincontent'})
      except:
        try:
          content = soup.find('div',{'id':'asciicontent'}).find_all('p',{'class':'asciicontent'})
        except:
          return []        
      for c in content:
        msg_list.append(c.text)
        cur_count +=1
        if cur_count == max_count:
          return msg_list
        
    
    ######## Step 2: Find The next Page in the pagination ####
    next_page = None
    
    if SITE_KEY == 'g10sms.com':
      page = soup.find('ul',{'class':'pagination'})      
      for a in page.find_all('a'):
        if a.text =='Next':
          next_page = a['href']
          
    if SITE_KEY == '140wordsms.com':
      for a in soup.find('div',{'class':'pagination'}).find_all('a'):
        if a.text =='Older Entries':
          next_page = a['href']
          break;
    if SITE_KEY == 'latestsms.in':
      try:
        for a in soup.find('div',{'class':'pagination'}).find_all('a'):
          if 'next' in a.text:
            next_page = 'http://www.latestsms.in/'+ a['href']
            break;
      except:
        next_page = None
    first_url = next_page
  return msg_list

def grabFullSite(base_url,use_cache=True):
  #Check for cache..
  if use_cache:
    if DEBUG: print '>>> Checking for cache...'
    data = load_site_data(base_url)
    if data:
      if DEBUG: print '>>> data Found in cache, Skip grabbing...'
      if DEBUG: print '>>> Total Content Count::'+str(sum([len(i) for i in data.values()]))
      return data
  if DEBUG: print '\n>>> Cache Not found hence grading'
  
  if DEBUG: print '\n>>> getting categorie list'
  cat_list = getHTMLMenuContent(base_url)
  
  data ={}
  for name,url in cat_list:
    if DEBUG: print '\n>>> Start processing categories:'+name
    data[name] = getHTMLPaginationContent(url)
    if DEBUG: print '>>> End processing categories:'+name
    if DEBUG: print '>>> Total Numbe of message is found:'+str(len(data[name]))
    

  if DEBUG: print '>>> Storing in cache Fefore Return'  
  save_site_data(base_url,data)
  if DEBUG: print '>>> Site Grab completed\n>>> Total Content Count::'+str(sum([len(i) for i in data.values()]))
  return data
  

def smsSendSchedular(to_list,sms_list,interval_in_sec=3600,randamize=True,default_service = "160by2"):
  " A mini Schedulr for sending sms"
  print ">>> You have Schedule %d number of sms  to the number %s in the interval of %d second " %(len(sms_list),to_list,interval_in_sec) 
  raw_input(">>> Please press ENTER type to Confirm.")
  import time
  import random
  from ConfigParser import ConfigParser
  import way2sms
  import one6tiby2
  
  if randamize: random.shuffle(sms_list)

  config = ConfigParser()
  config.read("../config.ini")
  username = config.get(default_service, "uname")
  password = config.get(default_service, "password")
  
  for sms in sms_list:
    if len(sms) > 150: # This is a restriton..
      continue
    try:
      handler = getSmsHandaler(username,password,default_service)
      for to in to_list:
        handler.do(to,sms)
    except Exception,e:
      print 'OOPS.. Msg not send some error',str(e)
    time.sleep(interval_in_sec)
  
  
  
### Sample Test ###
def activate(no_list=['8880428779'],interval_in_sec =3600,site = 'http://g10sms.com/sms140/'):
  data = grabFullSite(site)
  print '>>> Hello, we support following SMS type:'
  for key in data.keys():
    print '%s(%d / %d) ' %(key, len(data[key]), len(filter(lambda x:len(x)<=140, data[key]))) ,
  x = raw_input("\n>>> Please press type which SMS you want to subscribe:")
  smsSendSchedular(to_list=no_list,interval_in_sec=interval_in_sec,default_service="way2sms",sms_list = data[x])

############ Run here #############
WEBSITE_SUPPORT=[
  'http://g10sms.com/sms140/','http://www.latestsms.in/sad-sms.htm','http://www.140wordsms.com'
  ]
no = raw_input("Enter the number: ");
interval =raw_input("Enter the interval: ");
print 'We support:',WEBSITE_SUPPORT
site = raw_input('Enter which site you Support:')
activate([no],int(interval),str(site))
#SITE_URL = 'http://www.140wordsms.com' # Dont put www.
#data = grabFullSite(SITE_URL)
##print data
