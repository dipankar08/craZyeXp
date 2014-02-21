####################################3
# An command line utility to send sms Uinsg 160by2
# _CopyRight: I got the base code from ineternet and did some modification to make it work
# Date: 31/1/2014
# Author : Dipankar
####################################


#!/usr/bin/python
import sys
import time
from   urlparse import urlparse,parse_qs
import re
from   time import sleep
import traceback
from ConfigParser import ConfigParser
import pdb
import cookielib
import urllib2


#160by2 credentials.
#config = ConfigParser()
#config.read("config.ini")
#username = config.get("160by2", "uname")
#password = config.get("160by2", "password")
#import pdb

#post wait time in seconds, depends on connection speed.
post_wait = 3

#Turn on debug to get additional information
debug = False

#Useragent:
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"

dump_file = "/tmp/160by2.debug.html"



try:
    import mechanize
except ImportError:
    print "Please install mechanize module for python"
    print "Install python-mechanize, if you are on a Ubuntu/Debian machine"
    
try:
    from optparse import OptionParser
except ImportError:
    print "Error importing optparse module"
   

 
class smsHandler():
   def __init__(self,username,password):
      #print ">>> initializing.."
      if debug:
         print ">>> Debug: ON"
      self.username    = username
      self.password    = password
      
      self.idreg1      = re.compile('class="ip-l bc1 beta he pH" id="([A-z0-9]*)"')

      self.master       = "http://www.160by2.com/Index"      
      self.authurl    = "http://www.160by2.com/re-login"
      self.sendsmsurl = "http://www.160by2.com/SendSMS"
      self.smsposturl  = "http://www.160by2.com/SendSMSDec19"
      
      
      br = mechanize.Browser()
      cj = cookielib.LWPCookieJar()
      br.set_cookiejar(cj)

      br.set_handle_equiv(True)
      #br.set_handle_gzip(True)
      br.set_handle_redirect(True)
      br.set_handle_referer(True)
      br.set_handle_robots(False)

      br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
      
      self.br = mechanize.Browser()
      self.br.addheaders = [{"User-Agent":user_agent,
                           "Referer": "%s" % (self.master)}]    

   def coock_controls(self,html):
       try:
         if debug:
            print ">>> Trying irreg1.."
         self.id1  = self.idreg1.findall(html)
         if self.id1:
            if debug:
               print ">>> Token Recived: OK"
            self.id1 = self.id1[0]
         if not self.id1:
            print ">>> unable to parse m_15_b value."
            print ">>> something got changed at way2sms.com."
            print ">>> This program needs modification."
            return
       except:
          if debug:
             print "Dumping to: %s " % dump_file
             f = open('%s' % dump_file ,'w')
             f.writelines(html)
             f.close()
          print ">>> Error occured in coock_controls()"
          print ">>> Possible options includes: "
          print " 1. way2sms changed their form field names."
          print " 2. did not receive proper ids from SingleSMS.jsp"
          print " Exiting.."
          return
          
   def get_token(self,url):
       urlhandle  = urlparse(url)
       info       = parse_qs(urlhandle.query)
       self.token = info['id'][0]

   def do(self,mobile,text):
       #pdb.set_trace()
       if debug:
         print "\n>>> connecting to 162by2.com..."
       try:
          response = self.br.open(self.master)
          if debug:
             print ">>> Connected. Path %s Status: %s" %  (self.master,response.code)
          self.br.select_form(name="loginform")
          self.br["username"] = self.username
          self.br["password"] = self.password
          self.br.form.method="POST"
          self.br.form.action=self.authurl
          if debug:
            print 30 * "-"  
            print self.br.title()
            print 30 * "-"  
          response = self.br.submit()
          if debug:
             print ">>> Done. Path %s Status: %s\n" %  (self.authurl,response.code)
       except (mechanize.HTTPError,mechanize.URLError) as e:
           if isinstance(e,mechanize.HTTPError):
                if e.code == 404:
                     print ">>> way2sms have changed their login url."
                     print ">>> This program needs to be updated."
       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> FATAL: Error occured while performing process!"
          return

       if debug:
         print "\n>>> Get the  Token..."
       try:
          self.get_token(response.geturl())
       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Did not get proper Token ID/Error occured."
          print ">>> Please check your username/password."
          return
       if debug:
         print ">>> Received Token: %s" % self.token
       
       
       if debug:
         print "\n>>> Opening SmS From..."
         print ">>> Opening %s?id=%s" % (self.sendsmsurl,self.token)

       self.br.addheaders = [
       {"User-Agent": user_agent,
       "Referer": "%s?id=%s" % (self.sendsmsurl,self.token),
       }]

       #pdb.set_trace()
       r = self.br.open("%s?id=%s" % (self.sendsmsurl,self.token))
       if debug:
          print ">>> Done. Url: %s Status: %s" %  (self.sendsmsurl,r.code)
          print "\n>>> Sending SMS..."
          
       self.br.select_form(name="frm_sendsms")
       if debug:
          pass
       self.br.form.set_all_readonly(False)
       response_html = r.get_data()
       try:
          self.coock_controls(response_html)
          
          if debug:
            print ">>> Variable Token : %s" % (self.id1)
       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Error occured while processing dynamic ids."
          print ">>> Exiting."
          return
       if debug:
          print ">>> Filling up form details.."
       try:
          
          #Override new js dynamic controls.
          #Lets hope the dynamic fields id won't change ;-)
          self.br[self.id1]= mobile
          #self.br.form.new_control('text',self.tkn,{'value':''}) 
          self.br['maxwellapps'] =self.token
          self.br['hid_exists']='no'
          self.br['fkapps']='SendSMSDec19'
          self.br["sendSMSMsg"]   = text
          
          self.br["by2Hidden"] ="by2sms"
          self.br["UgadHieXampp"] ="ugadicome"
          self.br["aprilfoolc"] ="HoliWed27"
          self.br["reminderDate"] ="01-02-2014"
          self.br.form.new_control('text',"messid_0",{'value':'abc'})
          self.br.form.new_control('text',"messid_1",{'value':'abc'})
          self.br.form.new_control('text',"messid_2",{'value':'abc'})
          self.br.form.new_control('text',"messid_3",{'value':'abc'})
          self.br.form.new_control('text',"messid_4",{'value':'abc'})
       
          
          
          self.br.form.method="POST"
          self.br.form.action=self.smsposturl
          #self.br.form.fixup()
       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Error occured while processing InstantSMS form."
          print ">>> Exiting."
          return
       if debug:
         print "\n>>> Submitting SMS..."
       #pdb.set_trace()
       try:
          #response = self.br.submit()
          ##############################This is Vert Tricky on eas cookie send in request ##########
          if debug:
            print '>>> Creating Header .. This is an Hack by send cookie-string in GET Request.'
          myheaders = [
           ("User-Agent", user_agent),
           ("Referer", "%s?id=%s" % (self.sendsmsurl,self.token)),
           ( "Host","www.160by2.com"),
            ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0"),
            ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
            ("Accept-Language","en-us,en;q=0.5"),
            ("Accept-Encoding","gzip, deflate"),
            ("Accept-Charset","ISO-8859-1,utf-8;q=0.7,*;q=0.7"),
            ("Connection","keep-alive"),
            ("Cookie",'__gads=ID=8f03a8b282e76a1a:T=1391237241:S=ALNI_MbHkN5hZJg-WUUwOAnYVzMEXW2LTQ; _ga=GA1.2.1334230594.1391237244; '+ '; '.join([str(v.name)+'='+str(v.value) for k,v in self.br._ua_handlers['_cookies'].cookiejar._cookies['www.160by2.com']['/'].items()]) + '; adCookie=3; shiftpro=axisproapril8th;')
           ]
          LoginUrl = self.smsposturl
          LoginData = self.br.click().data
          LoginHeader = dict(myheaders)

          LoginRequest = urllib2.Request(LoginUrl, LoginData, LoginHeader)          
          if debug:
            print '>>> Sending request ...'
          response = self.br.open(LoginRequest)
          ##############################
          
          if debug:
             print ">>> Status URL: %s  Status: %s" %  (self.smsposturl,response.code)

       except (mechanize.HTTPError,mechanize.URLError) as e:
           if isinstance(e,mechanize.HTTPError):
                if e.code == 404:
                     if debug:
                        print ">>> Looks like instant sms submit url got changed."
                        print ">>> Trying auto.."
                        urldata = self.auto_submit.findall(response_html)
                        print "URL DATA ===>" , urldata 
                     print 50 * '*'
                     print " * way2sms have changed the SMS submit url."
                     print " * This program needs to be updated."
                     print 50 * '*'
                     return

       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Error occured while submitting InstantSMS form."
          print ">>> Exiting."
          return
       if debug:
         print ">>> Waiting...%s sec as a POST wait." % post_wait
       sleep(post_wait)
       print '>>> Successfuly send %s to %s ' %(text,mobile)
       print ">>>SMS Sent Succesfully.. %s/HTTP: %s" %  (response.geturl(),response.code)

       if debug:
         print ">>> Closing session.."
       self.br.close()
       if debug:
         print ">>> Done."

