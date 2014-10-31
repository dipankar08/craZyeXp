"""
Created on Aug 2, 2014

@author: Dipankar

The Rule of XML
1. properties should be like : dict([ x.split('=') for x in a.split(',')])
"""

import pdb
import codegen
from xml.dom import minidom

print '*'*40
print 'Welcome to XML2DJ Code Generation '
print '-'*40
print 'This will take xml file and generate the Django APPS simply in one click.'
print 'Please Write the <project.xml> eg Student.xml .'
print 'output: It will generate the Student/<py files> '
print 'How to run : <python XML2DJ.py Student.xml >'
print '*'*40
# helper
def genStr(template,mylist,sep=';'):
    ans = ''
    for i in mylist:
        ans += template.format(x=i) + sep
    return ans
def genStr2(template,mylist,sep=';'):
    ans = ''
    for (i,j) in mylist:
        ans += template.format(x=i,y=j) + sep
    return ans
#print genStr("{x}=request.POST.get('{x}',None)",['a','b','c']);


print '[GEN] Code Generation started'

ms = codegen.CodeGenerator()
aps = codegen.CodeGenerator()
ajs = codegen.CodeGenerator()
us = codegen.CodeGenerator()
hs = codegen.CodeGenerator()

ms += """
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField
"""

aps += """
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
"""

ajs += """
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
"""
ajs *= """
#Helper function
def AutoHttpResponse(code=200,res=None):
  if res and isinstance(res, dict):
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
  if code == 400:  
    res = {'res':None,'status':'error','msg':'400(Bad Request): '+str(res)} if res else {'res':None,'status':'error','msg':'400(Bad Request): required /invalid Paranmeter passed.'}
  if code == 501:  
    res = {'res':None,'status':'error','msg':'501(Not Implemented): '+str(res)} if res else {'res':None,'status':'error','msg':'501(Not Implemented)'}
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json') 
  
"""

us += """
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)
"""
hs += """
"""
import sys
import os
FileName = sys.argv[1]
print 'We are parsing :', FileName
APP_NAME = FileName[:FileName.index('.')]
print 'Apps Name is  :', APP_NAME
os.mkdir(APP_NAME)
xmldoc = minidom.parse(FileName)
models = xmldoc.getElementsByTagName('model')

