#!/usr/bin/python
####################################3
# An command line utility to send sms
# _CopyRight: I got the base code from ineternet and did some modification to make it work
# Date: 31/1/2014
# Author : Dipankar
####################################
import sys
import time
from   urlparse import urlparse,parse_qs
import re
from   time import sleep
import traceback
from ConfigParser import ConfigParser
import pdb

# :Note : Sat Aug 10 20:25:14 IST 2013
#---------------------------------------
# :-D  way2sms is updating their urls/form field names like anything!
# I guess they are struggling with scripts like this. 
# They can prevent the scrapping completely with one single step if they want but 
# they are not doing,don't know why.  :-o
# hmm.. anyway.. its their problem. Lets enjoy the service!
# 
#                                             - Bris

#way2sms credentials.
config = ConfigParser()
config.read("../config.ini")
username = config.get("7waysms", "uname")
password = config.get("7waysms", "password")

#post wait time in seconds, depends on connection speed.
post_wait = 4

#Turn on debug to get additional information
debug = True

#Useragent:
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"

dump_file = "/tmp/way2sms.debug.html"



try:
    import mechanize
except ImportError:
    print "Please install mechanize module for python"
    print "Install python-mechanize, if you are on a Ubuntu/Debian machine"
    sys.exit(1)
try:
    from optparse import OptionParser
except ImportError:
    print "Error importing optparse module"
    sys.exit(1)

 
class smsHandler():
   def __init__(self,username,password):
      print ">>> initializing.."
      if debug:
         print ">>> Debug: ON"
      self.username    = username
      self.password    = password
      self.idreg1      = re.compile("id='m_15_b' value='([A-z0-9]*)'")
      self.idreg1_1    = re.compile("name='m_15_b' id='m_15_b'>([A-z0-9]*)</textarea>")
      self.tknreg      = re.compile("id='t_15_k_5' value='([A-z0-9]*)'")
      self.tknreg_1    = re.compile("name='t_15_k_5' id='t_15_k_5'>([A-z0-9]*)</textarea>")
      self.auto_submit = re.compile(r'document.InstantSMS.action="([./A-z0-9]*)"')
      #self.master      = "http://site3.way2sms.com/entry.jsp"
      self.master       = "http://www.7waysms.com/index.php"     
      self.authurl    = "http://www.7waysms.com/index.php"

      self.homeurl="http://www.7waysms.com/home.php"
      

      self.sendsmsurl = "http://www.7waysms.com/7way_sms_sendv161.php"
      self.smsposturl  = "http://www.7waysms.com/send_v161.php"
      
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
               print ">>> idreg1: OK"
            self.id1 = self.id1[0]
         else:
            if debug:
               print ">>> idreg1: Fail"
               print ">>> Trying idreg1_1.."
            self.id1  = self.idreg1_1.findall(html) 
            if self.id1:
               if debug:
                  print ">>> idreg1_1: OK"
               self.id1 = self.id1[0]
         if not self.id1:
            print ">>> unable to parse m_15_b value."
            print ">>> something got changed at way2sms.com."
            print ">>> This program needs modification."
            sys.exit(1)
         if debug:
            print ">>> Trying first option.."
         self.tkn  = self.tknreg.findall(html)
         if self.tkn:
              if debug:
                 print ">>> First option: OK"
              self.tkn = self.tkn[0]
         else:
              if debug:
                 print ">>> First option failed."
                 print ">>> Trying second option.."
              self.tkn = self.tknreg_1.findall(html)
              if self.tkn:
                 if debug:
                    print ">>> Second option: OK"
                 self.tkn = self.tkn[0]
         if not self.tkn:
            print ">>> Failed to get token info for your login"
            print ">>> This program needs to be updated."
            print ">>> Exiting.."
            sys.exit(1)
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
          sys.exit(1)

   def get_token(self,url):
       urlhandle  = urlparse(url)
       info       = parse_qs(urlhandle.query)
       self.token = info['id'][0]

   def do(self,mobile,text):
       #pdb.set_trace()
       print ">>> connecting to way2sms..."
       try:
          #pdb.set_trace()
          response = self.br.open(self.master)
          print 30 * "-"  
          print self.br.title()
          print 30 * "-"
          print ">>> %s/HTTP: %s" %  (self.master,response.code)
          self.br.select_form(name="login")
          self.br["mobile_no2"] = self.username
          self.br["password"] = self.password
          self.br.form.method="POST"
          self.br.form.action=self.authurl
          response = self.br.submit()
          if debug:
             print ">>> %s/HTTP: %s" %  (response.geturl(),response.code)
          print '>>> Login Done'
          print 30 * "-"  
          print self.br.title()
          print 30 * "-"
          for i in range(10):
              response = self.br.open(self.sendsmsurl)
              self.br.select_form(name="aby1")
              self.br["mobile_no"] = self.username
              self.br["message"] = self.password
              self.br.form.method="POST"
              self.br.form.action=self.smsposturl
              response = self.br.submit()
              self.br.select_form(nr=0)
              response = self.br.submit()
              xx = response.read();
              if 'Successfully' in xx:
                  print '>>> MSG SENT',str(i)
         
       print ">>> Closing session.."
       self.br.close()
       print ">>> Done."

def main():
       handler = smsHandler(username,password)
       handler.do('8147830733','text')

if __name__ == "__main__":
   main()
