####################3
# Hack Bengali Matrimony...
# Serach List of MID : http://profile.bengalimatrimony.com/pinnableprofile/pinnableprofilecore.php?randid=2037123500&time=9991861111111 STLIMIT=61
# Profile : http://profile.bengalimatrimony.com/profiledetail/viewprofile.php?id=K893765
# Pic Link: From Profile Link you can get that.
# 
#######################


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
import requests

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
    
    def store_photo(self,uid,url): # IN BM We need to pass URL as it conatisn Random number :(
        " getting photoes"
        # Getting Dir
        if not os.path.exists(self.PHOTO_PATH):
            os.makedirs(self.PHOTO_PATH)

        #Check in cache.
        if os.path.exists(self.PHOTO_PATH+str(uid)+'_0.jpg'):
          print '>>> Already Photo Exist! return.., Still We are not check if all photo or not !)'
          return;
        print '>>> Photo are not in cache.. let"s download...'

        # Initialize data
        global PROFILE_INFO
        pd = PROFILE_INFO.get(uid)
        if pd:
            pd['PhotoCount']=0
        else:
            PROFILE_INFO[uid]={}
            PROFILE_INFO[uid]['PhotoCount']=0
        try:
          print '>>> Reading %s ...'% url
          resp = self.br.open(url)
          html = resp.read()
          soup = BeautifulSoup(html)
        except Exception,e  :
          print '>>> ERROR while readading',url ,e
        count = 0
        try:
          for s in soup.find('div',{'class':'ad-nav'}).find('ul').find_all('a'):
            try:
                data_url= s['href']
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
        
        PROFILE_INFO[uid]['PhotoCount']=count
        
        
    def get_info(self,uid):
        "getting Data and Picking data"
	global PROFILE_INFO
        pd = PROFILE_INFO.get(uid)
        if  not pd:
            PROFILE_INFO[uid]={}
            pd = PROFILE_INFO[uid]
        ### Initialize
	pd['PhotoCount']=0
	pd['name'] =  None
        pd['id'] = None
	pd['about_me'] =None
	pd['pic_url'] =None
        try:    
        	url = self.profile_url+str(uid)
        	print '>>> Reading profile info: %s ...', url
        	resp = self.br.open(url)
        	html = resp.read()
        	soup = BeautifulSoup(html)
	except Exception,e:
		print ">>> ERROR while reading ",url,e
        try:
            pd['name'] = clean_text(soup.find('div',{'id':'vps_'+uid}).text)
        except:
            pd['name'] =  None
        try:
            pd['id'] = uid
        except:
            pd['id'] = None
        try:
            pd['about_me'] = clean_text(soup.find('div',{'id':'vp-details'}).find('div',{'class':'lheight16'}).text)
        except:
            pd['about_me'] =None
        try:
            x = re.findall(r",'(.*?viewphoto.*?)'",html)[0]
            pd['pic_url'] = x[x.rfind('http'):]
        except:
            pd['pic_url'] =None
        ########
        try:
            self.store_photo(uid=uid,url=pd['pic_url'])
        except Exception,e:
          print 'Error',e
        
        #pdb.set_trace()
        return pd

        
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

      self.login_page = 'http://profile.bengalimatrimony.com/login/logout.php'
      self.login_target = 'https://secure.bengalimatrimony.com/login/memlogin.php'
      self.myhome ='http://profile.bengalimatrimony.com/login/myhome.php'
      self.search_form='http://profile.bengalimatrimony.com/search/search.php'
      self.all_serach ='http://profile.bengalimatrimony.com/pinnableprofile/pinnableprofilecore.php?randid=2037123500&time=9991861111111'
      self.photo_url = None
      self.profile_url ='http://profile.bengalimatrimony.com/profiledetail/viewprofile.php?id='#K893765'

      self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
      
      self.br = mechanize.Browser()
      print '>>> Open Login page'+site
      print '>>> Reading %s ...', self.login_page

      self.br.set_handle_robots(False)
      self.br.set_handle_equiv(False)
      self.br.open(self.login_page)
      self.br.select_form('Login')
      self.br['ID']='B861149'
      self.br['PASSWORD']='9933588184'
      self.br.form.method="POST"
      self.br.form.action=self.login_target
      
      print '>>> Reading %s ...', self.login_target
      response = self.br.submit()

      print '>>> Reading %s ...', self.myhome
      resp = self.br.open(self.myhome)
      if 'B861149' in resp.read():
        print '>>> Login Done..'
      else:
        print '>>> Auth Failed'
      print '*'*50;print self.br.title(); print '*'*50
      
    def do_serach(self):
      global SEARCH_INFO
      load =  load_site_data(self.login_page,ext='search')
      if load:
          print'>>> Profile Count: %s' %len(load)
          SEARCH_INFO = load
          return load
          
      print '\n>>> Opening Serach page...'
      self.global_list =[]
      #pdb.set_trace()
      resp = self.br.open(self.all_serach)
      html = resp.read()
      total_record = re.findall(r"Jsg_tot_rec='(.*?)'",html)[0] #19990
      page_number = int(total_record)/10 # 1999
      for i in range(page_number):        
        HTML ="""<form method='post' action='http://profile.bengalimatrimony.com/pinnableprofile/pinnableprofilecore.php?randid=2037123500&time=9991861111111'>
            <input type='text' name='STLIMIT',value='91'>
            <input type='text' name='password'>
            <input type='hidden' name='important_js_thing' value='processed_with_python TM'>
            </form>"""
        res = mechanize._form.ParseString(HTML, self.all_serach)
        self.br.form = res[1]
        #continue as if the form was on the page and selected with .select_form()
        self.br['STLIMIT'] = str(i*10+1)
        resp = self.br.submit()
        #print '>>> Reading... ',self.br.click().geturl(),'with data:',self.br.click().get_data()
        print '>>> Reading page %s...' %i
        html = resp.read()
        #resp = self.br.open(self.all_serach)
        print re.findall(r'"MId":"(.*?)"',html)
        
        y = re.findall(r'"MId":"(.*?)"',html)
        self.global_list+= y
        for x in y:
          self.pid_q.put(x)

      print '\n>>> Search Successful. We found total(%s) contacts.' % len(self.global_list)
      save_site_data(self.login_page,self.global_list,ext='serach')
      SEARCH_INFO = self.global_list
      return self.global_list

######### Main Program #########
def main():
    MAX_THREAD = 81
    t_list = []
    tcount =0;
    pindo = load_site_data('http://profile.bengalimatrimony.com/',ext='profile')
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
    save_site_data('http://profile.bengalimatrimony.com/',PROFILE_INFO,ext='profile')
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
#print conn.get_info('K569770')
#print x
#print '>>>>>>>>>>>',len(x)
#conn.get_info('BSH89615514')
#print PROFILE_INFO
          
      
      
      
      
      
      
      



      
