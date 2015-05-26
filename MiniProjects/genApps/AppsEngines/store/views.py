from django.shortcuts import render, render_to_response
import pdb
import os
from django.template import RequestContext
def looksGood(a):
   x= """
   <div style="
    background: yellow none repeat scroll 0 0;
    border: 2px dashed red;
    color: red;
    margin: 100px auto;
    padding: 20px;
    text-align: center;
    width: 500px;
" >
    %s
    <br><br><br>
    - Do you know about God ?
     -Dipankar
   </div>
   """%a
   return x
def getGlobalPath():
    path1 = os.path.dirname(os.path.abspath(__file__))
    path1 = os.path.join(path1, 'data')
    return path1+'/'
def store_home(request,uid=None):
    return render_to_response('store_home.html');
def myfiles_page(request,path=None):
    pdb.set_trace()
    path1 = getGlobalPath()
    if not path1:
      path1 = os.path.join(path1, path)
    os.chdir(path1)
    x = 0
    d = {}
    for file in os.listdir("."):
        d[x] = (path + file)
        x = x + 1

    variables = RequestContext(request, {
    'user' : request.user,
    'filedict' : d,
    })
    return render_to_response('myfiles_page.html', variables)
from django.http import HttpResponse
def downloadFile(request,path=''):
  "Downlaoding any file with relative path.."
  full_path =  getGlobalPath()+path
  if not os.path.isfile(full_path) :
    return HttpResponse(looksGood(full_path +' Seems to be not exist or not a file !'))
  try:
    x = file(full_path)
    return HttpResponse(x.read(),content_type='application/force-download')
  except:
    return HttpResponse(looksGood('Erro: Not able to read that file'))
    
import urllib2
def downLoadFromNet(url,path):
  pdb.set_trace()
  import requests
  import shutil
  import os
  r = requests.get(url, stream=True)
  if r.status_code == 200:
      size =  r.headers.get('content-length')
      ftype =  r.headers.get('content-type')
      url = r.url
      fname = url[url.rfind('/')+1:]
      local_path = getGlobalPath()+path+fname
      directory = os.path.dirname(local_path)
      if not os.path.exists(directory):
         os.makedirs(directory)
      with open(local_path, 'wb') as f:
          r.raw.decode_content = True
          shutil.copyfileobj(r.raw, f)      
def uploadViaUrl(request,path=''):
  """ We Support Update file by URL 
  1. http://192.168.56.101:7777/store/upload/?path=abc/hef/&isUrl=True&url=http://google.com/
  """
  isUrl = request.GET.get('isUrl')
  pdb.set_trace()
  if isUrl:
    print 'isUrl'
    url = request.GET.get('url')
    path = request.GET.get('path')
    downLoadFromNet(url,path)
  else:
    print ' not isUrl'
    for filename, file in request.FILES.iteritems():
      name = request.FILES[filename].name
      print name
  return HttpResponse(looksGood('This Feature is not yet implemnetd'))
