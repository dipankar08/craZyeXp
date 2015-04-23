################ ScanData ####################
import requests
from time import sleep
from bs4 import BeautifulSoup
from urlparse import urlparse
import pdb
class scrapData:
  def __init__(self,baseurl=""):
    self.BASE_URL = baseurl
    self.SOUP = None
    
    
  def getPage(self,url="http://www.careercup.com/",validate="Recent Interview Questions"):
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
  def norn(self,bs_data,y):
    #pdb.set_trace()
    try:
      # y =('.commentCount','first','all','text' | 'link']
      if y[1] == 'link':
        if y[2] =='first':
          return bs_data[0]['href']  
        elif y[2] == 'all':
          return [ t['href'] for t in bs_data ]
        else:
          print 'Unknown attribute ',y[2]
      elif y[1] == 'text':
        if y[2] =='first':
          return bs_data[0].text 
        elif y[2] == 'all':
          return [ t.text for t in bs_data ]
        else:
          print 'Unknown attribute ',y[2]
      else:
        print 'Unknown attribute ',y[1]
    except Exception,e:
      print '>>> Error at norn()',e
      #pdb.set_trace()
  def getSelectedDataInAContiner(self,c_selector,d_selector=None):
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
          tip[x]=n.select(y[0])
          #Normalazied: 
          #pdb.set_trace()
          tip[x] = self.norn(tip[x],y)
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
  f_page_limit =None,f_entry_limit=None,save_name=None):
    if n_url:
      url =n_url;
    b_url = url ;# This is the base url
    print '>>> DL Start processing first level work.....'
    list_data=[]
    f_page_counter = 0;
    f_entry_counter= 0;
    
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
      if(f_entry_limit and len(list_data) >= f_entry_limit):
        print '>>> DL We reaches f_entry_limit, breaking..'
        break
      if n_url:
        url =  self.iterateOverNextByPagination(n_url=url)
      else:
        url =  self.iterateOverNextBySelector(soup=self.SOUP, n_selector=n_selector)
      if dry_run : 
        print '>>> DRYRUN Next Url to process : %s'% url
        break ; # break the loop as it is a dry run.
      f_page_counter+=1
      if f_page_limit and f_page_counter >=f_page_limit:
        print '>>> DL We reaches f_page_limit breaking..'
        break;
      #End of while Loop
    print '>>> DL End processing first level work..All Entry Count: %d',len(list_data)
    list_data2=[]
    print '>>> DL Start processing Second level work..'
    #Validate..
    if not(s_c_selector and s_data):
      print '>>> Error , we must have s_c_selector and s_data for second level processing'
      return
    for d in list_data:
      if not d.has_key('url'):
        print '>>> ERROR : URL noy found for second level...sol: f_c_selctor must have {"url":"Something"}'
        continue;
      url =d['url']
      #Construct Abs Url
      if(url[0] == '/'):
        o = urlparse(b_url)
        url =  o.scheme+'://'+o.netloc +url
      # Now we have correct url
      html = self.getPage(url,validate=None)
      if not html: continue;
      self.buildSoup(html) 
      data = self.getSelectedDataInAContiner(s_c_selector,s_data)
      if dry_run : 
        print '>>> DRYRUN Number of Data in an entry Found is:',len(data)
        print '>>> DRYRUN Data Selected by %s is :'% s_c_selector
        for k,v in data[0].items():
          print '>>> DRYRUN %s ==> %s' %(k,v)
      if data==None: continue;
      #Inject url as a reference fuild
      for d in data:
        d['ref_url'] = url
      list_data2 += data 
      if dry_run : 
        print '>>> DRYRUN end for second level.'
        break ; # break the loop as it is a dry run.
      
    print '>>> DL Emd processing second level work..'
    print '>>> Total data count',len(list_data2)
    
    #Saving the data using pickle..
    if save_name:
      print '>>> DL Saving in a file..'
      import pickle
      f = open(save_name,'wb')
      pickle.dump(list_data2,f)
      f.close()
      
    

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
s.TwoLevelDataRetrival(url="http://www.careercup.com/page?&sort=comments&n=1",f_c_selctor="#question_preview .question",f_data={'url':('.entry a','link','first'),'rating':('.commentCount','text','first')},s_c_selector="#mainpagebody",s_data={'q':('.question .entry a','text','first'),'a':('.commentBody','text','first')}, n_url="http://www.careercup.com/page?&sort=comments&n=1",dry_run=False,save_name="data.pkl",f_page_limit =10,f_entry_limit=100)
