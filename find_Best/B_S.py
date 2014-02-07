#!/usr/bin/python
import sys
import time
import urlparse
import re
from   time import sleep
import traceback
from ConfigParser import ConfigParser
import pdb
import cookielib
import urllib2
import mechanize
from bs4 import BeautifulSoup
import os
import Queue
import threading
import pickle

############ Global Functions ###############################
PROFILE_INFO={}
SEARCH_INFO= []


# Help Function for Save and Restore WebSite Data ########
def getSiteKey(url):
  " return Site key as a domain name"
  netloc =  urlparse.urlparse(url).netloc
  netloc = netloc.replace("www.", "")
  return netloc

def save_site_data(url,data,ext=''):
  file_name =  getSiteKey(url)+'_'+ext+'.pkl'
  pickle.dump( data, open( file_name, "wb" ))

def load_site_data(url,ext=''):
    file_name =  getSiteKey(url)+'_'+ext+'.pkl'
    try:
      return pickle.load( open( file_name, "rb" ) )
    except:
      print 'No store data found for '+file_name
      return None
# Helper Function for makeing clean HTML data
def clean_text(s):
  """ Helper function remove all \n \t \r etc"""
  s = re.sub( '[\n\t\r\s]+', ' ', s ).strip()
  #s.decode('unicode_escape').encode('ascii','ignore')
  return s

class HTML_Handaler():
    
    def store_photo(self,uid):
        " getting photoes"
        # Getting Dir
        if not os.path.exists(self.PHOTO_PATH):
            os.makedirs(self.PHOTO_PATH)

        #Check in cache.
        if os.path.exists(self.PHOTO_PATH+str(uid)+'_0.jpg'):
          print '>>> Already Photo Exist! return.., Still We are not check if all photo or not !)'
          return;
        print '>>> Photo are not in cache.. let"s download...'

        url = self.photo_url+str(uid)
        print '>>> Reading %s ...'% url
        resp = self.br.open(url)
        html = resp.read()
        soup = BeautifulSoup(html)
        count = 0
        try:
          for s in soup.find('div',{'id':'slideshow-main'}).find('ul').find_all('img'):
            try:
                data_url= s['src']
                print '>>> Reading %s ...' %data_url
                self.br.set_handle_robots(False)
                image_response = self.br.open_novisit(data_url)
                with open(self.PHOTO_PATH+str(uid)+'_'+str(count)+'.jpg', 'wb') as f:
                    f.write(image_response.read())
                count = count +1
            except Exception ,e:
                print '>>> [ERROR] Not able to pic %s due to %s' % (data_url,e)
        except:
            print '>>> [ERROR] Not able to get pic'
        print '>>> The count of image found is %s' % count
        pd = PROFILE_INFO.get(uid)
        if pd:
            pd['PhotoCount']=count
        else:
            PROFILE_INFO[uid]={}
            PROFILE_INFO[uid]['PhotoCount']=count
        
        
    def get_info(self,uid):
        "getting Data and Picking data"

        pd = PROFILE_INFO.get(uid)
        if  not pd:
            PROFILE_INFO[uid]={}
            pd = PROFILE_INFO[uid]
            
        url = self.profile_url+str(uid)
        print '>>> Reading profile info: %s ...', url
        resp = self.br.open(url)
        html = resp.read()
        soup = BeautifulSoup(html)
        try:
            pd['name'] = soup.find('span',{'class':'prof_username'}).text
        except:
            pd['name'] =  None
        try:
            pd['id'] = soup.find('span',{'class':'prof_uid'}).text
        except:
            pd['id'] = None
        try:
            pd['about_me'] = clean_text(soup.find('div',{'class':'about_self'}).text)
        except:
            pd['about_me'] =None
        return 

        
    def __init__(self,site='bengalishaadi',username='dutta.dipankar08@gmail.com',password='9933588184'):

      self.PHOTO_PATH = './Photos/'

      #use number of Queue for Fast processing using threading
      self.pid_q = Queue.Queue()
      
      self.br = mechanize.Browser()
      self.cj = cookielib.LWPCookieJar()
      self.br.set_cookiejar(self.cj)

      self.br.set_handle_equiv(True)
      #br.set_handle_gzip(True)
      self.br.set_handle_redirect(True)
      self.br.set_handle_referer(True)
      self.br.set_handle_robots(False)

      self.login_page = 'http://www.bengalishaadi.com/registration/user/login'
      self.login_target = 'http://www.bengalishaadi.com/registration/user/login-submit'
      self.photo_url ='http://www.bengalishaadi.com/profile/index/view-album-photos/profileid/'#1SH12523390'
      self.profile_url ='http://www.bengalishaadi.com/profile?profileid='#eSH31128502'

      self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
      
      self.br = mechanize.Browser()
      print '>>> Open Login page'+site
      print '>>> Reading %s ...', self.login_page
      self.br.open(self.login_page)
      self.br.select_form('frmLogin')
      self.br['email']='DDD'
      self.br['password']='XXX'
      self.br.form.method="POST"
      self.br.form.action=self.login_target
      
      print '>>> Reading %s ...', self.login_target
      response = self.br.submit()
      print '>>> Login Done..'
      print '*'*50;print self.br.title(); print '*'*50
      
    def do_serach(self):
      global SEARCH_INFO
      load =  load_site_data(self.login_page,ext='search')
      if load:
          print'>>> Profile Count: %s' %len(load)
          SEARCH_INFO = load
          return load
          
      print '\n>>> Opening Serach page...'
      self.first_s_url = 'http://www.bengalishaadi.com/search?loc=top-nav'
      self.global_list =[]

      self.br.open(self.first_s_url)
      first_s_url = self.first_s_url
      self.br.select_form('basic')
      resp = self.br.submit()

      while(first_s_url):
          print '>>> Reading %s ...', first_s_url
          html = resp.read()
          
          self.br._ua_handlers['_cookies'].cookiejar
          soup = BeautifulSoup(html)
          for i in soup.find_all('div',{'class':'result_box_nw'}):
              pid = i.find('input',{'type':'checkbox'})['value']
              self.global_list.append(pid )
              self.pid_q.put( pid)
          nexturl = None
          try:
              for i in soup.find('ul',{'class':'pagination_search'}).find_all('a'):
                  if i.get('class') and 'next_pg' in i.get('class'):
                      nexturl= i['href']
              first_s_url = nexturl
          except:
              print '>>> Serach Conpleted.'
              first_s_url = None
          try:
              if first_s_url: resp = self.br.open(first_s_url)
          except:
              print '>>> ERROR2'
          
      print '\n>>> Search Successful. We found total(%s) contacts.' % len(self.global_list)
      save_site_data(self.first_s_url,self.global_list,ext='serach')
      SEARCH_INFO = self.global_list

