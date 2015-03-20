###########################################
## Author : Dipankar Dutta
## Title :
## Description:
## Function: Contains XHR Request handlers- hence it;s a Ajax Request Handlers
###########################################
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CommonLib import utils
from django.shortcuts import render, render_to_response
from bs4 import BeautifulSoup

import logging
logger = logging.getLogger('testlogger')
logger.info('This is a simple log message')

######################3  Start Feedback Operation using Ajax #########################
from .api import FeedbackManager
@csrf_exempt
def ajax_feedback(request):
    import pdb
    #pdb.set_trace()
    res=None
    if request.method == 'GET':
        page=request.GET.get('page',None)
        limit=request.GET.get('limit',None)

        name=request.GET.get('name',None)
        email=request.GET.get('email',None)
        mobile=request.GET.get('mobile',None)
        res=FeedbackManager.getAllFeedbackWithFilter(name=name, email=email,mobile=mobile,page=page,limit=limit)

    elif request.method == 'POST':
        name=request.POST.get('name',None)
        email=request.POST.get('email',None)
        mobile=request.POST.get('mobile',None)
        feedback=request.POST.get('feedback',None)
        ipaddress  = utils.get_client_ip(request)
        res=FeedbackManager.createFeedback(name=name,email=email,mobile=mobile,feedback=feedback,ipaddress = ipaddress )
    elif request.method ==  'DELETE':
        #Pass No Delete
        pass
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')

######################  End Address Operation ############################

###################### TODO Clean Code logic #########################
from AppsEngines.cleanCode.api import *
@csrf_exempt
def ajax_cleancode_compile(request):
    logger.info('Compilation Called....')
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('lang','c')
        name=request.POST.get('name',None)
        main=request.POST.get('main',None)
        func=request.POST.get('func',None)
        input=request.POST.get('input',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,main,func,input)
        #pdb.set_trace();
        ex.save(name,main,func,input)
        res = ex.compile(name)
        #ex.run(name)
        #ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def ajax_cleancode_run(request):
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('lang','c')
        name=request.POST.get('name',None)
        main=request.POST.get('main',None)
        func=request.POST.get('func',None)
        input=request.POST.get('input',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,main,func,input)
        res = ex.run(name)
        #ex.run(name)
        #ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def ajax_cleancode_perf(request):
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('lang','c')
        name=request.POST.get('name',None)
        main=request.POST.get('main',None)
        func=request.POST.get('func',None)
        input=request.POST.get('input',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,main,func,input)
        res = ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')

def remove_all_spl_char(s):
  return ''.join(e for e in s if e.isalnum()) 
    
