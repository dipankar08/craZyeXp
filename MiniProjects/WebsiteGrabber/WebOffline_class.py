#########
# Full Website Crawler 
# Author : Dipankar
# Code : python Ad.
##########

import random
import string
import requests
from bs4 import BeautifulSoup
import pdb
import urlparse
import os
from Queue import Queue
import threading
import re
from os.path import expanduser
from urlparse import urljoin
import pickle

# Helper Function for makeing clean HTML data
def clean_text(s):
  """ Helper function remove all \n \t \r etc"""
  s = re.sub( '[\n\t\r\s]+', ' ', s ).strip()
  s.decode('unicode_escape').encode('ascii','ignore')
  return s

def getSiteKey(url):
  " return Site key as a domain name"
  netloc =  urlparse.urlparse(url).netloc
  netloc = netloc.replace("www.", "")
  return netloc

def getProperUrl(base,target):
    cur= None
    if target.startswith('http'):
        cur = target
    else:
        cur = urljoin(base, target)

    # Removing www
    #pdb.set_trace()
    if cur.startswith('http://www.'):
        cur = cur.replace('http://www.','http://')
    if cur.startswith('https://www.'):
        cur = cur.replace('https://www.','https://')
    return cur
def genarate_random_Name(ext='html'):
    """
    Generate 32 bype ramdom ID with extension
    """
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    return rand +'.'+ext

class myThread (threading.Thread):
    def __init__(self,id,data,wf):
        threading.Thread.__init__(self)
        self.id = id
        self.data = data
        self.wf = wf
    def run(self):
        print '>>> [%s] Processing %s' %(self.id, self.data[1]) 
        self.wf.download_change_save(self.data)

