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

post_wait = 4

#Turn on debug to get additional information
debug = False

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
      if debug:
         print ">>> initializing.."
         print ">>> Debug: ON"
      self.username    = username
      self.password    = password
      self.is_auth = False
      
      self.LOGIN_TEXT  = '<span>Logout</span>'
      self.idreg1      = re.compile("id='m_15_b' value='([A-z0-9]*)'")
      self.idreg1_1    = re.compile("name='m_15_b' id='m_15_b'>([A-z0-9]*)</textarea>")
      self.tknreg      = re.compile("id='t_15_k_5' value='([A-z0-9]*)'")
      self.tknreg_1    = re.compile("name='t_15_k_5' id='t_15_k_5'>([A-z0-9]*)</textarea>")
      self.auto_submit = re.compile(r'document.InstantSMS.action="([./A-z0-9]*)"')
      #self.master      = "http://site3.way2sms.com/entry.jsp"
      self.master       = "http://site4.way2sms.com/content/index.html"
      
      self.authurl    = "http://site4.way2sms.com/Login1.action"
      #self.authurl     = "http://site1.way2sms.com/w2sauth.action"
      
      #self.sendsmsurl  = "http://site1.way2sms.com/jsp/SingleSMS.jsp"
      self.sendsmsurl = "http://site4.way2sms.com/singles.action"
      
      #self.smsposturl  = "http://site1.way2sms.com/jsp/m2msms.action"
      #self.smsposturl  = "http://site1.way2sms.com/jsp/stp2p.action"
      #self.smsposturl  = "http://site4.way2sms.com/stp2p.action"
      self.smsposturl  = "http://site4.way2sms.com/smstoss.action"
      
      self.br = mechanize.Browser()
      self.br.addheaders = [{"User-Agent":user_agent,
                           "Referer": "%s" % (self.master)}]    
      if debug: print ">>> connecting to way2sms..."
      try:
          response = self.br.open(self.master)
          if debug:
             print ">>> %s/HTTP: %s" %  (self.master,response.code)
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
             print ">>> %s/HTTP: %s" %  (self.authurl,response.code)
      except (mechanize.HTTPError,mechanize.URLError) as e:
           if isinstance(e,mechanize.HTTPError):
                if e.code == 404:
                     print ">>> way2sms have changed their login url."
                     print ">>> This program needs to be updated."
           return
      except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> FATAL: Error occured while performing process!"
          return
      #pdb.set_trace()
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
      if self.LOGIN_TEXT in response.read():
         self.is_auth = True
      #pdb.set_trace()        
      # At this point auth is Done...
       
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
            #sys.exit(1)
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
            #sys.exit(1)
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
          #sys.exit(1)

   def get_token(self,url):
       urlhandle  = urlparse(url)
       info       = parse_qs(urlhandle.query)
       self.token = info['id'][0]

   def do(self,mobile,text):
       #pdb.set_trace()
       if debug:
         print ">>> sending message..."
         print ">>> Opening %s?Token=%s" % (self.sendsmsurl,self.token)
       self.br.addheaders = [{"User-Agent": user_agent, 
                               "Referer": "%s?Token=%s" % (self.sendsmsurl,self.token)}]
       r = self.br.open("%s?Token=%s" % (self.sendsmsurl,self.token))
       if debug:
          print ">>> %s/HTTP: %s" %  (self.sendsmsurl,r.code)

       self.br.select_form(name="InstantSMS")
       if debug:
          print ">>> Setting InstantSMS form readonly: False."
       self.br.form.set_all_readonly(False)
       response_html = r.get_data()
       try:
          self.coock_controls(response_html)
          if debug: print ">>> ID1: %s, TKN:%s" % (self.id1,self.tkn)
       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Error occured while processing dynamic ids."
          print ">>> Exiting."
          #sys.exit(1)
       if debug:
          print ">>> Filling up form details.."
       try:
          #Override new js dynamic controls.
          #Lets hope the dynamic fields id won't change ;-)
          self.br.form.new_control('text',self.id1,{'value':mobile})
          self.br.form.new_control('text',self.tkn,{'value':self.token})
          self.br["textArea"]   = text
          self.br.form.method="POST"
          self.br.form.action=self.smsposturl
          self.br.form.fixup()
       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Error occured while processing InstantSMS form."
          print ">>> Exiting."
          #sys.exit(1)
       if debug: print ">>> submitting..."

       try:
          response = self.br.submit()
          if debug:
             print ">>> %s/HTTP: %s" %  (self.smsposturl,response.code)

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
                     #sys.exit(1)

       except:
          if debug:
             print "Debug information"
             print 25 * "*"
             print traceback.format_exc()
             print 25 * "*"
          print ">>> Error occured while submitting InstantSMS form."
          print ">>> Exiting."
          #sys.exit(1)
       if debug: print ">>> Waiting...%s sec/POST wait." % post_wait
       sleep(post_wait)
       print '>>> Successfuly send %s to %s ' %(text,mobile)
       if debug:
          print ">>> %s/HTTP: %s" %  (response.geturl(),response.code)
       else:
          print response.geturl()
       if debug: print ">>> Closing session.."
       self.br.close()
       print ">>> Done."

def main():
    parser = OptionParser()
    usage = "Usage: %prog -m [number] -t [text]"
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option("-m", "--number",  action="store", type="string",dest="number",  help="Mobile number to send sms")
    parser.add_option("-t", "--text", action="store", type="string", dest="text", help="Text to send")
    (options, args) = parser.parse_args()
    
    if options.number and options.text:
       text = options.text +' '+ ' '.join(args)
       handler = smsHandler(username,password)
       handler.do(options.number,text)
    else:
       print "Fatal: Required arguments are missing!"
       print "Use: -h / --help to get help."

if __name__ == "__main__":
   pass #main()
