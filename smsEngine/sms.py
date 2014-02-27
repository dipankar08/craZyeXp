#!/usr/bin/python

####################################3
# Maim Program for sending sms.
# CopyRight: I got the base code from ineternet and did some modification to make it work
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
import pickle
import way2sms
import one6tiby2
import os

######## Config Here ##########
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
CONTACT_FILE_LOC =os.path.join(ROOT_PATH,"contacts.pkl")

def getdata():
  try:
  	contacts = pickle.load( open( CONTACT_FILE_LOC, "rb" ) )
  	return contacts
  except:
        return {}
def savedata(no,name):
  contacts ={}
  try:
    contacts = pickle.load( open( CONTACT_FILE_LOC, "rb" ) )
  except:
    pass
  contacts[no]=name
  
  try:
    pickle.dump(contacts, open(CONTACT_FILE_LOC, "wb" ) )
    print '>>> Data Saved'
  except:
    print '>>> Error Saveing the ontacts'

try:
    from optparse import OptionParser
except ImportError:
    print "Error importing optparse module"
    sys.exit(1)

import pdb
default_service = '160by2'

#post wait time in seconds, depends on connection speed.
post_wait = 3

#Turn on debug to get additional information
debug = False

#Useragent:
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"

dump_file = "/tmp/160by2.debug.html"

def getSmsHandaler(username,password,provider = 'way2sms'):
    """ interface to get a sms handaler - In general"""
    try:
        if provider == 'way2sms':
         return way2sms.smsHandler(username,password)
        else:
         return one6tiby2.smsHandler(username,password)
    except:
        print '>>> [ERROR] Not able to get handaler'
        return None
   

def main():
    parser = OptionParser()
    usage = "Usage: %prog -s [server] -m [number] -t [text]"
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option("-m", "--number",  action="store", type="string",dest="number",  help="Mobile number to send sms")
    parser.add_option("-t", "--text", action="store", type="string", dest="text", help="Text to send")
    parser.add_option("-s", "--server", action="store", type="string", dest="server", help="use 160by2 or way2sms")
    (options, args) = parser.parse_args()

    #Read Credentials
    default_service = "way2sms"
    if options.server and options.server in ['160by2','way2sms']:
        default_service = options.server
    config = ConfigParser()
    config.read("/home/dipankar/myExp/craZyeXp/config.ini")
    username = config.get(default_service, "uname")
    password = config.get(default_service, "password")
    handler = getSmsHandaler(username,password,default_service)
    if not handler: print '>>> Ooops.. Something went Wrong' ; return;
    num =None
    if options.number and options.text:
       text = options.text +' '+ ' '.join(args)       
       num = options.number
       handler.do(num,text)
       name = raw_input(">>> name of this person:")
       if (num not in getdata()) or name: 
         savedata(num,name)
         print '>>> Person Saved'
    elif len(args) >1:
       num =args[0]
       text = ' '.join(args[1:])
       handler.do(num,text)
       name = raw_input(">>> name of this person:")
       if (num not in getdata() )or name:
         savedata(num,name)
         print '>>> Person Saved'
    else:
       print "Ooops ! Looks like you don't know how to use it.It's so simple to use : "
       print "1. python sms.py 8147830733 Hi I am Dipankar"
       print "2. python sms.py -s 160by2 8147830733 Hi! Dipankar again !"
       print "3. python sms.py -s way2sms -m 8147830733 -t Yes ! Dipankar Again!!"
       print "Use: -h / --help to get help.\n"
       print '*'*50
       u = getdata().items()
       if u :
         print 'Save Number is:',
         for k,v in getdata().items():
            print '%s(%s), ' %(k,v),  
       else:
          print 'No saved Number Found.'
       print '\n','*'*50
if __name__ == "__main__":
   main()