######### Main Program #########
def main():
    MAX_THREAD = 81
    t_list = []
    tcount =0;
    pindo = load_site_data('http://www.bengalishaadi.com/',ext='profile')
    global PROFILE_INFO
    global SEARCH_INFO
    if pindo : PROFILE_INFO = pindo
    
    conn = HTML_Handaler()
    print '>>> Creating Serach thread(%s)',tcount
    tcount +=1
    s = threading.Thread(target=conn.do_serach)
    t_list.append(s)
    s.daemon = True
    s.start()

    while (s.is_alive() or conn.pid_q.qsize() > 0):
        while( threading.active_count() > MAX_THREAD ):
            time.sleep(10); ## Sleep for 10 sec
        pid = conn.pid_q.get()
        print '>>> Creating Photo Download thread(%s) for %s' %(tcount,pid)
        tcount +=1
        t = threading.Thread(target=conn.store_photo, kwargs={'uid':pid})
        t_list.append(t)
        t.daemon = True
        t.start()

        print '>>> Creating Info Download thread(%s) for %s' %(tcount,pid)
        tcount +=1
        t = threading.Thread(target=conn.get_info, kwargs={'uid':pid})
        t_list.append(t)
        t.daemon = True
        t.start()
        
    # Wait for all threads to complete
    for t in t_list:
        t.join()
    print ">>> Exiting Main Thread"
    
    print ">>> Save Site Data..."
    save_site_data('http://www.bengalishaadi.com/',PROFILE_INFO,ext='profile')
    print '*'*50
    print 'Summary:'
    print 'Total Profile Searched:', len(SEARCH_INFO)
    print 'Total Profile ViewEd:',len(PROFILE_INFO.keys())
    print 'Total Photo Count:', len([name for name in os.listdir(conn.PHOTO_PATH)]),'(',sum([x['PhotoCount'] for x in PROFILE_INFO.values()]),')'
    print '*'*50
    

main()
#print PROFILE_INFO
    
#conn = HTML_Handaler()
#x = conn.do_serach()
#print x
#print '>>>>>>>>>>>',len(x)
#conn.get_info('BSH89615514')
#print PROFILE_INFO
          
      
      
      
      
      
      
      



      