class WebOffline:
  def __init__(self):
    self.HOME = expanduser("~")
    self.URL_HASH ={}
    self.PENDING_URL_QUEUE = Queue()
    self.COMPLETE_URL_MAP ={}
    self.REJECT_URL_LIST =[]
    self.FILE_TYPE = ['html','css','js','img','other']
  def config(self,BASE_URL = 'http://geeksforgeeks.org',INCLUDE_ONLY_URL_EXP =[],EXCLUDE_URL_EXP =[], DEPTH =99,INDOMAIN=True,ALLOWED_DOMAIN=[],DEBUG=False,MAX_THREAD=10):
    self.BASE_URL=getProperUrl(BASE_URL,'')
    if self.BASE_URL.endswith('/'): self.BASE_URL = self.BASE_URL[:-1]
    self.INCLUDE_ONLY_URL_EXP = INCLUDE_ONLY_URL_EXP
    self.EXCLUDE_URL_EXP = EXCLUDE_URL_EXP
    self.DEPTH = DEPTH
    self.INDOMAIN = INDOMAIN
    self.ALLOWED_DOMAIN = ALLOWED_DOMAIN
    self.DEBUG = DEBUG
    self.MAX_THREAD = MAX_THREAD
    self.PATH_ROOT = os.path.join(self.HOME,'download',getSiteKey(self.BASE_URL))
    """
    TPL Format : < type, link, extension, title, ref-link, depth >
    """
    self.start_tpl = ('html',BASE_URL,'html','HomePage',BASE_URL,0)
    
    # Step 1: Initialization of Stuffs.
    for i in self.FILE_TYPE:
      path = os.path.join(self.PATH_ROOT,i)
      if not os.path.exists(path): os.makedirs(path)
      
    ### Customize CSS file ###
    for i in range(1,6):
      open(os.path.join(self.PATH_ROOT,'css',"mycustom"+str(i)+".css"), 'a').close()
  def show_summary(self):
    print '******************************************'
    print 'BASE_URL: ',self.BASE_URL
    print 'COMPLETE_URL_MAP: ',len(self.COMPLETE_URL_MAP.keys())
    print 'REJECT_URL_LIST: ',len(self.REJECT_URL_LIST)
    
    print '******************************************'
    """
    print 'COMPLETE_URL_MAP: '
    for i in self.COMPLETE_URL_MAP:
      print i
    print 'REJECT_URL_LIST: '
    for i in self.REJECT_URL_LIST:
      print i
    
    print '******************************************'
    """
  def checkCrawnCondition(self,tpl=None):
    """
    tested : max-depth, not in domain, include and xcluode url.
    """
    # 1. General URL Check.
    if "#" in tpl[1]: # We remove all # realated link as duplicates.
      if self.DEBUG: print '>>> removing %s due to duplicates.' %tpl[1]
      self.REJECT_URL_LIST.append((tpl[1],'INVALID URL'))
      return False 
        
    # 2. Customize url Check.
    if tpl[0] == 'html' and tpl[5] > self.DEPTH :
      self.REJECT_URL_LIST.append((tpl[1],'MAX-DEPTH REACHED'))
      return False
    if tpl[0] == 'html':
      if self.INDOMAIN is True and not tpl[1].startswith(self.BASE_URL):
        self.REJECT_URL_LIST.append((tpl[1],'NOT IN DOMAIN'))
        return False
      if self.INDOMAIN is False:
        self.REJECT_URL_LIST.append((tpl[1],'NOT IN ALLOWED DOMAIN'))
        return False
      if len(self.INCLUDE_ONLY_URL_EXP) > 0:
        flag = False
        for i in  self.INCLUDE_ONLY_URL_EXP:
          if i in tpl[1]: flag =True;break;
        if not flag:
          self.REJECT_URL_LIST.append((tpl[1],'URL NOT IN INCLUDE_ONLY_URL_EXP'))
          return False
      if len(self.EXCLUDE_URL_EXP) > 0:
        for i in  self.EXCLUDE_URL_EXP:
          if i in tpl[1]: 
            self.REJECT_URL_LIST.append((tpl[1],'URL IN EXCLUDE_URL_EXP'))
            return False          
          
    return True
  
  def linkStoreHash(self,tpl):
      "Store type url --> (abc.css,(css, http:///// , helloworld ...))"
      if tpl[1] in self.URL_HASH:
          if self.DEBUG: print '>>> URL alredy exit Skip..'
          return self.URL_HASH[tpl[1]]
      name = genarate_random_Name(tpl[2])
      self.URL_HASH[tpl[1]] =(name,tpl)
      self.PENDING_URL_QUEUE.put(self.URL_HASH[tpl[1]])
      return self.URL_HASH[tpl[1]]
  def getHashName(self,url):
      """
      url -> file name mapping
      """
      if url in self.URL_HASH:
          return self.URL_HASH[url][0]
      else:
          return None
  def download_change_save(self,tpl):
    """
    Main Handaler for each Selected URL, Download URL--> Find Link--> Replace Link--> Save.
    """
    try:
      url = tpl[1]
      r = requests.get(url)
      data = r.content
      typex = r.headers.get('content-type')
      if tpl[0] == 'html':
          data = self.xplore_link(data,url,tpl[5])
      self.save_data(data,tpl)
      
      print '>>> Save Complete'
    except Exception ,e :
      print '>>> ERROR While Downloading',e
  def reconstractHyperLink(self,tplh):
      """
      Reconstruct HyperLink with relative link for off line access
      """
      ret = "../"+tplh[1][0] +"/" +tplh[0]
      return ret
  def raw_search(self,data,baseurl):
    """
    This search for url in JS or CSS file.
    """
    list = re.findall(r'["\'](http://.*?)["\']',data)
    for l in list:
      if '.css' in l:
       tpl = ('css',getProperUrl(baseurl,l))
       tplh = self.linkStoreHash(tpl)
      if '.js' in l:
       tpl = ('css',getProperUrl(baseurl,l))
       tplh = self.linkStoreHash(tpl)
    if self.DEBUG : print '>>> %s number of hidden url found' %len(list)
  def xplore_link(self, html,baseurl,depth):
      """
      Scan the HTML and find all the LInk
      Generate the relative name and replace the href and src.
      Adding some HTML code or customize css/js
      """
      soup = BeautifulSoup(html)
      
      links = soup.find_all("link")
      for link in links:
        try:
          if  'stylesheet' in link['rel'] :
            tpl = ('css',getProperUrl(baseurl,link['href']),'css','No-title',baseurl,depth+1)
            if self.checkCrawnCondition(tpl):
                tplh = self.linkStoreHash(tpl)
                link['href'] = self.reconstractHyperLink(tplh)              
           
          else:
            a = link['href']
            tpl = ('other',getProperUrl(baseurl,link['href']),a[a.rindex('.')+1:],'No-Tile',baseurl,depth+1)
            if self.checkCrawnCondition(tpl):
                tplh = self.linkStoreHash(tpl)
                link['href'] = self.reconstractHyperLink(tplh)              
        except Exception ,e :
          print 'ERROR',e

      links = soup.find_all("script")
      for link in links:
        try:
          tpl = ('js',getProperUrl(baseurl,link['src'] ), 'js', 'No-title',baseurl,depth+1)
          if self.checkCrawnCondition(tpl):
                tplh = self.linkStoreHash(tpl)
                link['src'] = self.reconstractHyperLink(tplh)              
                
        except Exception ,e :
          print 'ERROR',e

      links = soup.find_all("a")
      for link in links:
        try:
            tpl = ('html',getProperUrl(baseurl,link['href']),'html',link.text,baseurl,depth+1)
            if self.checkCrawnCondition(tpl):
                tplh = self.linkStoreHash(tpl)
                link['href'] = self.reconstractHyperLink(tplh)
        except Exception ,e :
            print 'ERROR',e

      links = soup.find_all("img")
      for link in links:
        try:
          a = link['src']
          tpl = ('img',getProperUrl(baseurl,link['src']),a[a.rindex('.')+1:],'No-Title',baseurl,depth+1)
          if self.checkCrawnCondition(tpl):
                tplh = self.linkStoreHash(tpl)
                link['src'] = self.reconstractHyperLink(tplh)
        except Exception ,e :
          print 'ERROR',e
      # -- Insert 5 custom CSS Stype ----------
      for i in range(1,6):
        new_tag = soup.new_tag("link")
        new_tag['rel'] ='stylesheet'
        new_tag['href'] = "../css/mycustom"+str(i)+".css"
        soup.head.insert(-1, new_tag)

      return soup.prettify("utf-8")
  def save_data(self, html,linkTPL):
      """
      Save data with name in relative directory
      """
      #pdb.set_trace()
      try:
          NammedTPL = self.linkStoreHash(linkTPL)
          name = NammedTPL[0]
          ext = NammedTPL[1][0]
          f= open(os.path.join(self.PATH_ROOT,ext,name),'wb')
          f.write(html)
          f.close();
          self.COMPLETE_URL_MAP[NammedTPL[1][1]] = (name,NammedTPL)
      except Exception ,e :
          print 'ERROR',e
  def thread_run(self):
    tplh = self.linkStoreHash(self.start_tpl)
    threads =[]
    count = 0;
    while(not self.PENDING_URL_QUEUE.empty()):
      while(threading.activeCount()< self.MAX_THREAD):
        next = self.PENDING_URL_QUEUE.get()
        thd = myThread(count,next[1],self)
        threads.append(thd)
        thd.start()
        count = count +1
    # Wait for all threads to complete
    for t in threads:
      t.join()
    self.exit()
  def non_thread_run(self):
    tplh = self.linkStoreHash(self.start_tpl)
    count = 0;
    while(not self.PENDING_URL_QUEUE.empty()):
      next = self.PENDING_URL_QUEUE.get()
      print '>>> [%s] Processing %s' %(count, next[1][1]) 
      self.download_change_save( next[1])
      count = count +1
    self.exit()
  def exit(self):
    # Store the Data in a pkl.
    pickle.dump( self.COMPLETE_URL_MAP, open( os.path.join(self.PATH_ROOT,'url_map.pkl'), "wb" ) )

class CustomizeManager:
  def __init__(self):
    pass
  def read_data(self):
    self.COMPLETE_URL_MAP = pickle.load( open( os.path.join(self.PATH_ROOT,'url_map.pkl'), "rb" ) )

def main():
  wo = WebOffline()
  wo.config(BASE_URL = 'http://www.geeksforgeeks.org/',INCLUDE_ONLY_URL_EXP =[ ],EXCLUDE_URL_EXP =['/forums/'], DEPTH = 20,INDOMAIN=True,ALLOWED_DOMAIN=[],DEBUG=False,MAX_THREAD=10)
  wo.thread_run()
  wo.show_summary()
main()