model_count =0
for model in models:
  #initialize model info ..
  arg = [] 
  field_list = [] # Similar as arg by list of touple [ ..(name.charType) ...]
  OneOrFrnKey = []
  Many2ManyKey = [] #[..(author,Author)..]
  log_history = track_update = False
  tag_ops =[] # [..(student,string)..]
  
  #process model ..
  model_count += 1
  mname = model.getAttribute('name')
  print '[GEN] Processing module'+mname
  ms += "class %s(models.Model):"%mname
  ms.indent()
  
  #process addon

  
  addon_list = model.getElementsByTagName('addon')
  for a in addon_list:
    if a.getAttribute('name') == 'log_history':
      log_history= True;
    elif a.getAttribute('name') == 'track_update':
      track_update= True;
    elif a.getAttribute('name') == 'tag_ops':
      tag_ops += a.getAttribute('onField').split(" ")  

  print tag_ops
  # process each field ..
  fields = model.getElementsByTagName('field')
  for f in fields:
    fname = f.getAttribute('name')
    prop = f.getAttribute('properties')
    ftype = f.getAttribute('type')
    if f.getAttribute('type')not in ['DictField', 'ListField']:
      ms += "%s = models.%s(%s)" % (f.getAttribute('name'), f.getAttribute('type'), f.getAttribute('properties'))
    else:
      ms += "%s = %s(%s)" % (f.getAttribute('name'), f.getAttribute('type'), f.getAttribute('properties'))

    if f.getAttribute('user_input') == 'yes':
      arg.append(fname)
      field_list.append((fname,ftype))
    elif f.getAttribute('user_input') == 'default':
      arg.append(fname)
      field_list.append((fname,ftype))

    if f.getAttribute('type') in ['ForeignKey','OneToOneField']:
      OneOrFrnKey.append((fname, f.getAttribute('ref')))
    elif f.getAttribute('type') in ['ManyToManyField']:
      Many2ManyKey.append((fname, f.getAttribute('ref')))
  
  #adding extra fuild based on addon
  if log_history:
    ms += "log_history = ListField(default=[{'type':'Unknown', 'msg':'Gods knows the event','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}],null=True,blank=True);"
  if track_update:
    ms += "created_at = models.DateTimeField(auto_now_add=True)"
    ms += "updated_at = models.DateTimeField(auto_now=True)"

  # Construct the Templetes Argumnets ..
  print '[GEN] user args are :'+str(arg)
  print '[GEN] user field_list are :',field_list
  MODEL_ARG = genStr("{x}",arg,',')# =>a,b,c,d
  MODEL_ARG_ARG = genStr("{x}={x}",arg,',') #=> a=a,b=b,c=c,
  MODEL_ARG_NON_NULL_UPDATE = genStr("t.{x} = {x} if {x} is not None else t.{x}",arg,';') 
  MODEL_ARG_GET =genStr("{x}=request.GET.get('{x}',None)",arg,';')
  MODEL_ARG_POST =genStr("{x}=request.POST.get('{x}',None)",arg,';')
  
  #QUERY_STR = genStr("t.{x} = {x} if {x} is not None else t.{x}",arg,';')
  #QUERY_STR = genStr("if {x} is not None: Query['{x}']={x}",arg,'\n      ')  
  QUERY_STR = ''
  #pdb.set_trace()
  for _f in field_list:
    if _f[1] == 'CharField':
      QUERY_STR += '\n      ' + "if {x} is not None: Query['{x}__contains']={x}".format(x=_f[0])
    else:
      QUERY_STR += '\n      ' + "if {x} is not None: Query['{x}']={x}".format(x=_f[0])
      
  #advance Serach Option.
  ADV_QUERY_STR = ''
  
   
  MODEL_FRN_KEY_LOOKUP =''
  MODEL_FRN_KEY_INFO = ''
  if OneOrFrnKey:
    MODEL_FRN_KEY_LOOKUP = genStr2("""
      {x}_res = {y}Manager.get{y}Obj(id={x})
      if {x}_res['res'] is None: return {x}_res
      {x} = {x}_res['res']""",OneOrFrnKey,'')
    MODEL_FRN_KEY_INFO = genStr2("res['{x}_desc'] = {y}Manager.get{y}(id=res['{x}'])['res']",OneOrFrnKey,';')
  
  LOG_HISTORY_CREATE = ''
  LOG_HISTORY_UPDATE = ''
  LOG_HISTORY_DELETE = ''
  if log_history:
    LOG_HISTORY_CREATE = "t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
    _CHANGE_MSG = genStr("changes +=str('update {x}:'+ str(t.{x}) +' to '+str( {x})+' ;')  if {x} is not None  else '' ",arg,';') 
    LOG_HISTORY_UPDATE = "changes='';"+_CHANGE_MSG+"t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
    LOG_HISTORY_DELETE = ''     

  #Makeing model methods
  ms.sp()
  ms.dedent()
  ms.sp()
  ms.sp()

  #Generating api.py
  aps*="""
from .models import {MODEL_NAME}
class {MODEL_NAME}Manager:
  @staticmethod
  def create{MODEL_NAME}({MODEL_ARG}): #Crete an Obj
    try:
      {MODEL_FRN_KEY_LOOKUP}
      t = {MODEL_NAME}({MODEL_ARG_ARG})
      {LOG_HISTORY_CREATE}
      t.save()
      return {{'res':model_to_dict(t),'status':'info','msg':'New {MODEL_NAME} got created.'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to create {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def get{MODEL_NAME}(id): # get Json
    try:
      t={MODEL_NAME}.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        {MODEL_FRN_KEY_INFO}
      return {{'res':res,'status':'info','msg':'{MODEL_NAME} returned'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not Able to retrive {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def get{MODEL_NAME}Obj(id): #get Obj
    try:
      t={MODEL_NAME}.objects.get(pk=id)
      return {{'res':t,'status':'info','msg':'{MODEL_NAME} Object returned'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to retrive object {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def update{MODEL_NAME}(id,{MODEL_ARG} ): #Update Obj
    try:
      res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
      if res['res'] is None: return res
      t=res['res']
      {LOG_HISTORY_UPDATE}
      {MODEL_ARG_NON_NULL_UPDATE}      
      t.save()
      return {{'res':model_to_dict(t),'status':'info','msg':'{MODEL_NAME} Updated'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to update {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def delete{MODEL_NAME}(id): #Delete Obj
    try:
      d={MODEL_NAME}.objects.get(pk=id)
      d.delete()
      return {{'res':d,'status':'info','msg':'one {MODEL_NAME} deleted!'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to delete {MODEL_NAME}!','sys_error':str(e)}}


  @staticmethod
  def search{MODEL_NAME}({MODEL_ARG}page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={{}}
      if id is not None: Query['id']=id
      {QUERY_STR} #if state is not None: Query['state_contains']=state
      d={MODEL_NAME}.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {{'res':res,'status':'info','msg':'{MODEL_NAME} search returned'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}!','sys_error':str(e)}}

  """.format(MODEL_NAME=mname,MODEL_ARG=MODEL_ARG,MODEL_ARG_ARG=MODEL_ARG_ARG,
              QUERY_STR=QUERY_STR,MODEL_ARG_NON_NULL_UPDATE=MODEL_ARG_NON_NULL_UPDATE,
              MODEL_FRN_KEY_LOOKUP=MODEL_FRN_KEY_LOOKUP,
              LOG_HISTORY_UPDATE=LOG_HISTORY_UPDATE,
              LOG_HISTORY_CREATE=LOG_HISTORY_CREATE,
              MODEL_FRN_KEY_INFO=MODEL_FRN_KEY_INFO)

  # Adding many to many Key in API
  for (field_name,ref_model) in Many2ManyKey:
      pass
      aps *= """
  @staticmethod
  def get{ref_model}(id):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.{field_name}.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} for the {MODEL_NAME} returned.'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to get {field_name} ','sys_error':str(e)}}

  @staticmethod
  def add{ref_model}(id,{field_name}_list):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if isinstance({field_name}_list,list):
         for i in {field_name}_list:
           # get the object..
           obj={ref_model}Manager.get{ref_model}Obj(i)['res']
           if obj is not None:
             t.{field_name}.add(obj)
             loc_msg+= str(obj.id)+','
       else:
         obj={ref_model}Manager.get{ref_model}Obj({field_name}_list)['res']
         if obj is not None:
            t.{field_name}.add(obj)
            loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.{field_name}.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got added!'}}
    except Exception,e :
       return {{'res':None,'status':'error','msg':'Not able to get {field_name} ','sys_error':str(e)}}

  @staticmethod
  def remove{ref_model}(id,{field_name}_list):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       if isinstance({field_name}_list,list):
         for i in {field_name}_list:
           # get the object..
           obj={ref_model}Manager.get{ref_model}Obj(i)['res']
           if obj is not None:
              t.{field_name}.remove(obj)
              loc_msg+= str(obj.id)+','
       else:
         obj={ref_model}Manager.get{ref_model}Obj({field_name}_list)['res']
         if obj is not None:
            t.{field_name}.remove(obj)
            loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.{field_name}.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got removed!'}}
    except Exception,e :
       return {{'res':None,'status':'error','msg':'Some {field_name} not able to removed! ','sys_error':str(e)}}

""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)


  #Adding Append/Remove/Search API on tags
  TAG_ARG_LIST = genStr("{x}=[]",tag_ops,',')# =>a=[],b=[],c=[],d=[]
  TAG_ARG_ARG = genStr("{x}={x}",tag_ops,',') #=> a=a,b=b,c=c,
  TAG_ARG_NON_NULL_APPEND = genStr("t.{x} = sorted(list(set(t.{x}+{x}))) if {x} is not None else t.{x}",tag_ops,';') 
  TAG_ARG_NON_NULL_REMOVE = genStr("t.{x} = sorted(list(set(t.{x})-set({x}))) if {x} is not None else t.{x}",tag_ops,';') 
  TAG_POST_GET_ARG= genStr("{x} = eval(request.POST.get('{x}','[]'))",tag_ops,';') 

  #TAG_QUERY_STR = genStr("\n      if {x}: Query['{x}__contains']= str(sorted({x}))[1:-1]",tag_ops,'') 
  TAG_QUERY_STR = genStr("\n      for x in {x}:Query['{x}__contains']= x",tag_ops,'') 
  

  for tags in tag_ops:
      aps *= """
  @staticmethod
  def appendList{MODEL_NAME}(id,{TAG_ARG_LIST}):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       {TAG_ARG_NON_NULL_APPEND}
       t.save()
       res= model_to_dict(t)
       return {{'res':res,'status':'info','msg':'tag added'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}}

  @staticmethod
  def removeList{MODEL_NAME}(id,{TAG_ARG_LIST}):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       {TAG_ARG_NON_NULL_REMOVE}
       t.save()
       res= model_to_dict(t)
       return {{'res':res,'status':'info','msg':'tag added'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}}
      
  @staticmethod
  def searchList{MODEL_NAME}({TAG_ARG_LIST}page=None,limit=None):
    try:
      Query={{}}
      {TAG_QUERY_STR} # Autogen
      d={MODEL_NAME}.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {{'res':res,'status':'info','msg':'{MODEL_NAME} search returned'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}!','sys_error':str(e)}}
  

""".format(MODEL_NAME=mname,
  TAG_ARG_LIST=TAG_ARG_LIST,
  TAG_ARG_NON_NULL_APPEND=TAG_ARG_NON_NULL_APPEND,
  TAG_ARG_NON_NULL_REMOVE=TAG_ARG_NON_NULL_REMOVE,
  TAG_QUERY_STR=TAG_QUERY_STR,
  ) 
  
  
  #########  Adding the Ajax Handaler ##########
  ajs*="""
from .api import {MODEL_NAME}Manager
@csrf_exempt
def ajax_{MODEL_NAME}(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    {MODEL_ARG_GET}
    # if Id is null, get the perticular {MODEL_NAME} or it's a search request
    if id is not None: 
      res= {MODEL_NAME}Manager.get{MODEL_NAME}(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= {MODEL_NAME}Manager.search{MODEL_NAME}({MODEL_ARG_ARG}id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    {MODEL_ARG_POST}
    # Update request if id is not null. 
    if id is not None: 
      res={MODEL_NAME}Manager.update{MODEL_NAME}(id=id,{MODEL_ARG_ARG})
    else:
      # This is new entry request...
      res={MODEL_NAME}Manager.create{MODEL_NAME}({MODEL_ARG_ARG})
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res ={MODEL_NAME}Manager.delete{MODEL_NAME}(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
""".format(MODEL_NAME=mname,MODEL_ARG=MODEL_ARG,MODEL_ARG_ARG=MODEL_ARG_ARG,
           MODEL_ARG_GET=MODEL_ARG_GET,MODEL_ARG_POST=MODEL_ARG_POST) 

  # Adding many to many Key in Ajax handaler
  for (field_name,ref_model) in Many2ManyKey:
      
      ajs *= """
@csrf_exempt
def ajax_{MODEL_NAME}_{ref_model}(request,id=None):
  res=None
  #If the request is coming for get to all {field_name}
  if request.method == 'GET':
      res= {MODEL_NAME}Manager.get{ref_model}(id=id)

  #This is the implementation for POST request to add or delete {field_name}
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    try:
      {field_name}_list=eval(request.POST.get('{field_name}_list',None))
    except:
      return AutoHttpResponse(400,'bad input for {field_name}_list')
    # Update request if id is not null.
    if action == 'ADD':
      res={MODEL_NAME}Manager.add{ref_model}(id=id,{field_name}_list = {field_name}_list)
    else:
      # do a delete action
      res={MODEL_NAME}Manager.remove{ref_model}(id=id,{field_name}_list = {field_name}_list)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')

""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)

  # 3.  For Tag Feature 
  if tag_ops:
      ajs *= """
@csrf_exempt
def ajax_{MODEL_NAME}_list(request,id=None,):
  res=None
  # This is basically a search by a tag or list items with given arguments
  if request.method == 'GET':
    return AutoHttpResponse(501)
  # This is basically a append to a list with given arguments
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if action not in ['APPEND', 'REMOVE', 'SEARCH'] : return AutoHttpResponse(400,'id missing ! your post data must have action = APPEND or REMOVE or SEARCH ?')     
    if not id and action != 'SEARCH' : return AutoHttpResponse(400,'id missing ! is your urls looks like http://192.168.56.101:7777/api/Author/1/list/ ?')   

    try:
      {TAG_POST_GET_ARG}
      if action == 'APPEND':
        res = {MODEL_NAME}Manager.appendList{MODEL_NAME}(id,{TAG_ARG_ARG})
      elif action == 'REMOVE':
        res = {MODEL_NAME}Manager.removeList{MODEL_NAME}(id,{TAG_ARG_ARG})
      elif action == 'SEARCH':
        res = {MODEL_NAME}Manager.searchList{MODEL_NAME}({TAG_ARG_ARG})
    except:
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
""".format(MODEL_NAME=mname,TAG_POST_GET_ARG=TAG_POST_GET_ARG,TAG_ARG_ARG=TAG_ARG_ARG)    

  # Generating urls.py 
  #1. Generating basic urls.....
  us*= """
urlpatterns += patterns('',
    # Read Operation
    (r'^api/{MODEL_NAME}/$',ajaxHandeler.ajax_{MODEL_NAME}),
    (r'^api/{MODEL_NAME}/(?P<id>\d+)/$',ajaxHandeler.ajax_{MODEL_NAME}),
    #(r'^{MODEL_NAME}/$',views.tt_home),
)
""".format(MODEL_NAME=mname)


  #2. Adding many to many Key in Ajax handaler
  for (field_name,ref_model) in Many2ManyKey:
      pass
      us*= """
urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/{MODEL_NAME}/(?P<id>\d+)/{ref_model}/$',ajaxHandeler.ajax_{MODEL_NAME}_{ref_model}),
)
""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)

  #3. For Tag addon 
  if tag_ops:
    us*= """
urlpatterns += patterns('',
    # Allowing adding and removing tags..
    (r'^api/{MODEL_NAME}/(?P<id>\d+)/list/$',ajaxHandeler.ajax_{MODEL_NAME}_list),
    (r'^api/{MODEL_NAME}/list/$',ajaxHandeler.ajax_{MODEL_NAME}_list),
)
""".format(MODEL_NAME=mname)

  #Generating the Help file
  hs*= """
  {model_count}. {MODEL_NAME} Func specifications
  ====================================
  {model_count}.1 Brief Description

  {model_count}.2 REST End point API specifications
     i) Creating a new {MODEL_NAME}
         HTTP: POST /api/{MODEL_NAME}/
         DATA: {MODEL_ARG_ARG}

    ii) Update a exiting {MODEL_NAME} info
         HTTP: POST /api/{MODEL_NAME}/1/
         DATA: {MODEL_ARG_ARG}

   iii) Getting an {MODEL_NAME} info
         HTTP: GET /api/{MODEL_NAME}/1/

    iv) Getting All {MODEL_NAME} info
         HTTP: GET /api/{MODEL_NAME}/
         DATA: {MODEL_ARG_ARG}

     v) search  All {MODEL_NAME} info
         HTTP: GET /api/{MODEL_NAME}/
         DATA: {MODEL_ARG_ARG}

    vi) Search using pagination of {MODEL_NAME} data
         HTTP: GET /api/{MODEL_NAME}/
         DATA: {MODEL_ARG_ARG}

  """.format(MODEL_NAME=mname,MODEL_ARG=MODEL_ARG,MODEL_ARG_ARG=MODEL_ARG_ARG,
           MODEL_ARG_GET=MODEL_ARG_GET,model_count=model_count)
           
  #Help String for Many2ManyKey
  for (field_name,ref_model) in Many2ManyKey:
      pass
      hs*= """
    vii) Getting all {ref_model} for a {MODEL_NAME}
         HTTP: GET /api/{MODEL_NAME}/1/{ref_model}/

   viii) Adding more {ref_model} for a {MODEL_NAME}
         HTTP: POST /api/{MODEL_NAME}/1/{ref_model}/
         DATA: action=ADD&{field_name}_list=[1,2,3]

     ix) Removing more {ref_model} for a {MODEL_NAME}
         HTTP: POST /api/{MODEL_NAME}/1/{ref_model}/
         DATA: action=DEL&{field_name}_list=[1,2,3]

