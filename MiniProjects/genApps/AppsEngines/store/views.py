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
