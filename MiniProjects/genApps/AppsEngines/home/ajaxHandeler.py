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
from CommonLib import utils,YouTube
from CommonLib.SmartText import smartTextToHtml
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
        lang=request.POST.get('language','c')
        name=request.POST.get('name',None)
        main=request.POST.get('main',None)
        func=request.POST.get('func',None)
        input=request.POST.get('input',None)
        depends=request.POST.get('depends',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,main,func,input,depends)
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
        lang=request.POST.get('language','c')
        name=request.POST.get('name',None)
        main=request.POST.get('main',None)
        func=request.POST.get('func',None)
        input=request.POST.get('input',None)
        depends=request.POST.get('depends',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,main,func,input,depends)
        res = ex.run(name)
        #ex.run(name)
        #ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def ajax_cleancode_perf(request):
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('language','c')
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
          if res['res']['language'] == None: res['res']['language']='c'
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
          if res['res']['language'] =='c':
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
def get_stat(request):
    res= {}
    if request.method == 'GET':
      from AppsEngines.cleanCode.models import Code
      res['total']= Code.objects.filter().count()
      res['stat_code_complete'] = res['total'] - Code.objects.filter(main=None).count()
      res['stat_intro_complete'] = res['total'] -(Code.objects.filter(solution=None).count()+Code.objects.filter(solution='').count()	+ Code.objects.filter(solution='Explane the code with comaplexity').count() ) 
      res['total']= Code.objects.filter().count()
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
def edit_file(request,id=None):
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
  
def getHtmlContent(a):
  " <div> hello1 <b>hello2</b></div> => Just remove first and last tag"
  try:
    return a[a.index('>')+1:a.rindex('</')]
  except: 
    return a

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
            #pdb.set_trace()
            out =''                 
            soup = BeautifulSoup(p)
            out += ''.join([ '\nP:%s'%p  for p in [ getHtmlContent(str(i)) for i in soup.find_all('div')] ])
            out =out[1:] # Remove first \n
            soup = BeautifulSoup(a)
            out += ''.join([ '\nA:%s'%p  for p in [ getHtmlContent(str(i)) for i in soup.find_all('div')] ])
            soup = BeautifulSoup(l)
            out += ''.join([ '\nL#%s:%s'%(p,q)  for (p,q) in [ (i.attrs['target'], getHtmlContent(str(i))) for i in soup.find_all('div')] ])
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
    if combine: combine = '\n'+combine
    sec_count = combine.count("\nP:")+combine.count("\nA:")+combine.count("\nL#");
    # Construct COMBINE : ONE TEXT  --> SPLIT HTML        
    try:
      #pdb.set_trace()
      sp = combine.find('\nP:')
      sa = combine.find('\nA:')         
      sl = combine.find('\nL#')
      if sa != -1:
        p = combine[sp+3:sa]
      elif sl != -1:
        p = combine[sp+3:sl]
      else:
        p = combine[sp+3:]       
      # Now we have the p
      try:
        if p.strip():
          p = ''.join(['<div class="iview">%s</div>'%i for i in p.split('\nP:')])
      except Exception, e:
        res= {'status':'error','msg':'Error: Wring format ','sys_error':'use => Some problem of getting all P('+e+')'}
        return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')		  

      if combine.find('\nA:') != -1:
        combine = combine[combine.find('\nA:')+3:]
      if sl != -1:
        a = combine[:combine.find('\nL#')]
      else:
        a = combine[:]
      #Now we have the a:
      try:
        if a.strip():
          a = ''.join(['<div class="iview">%s</div>'%i for i in a.split('\nA:')])
      except Exception, e:
        res= {'status':'error','msg':'Error: Wring format ','sys_error':'use => Some problem of getting all A:('+e+')'}
        return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
      if combine.find('\nL#') != -1:
        combine = combine[combine.find('\nL#')+3:]
      else:
        combine =''
            
      exp =''
      if combine.strip():
        try:
          #pdb.set_trace()
          exp = ''.join(['<div class="iview codeExp" target="%s">%s</div>'%(i,j) for (i,j) in [ (c[:c.index(':')],c[c.index(':')+1:]) for c in combine.strip().split('\nL#')]])
        except Exception, e:
          res= {'status':'error','msg':'Error: Wring format ','sys_error':'use => "L#1-2,3: this is this('+e+')'}
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
      #Now Update..
      res= CodeManager.updateCode(id,full_desc=p,intro=a,solution=exp)
    except Exception,e:
      print 'Error: failed Construct COMBINE : ONE TEXT  -->  SPLIT HTML '
      res={'status':'error','msg':'Error: failed Construct COMBINE : ONE TEXT  -->  SPLIT HTML ','sys_error':str(e)}
    # Make a validation of Update"
    r = res['res']
    pdb.set_trace()
    if(sec_count == (r['full_desc'].count('iview')+r['intro'].count('iview')+r['solution'].count('iview'))):
      return HttpResponse(json.dumps({'status':'success','msg':'Total section successfully: '+str(sec_count)},default=json_util.default),content_type = 'application/json')
    else:
      return HttpResponse(json.dumps({'status':'error','msg':'validation failed: section count doesnt match..'},default=json_util.default),content_type = 'application/json')
    
######################  End Address Operation ############################

####################### Start LOOK Views #################################
# Interactive View 
@csrf_exempt
def look(request,id):
    res= {}
    if request.method == 'GET':        
        res= CodeManager.getCode(id)
        if res['res']:
          #pdb.set_trace()
          res['res']['solution'] = smartTextToHtml(res['res']['solution'],{'MAIN_CODE':res['res']['main']})
          return render_to_response('cleanCode_look.html',res['res']);
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
################################  END LOOK #################################


#####################  YoutUbe related Stuff ##############################

# Interactive View 
@csrf_exempt
def ajax_youtube(request):
    res= {}
    if request.method == 'GET':
        url = request.GET.get('url',None)
        res= YouTube.getYoutubeData(url)
        return render_to_response('youtube.html',res);
    else:
          return HttpResponse(json.dumps({'res':'Not Suppored;'},default=json_util.default),content_type = 'application/json')