################ ScanData ####################
import requests
from time import sleep
from bs4 import BeautifulSoup
import pdb
class scrapData:
  def __init__(self,baseurl=""):
    self.BASE_URL = baseurl
    self.SOUP = None
    
    
  def getPage(self,url="http://www.careercup.com/",validate="Yahoo Interview Questions"):
    print '>>> INFO : Geting page %s .....' %url
    try:
      for i in range(5): # Try max 5 mines
        r = requests.get(url)
        print '>>> INFO Donlowed ',r.url
        print '>>> INFO : Geting page %s DONE'
        ans = r.text;
        if not validate: 
          return ans;
        else:
          if validate in ans:
            return ans;
          else: 
            print '>>> ERROR : Opps the site make some twics.... wait for 30 sec and retry ID:',i
            sleep(60)
      return None
      
    except Exception ,e:
      print 'Error Wile downlaod:',e
      return None
  def buildSoup(self,a):
    self.SOUP = BeautifulSoup(a) 
    
  
  def getSelectorContant(self,selector='div.a div > pre.h1'):
    if  self.SOUP ==None:
      print 'ERROR No Soup Ready.. return '
      return
    else:
      now = s.SOUP.select(selector)
      if len(now)==1:
        return now[0]
      else:
        return now;
  def getAllHyperLink(self,selector):
    print '>>> INFO : Geting All Hyperlink for  %s .....' %selector
    if  self.SOUP ==None:
      print 'ERROR No Soup Ready.. return '
      res = []
    else:
      now = s.SOUP.select(selector)
      if not now:
        print 'ERROR: selector dont select anything..'
      res=[]
      for n in now:
        for a in n.findAll('a'):
          res.append((a.text,a['href']))
    print '>>> INFO : Geting All Hyperlink Done'
    return res
  def norn(self,bs_data):
    try:
      if bs_data.has_attr('href') == True:
        return bs_data['href']
      else:
        return bs_data.text
    except Exception,e:
      print '>>> Error at norn()',e
      #pdb.set_trace()
  def getSelectedDataInAContiner(self,c_selector,d_selector={'title':'h4','link':'a'}):
    print '>>> INFO : start getSelectedDataInAContiner'
    if  self.SOUP ==None:
      print 'ERROR No Soup Ready.. return '
      res= []
    else:
      now = s.SOUP.select(c_selector)
      if not now:
        print 'ERROR: ContainerSelcetor looks like Empty<c_selector:%s>'%c_selector
        #pdb.set_trace()
        return None
   
      res=[]
      for n in now:
        tip={}
        for x,y in d_selector.items():
          tip[x]=n.select(y)
          if(len(tip[x]) > 1):
            print '>>> WARN.. Multiple data ..takeing first data'
            tip[x]=tip[x][0]
          #Normalazied: 
          #pdb.set_trace()
          tip[x] = self.norn(tip[x])
          res.append(tip)
    print '>>> INFO : End getSelectedDataInAContiner'
    return res;
  
  def iterateOverNextByPagination(self,n_url=None):
    """ Get Next page URL"""
    print '>>> INFO : start iterateOverNextByPagination'
    try:
      #NOTE THAT IN THIS CASE WE SOND NOT HAVE ANY INTEGER..
      a= n_url
      i = [x.isdigit() for x in a].index(True)
      j = [x.isdigit() for x in a[::-1]].index(True)
      #pdb.set_trace()
      if j ==0: # number at last
        a = a[:i]+str(int(a[i:])+1) 
      else:
        a = a[:i]+str(int(a[i:-j])+1)+a[-j:]
    except Exception,e:
      print 'Error: Not able to do iterateOverNextByPagination for :',n_url
      print e
    print '>>> INFO : End iterateOverNextByPagination to %s'%a
    sleep(2)
    
    return a
  def iterateOverNextBySelector(self,soup=None, n_selector=None):
      """ Get Next page URL"""
      # HEHE BASE is SOUP OBJ  ans Slecetor indiacte the URL to get next <a> Elements
      a=soup.select(n_selector)
      if len(a)==0 :
        return None; # loops ends Here..
      else:
        a=a[0]['href']
      return a
  ########################################
  # url : Give the base url
  # f_c_selctor : First lelevl(listing page) Continer Selecor
  # f_data: data to be taken from Listing page
  # n_url : url to  if we are using pagination to go next link
  # n_selector: Use of Selctor to go to next link.
  # s_c_selector: Second Lvele(Detils page) container selctor)
  # s_data : Second Level to gather data
  ########################################
  def TwoLevelDataRetrival(self,url,f_c_selctor='',f_data={},n_url=None,n_selector=None,s_c_selector='',s_data={},dry_run=False, \
  f_page_limit =None,f_entry_limit=None):
    if n_url:
      url =n_url;
    self.buildSoup(url);
    list_data=[]
    while True:
      if url == None:
        break;
      if dry_run : print '>>> DRYRUN url is : %s'% url 
      html = self.getPage(url)
      if not html:
        break
      self.buildSoup(html)
      print '>>>>>>>>>>.  Processing <<<<<<<<<<<<<<',url
      data = self.getSelectedDataInAContiner(f_c_selctor,f_data)
      if dry_run : 
        print '>>> DRYRUN Number of Entry Found is:',len(data)
        print '>>> DRYRUN Data Selected by %s is :'% f_c_selctor
        for k,v in data[0].items():
          print '>>> DRYRUN %s ==> %s' %(k,v)
      if data==None:
        print '>>> INFO completed!'
        break;
      list_data += data 
      if n_url:
        url =  self.iterateOverNextByPagination(n_url=url)
      else:
        url =  self.iterateOverNextBySelector(soup=self.SOUP, n_selector=n_selector)
      if dry_run : 
        print '>>> DRYRUN Next Url to process : %s'% url
        break ; # break the loop as it is a dry run.
    print list_data
    print  len(list_data)
# test 
html="""
<html>
<body>
  <div class="a">
    <div id="1"></div>
    <div id="1"></div>
    <div id="3"></div>
    <div id="4">
      <pre class="h1"> 
      </pre>
      <pre class="h2"> 
      </pre>
      <pre class="h3"> 
      </pre>
    </div>
  </div>
  <pre id="1">
  </pre>
</body>
</html>
"""
s= scrapData()
s.TwoLevelDataRetrival(url="http://www.careercup.com/page?pid=yahoo-interview-questions",f_c_selctor="#question_preview .question",f_data={'url':'.entry a','rating':'.commentCount'},n_url="http://www.careercup.com/page?pid=yahoo-interview-questions&n=1",dry_run=True)