""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)

  #Help String for Tags
  if tag_ops:
      pass
      hs*= """
    x) Append a tags on a list 
         HTTP: POST : http://192.168.56.101:7777/api/Author/3/list/
         DATA : name=dipankar12322333&reg=1&tag1=%5B3%2C4%5D&action=APPEND

   xi) Remove a tags on a list 
         HTTP: POST : http://192.168.56.101:7777/api/Author/3/list/
         DATA : name=dipankar12322333&reg=1&tag1=%5B3%2C4%5D&action=REMOVE

   xii) Serach a tags on a list 
         HTTP: POST : http://192.168.56.101:7777/api/Author/3/list/
         DATA : name=dipankar12322333&reg=1&tag1=%5B3%2C4%5D&action=SEARCH

""".format(MODEL_NAME=mname)

  # End of Processing this model table.
print '[GEN] Code Gen complete.'
print '[GEN] Writing into files'
mf = open(APP_NAME+'/models.py','w+');mf.write(str(ms));mf.close()
apf = open(APP_NAME+'/api.py','w+');apf.write(str(aps));apf.close()
ajf = open(APP_NAME+'/ajaxHandeler.py','w+');ajf.write(str(ajs));ajf.close()
uf = open(APP_NAME+'/mapping.py','w+');uf.write(str(us));uf.close()
uf = open(APP_NAME+'/__init__.py','w+');uf.write("#Simple Init file");uf.close()
hf = open(APP_NAME+'/help.txt','w+');hf.write(str(hs));hf.close()
