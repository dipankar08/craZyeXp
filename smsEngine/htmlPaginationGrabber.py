import requests
from bs4 import BeautifulSoup

def getHTMLPaginationContent(first_url,max_count=99999):
  msg_list=[]
  cur_count =0;
  while(first_url):
    print 'reading '+first_url+'...'
    resp = requests.get(first_url)
    html = resp.text
    soup = BeautifulSoup(html)
    ######## Dig the Content and Populate the list ###
    content = soup.find('div',{'class':'blog'}).find_all('div',{'class':'article_column'})
    for c in content:
      msg_list.append(c.find_all('p')[1].text)
      cur_count +=1
      if cur_count == max_count:
        return msg_list
    
    ######## Find The next Page in the pagination ####
    page = soup.find('ul',{'class':'pagination'})
    next_page = None
    for a in page.find_all('a'):
      if a.text =='Next':
        next_page = a['href']
    first_url = next_page
  return msg_list
  
### Sample Test ###
s = getHTMLPaginationContent("http://g10sms.com/sms140/english/love/",20)
print 'msg count',len(s)


############# Send this to Dipankar in every 10 Minites ##########
import time
import traceback
from ConfigParser import ConfigParser
import way2sms
import one6tiby2
default_service = "way2sms"
config = ConfigParser()
config.read("../config.ini")
username = config.get(default_service, "uname")
password = config.get(default_service, "password")
for es in s:
  handler = way2sms.smsHandler(username,password)
  handler.do('8880428779',es)
  time.sleep(600)
  

    
    
    
  