@csrf_exempt
def download_file(request,id):
    res= {}
    if request.method == 'GET':
        res= CodeManager.getCode(id)        
        if res['res']:
          # Some Normalization ..
          if res['res']['language'] == None: res['res']['language']='C'
          res['res']['name']  = remove_all_spl_char(res['res']['name'])
          
          if res['res']['language'].lower() == 'py':
            file=''
            file +="\n'''\n"+"*"*50+"\n"+" Program Details " +"\n"+"*"*50
            file +="\n Name:"+res['res']['name']
            file +="\n Description:"+res['res']['short_desc']+"\n"+"*"*50+"\n'''\n"
            if res['res']['main']:
              file +="\n#"+"*"*50+"\n"+"Driver Code "+"\n"+"*"*50+"#\n"
              file +=res['res']['main']
            if res['res']['func']:
              file +="\n#"+"*"*50+"\n"+"Function Code "+"\n"+"*"*50+"#\n"
              file +=res['res']['func']
          else:
            file=''
            file +="\n/*"+"*"*50+"\n"+" Program Details " +"\n"+"*"*50
            file +="\n Name:"+res['res']['name']
            file +="\n Description:"+res['res']['short_desc']+"\n"+"*"*50+"*/\n"
            if res['res']['main']:
              file +="\n/*"+"*"*50+"\n"+"Driver Code "+"\n"+"*"*50+"*/\n"
              file +=res['res']['main']
            if res['res']['func']:
              file +="\n/*"+"*"*50+"\n"+"Function Code "+"\n"+"*"*50+"*/\n"
              file +=res['res']['func']
          
          from django.core.servers.basehttp import FileWrapper
          # generate the file
          if res['res']['language'] =='C':
            response = HttpResponse(file, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=%s.c' %(res['res']['name'])
          
          response['Content-Length'] = len(file)
          return response           
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def view_book(request):
    res= {}
    if request.method == 'GET':
        passwd = request.GET.get('pass',None)
        if passwd != 'ThanksDipankar':
           return HttpResponse(json.dumps({'error':'Opps.. You dont have the requited permission, wait till release :)'},default=json_util.default),content_type = 'application/json')
        res= CodeManager.searchCode(limit=20,mv=['id','name','short_desc','full_desc','main','solution','topic'])       
        #pdb.set_trace() 
        if res['res']:
          return render_to_response('cleanCode_book.html',res['res']);          
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')

@csrf_exempt
def view_file(request,id):
    res= {}
    if request.method == 'GET':
        
        res= CodeManager.getCode(id)
        if res['res']:
          return render_to_response('cleanCode_view.html',res['res']);
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def edit_file(request,id):
    res= {}
    if request.method == 'GET':        
        res= CodeManager.getCode(id)
        if res['res']:
          return render_to_response('cleanCode_editor.html',res['res']);
        else:
          data={'id':0,'main':'//write your main code here','func':'//your helper func','name':'sample','short_desc':'sample prog'}
          return render_to_response('cleanCode_editor.html',data);

# Interactive View 
@csrf_exempt
def iview_file(request,id):
    res= {}
    if request.method == 'GET':
        
        res= CodeManager.getCode(id)
        if res['res']:
          return render_to_response('cleanCode_iview.html',res['res']);
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
          
###### Helper Function ##########
def htmlToText(html):
  " HTML to Text converted"
  
def textToHTML(html):
  " text to html coverter"
########### END ############


#Save as Combine data
@csrf_exempt 
def iview_file_save(request,id):
    res= {}
    if request.method == 'GET':
        """ DATABASE ->  splitData(p,a,l)(this is proper html format) -> DeNorm from TextArea -> Merege All ->return FullArea """
        res= CodeManager.getCode(id)
        if res['res']:          
          p = res['res']['full_desc']
          a= res['res']['intro']
          l = res['res']['solution']
          
          # Construct COMBINE : SPLIT HTML - ONE TEXT
          try:
            out =''                 
            soup = BeautifulSoup(p)
            out += 'P:'+str(soup.p)[3:-4]
            soup = BeautifulSoup(a)
            out += '\nA:'+str(soup.p)[3:-4]
            soup = BeautifulSoup(l)
            out += ''.join([ '\nL#%s:%s'%(p,q)  for (p,q) in [ (i.attrs['target'], str(i.p)[3:-4]) for i in soup.find_all('div')] ])
          except:
            print 'error: Not able to Construct COMBINE : HTML - ONE TEXT '
            out={'combine':'P: problem\nA: Algorithms\nL#1-12: line 1 to 12\nL#13-14: 14 to 15\n'}         
          res={'combine':out}          
        else:
          res={'combine':'P: problem\nA: Algorithms\nL#1-12: line 1 to 12\nL#13-14: 14 to 15\n'}
        return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
    if request.method == 'POST':
        """ textarea input ->Split(p,a,l)-> Normalized each one HTML -> StoreInDatabase """
        combine = request.POST.get('combine',None)   
        
        # Construct COMBINE : ONE TEXT  --> SPLIT HTML        
        try:
          #pdb.set_trace()
          sp = combine.find('P:')
          sa = combine.find('\nA:')         
          sl = combine.find('\nL#')
          if sa != -1:
            p = combine[sp+2:sa]
          elif sl != -1:
            p = combine[sp+2:sl]
          else:
            p = combine[sp+2:]         
          #p = '<pre>'+p+'</pre>'
          if combine.find('\nA:') != -1:
            combine = combine[combine.find('\nA:')+3:]
          if sl != -1:
            a = combine[:combine.find('\nL#')]
          else:
            a = combine[:]
          #a = '<pre>'+a+'</pre>'
          if combine.find('\nA:') != -1:
            combine = combine[combine.find('\nL#')+3:]
          else:
            combine =''
            
          exp =''
          if combine.strip():
            try:
              exp = ''.join(['<div class="iview codeExp" target="%s">%s</div>'%(i,j) for (i,j) in [ c.split(':') for c in combine.strip().split('\nL#')]])
            except:
              res= {'status':'error','msg':'Error: Wring format ','sys_error':'use => "L#1-2,3: this is this'}
              return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
          res= CodeManager.updateCode(id,full_desc=p,intro=a,solution=exp)
        except Exception,e:
          print 'Error: failed Construct COMBINE : ONE TEXT  -->  SPLIT HTML '
          res={'status':'error','msg':'Error: failed Construct COMBINE : ONE TEXT  -->  SPLIT HTML ','sys_error':str(e)}
        
        return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
         
######################  End Address Operation ############################


