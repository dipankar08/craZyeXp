#!/usr/bin/python
"""
Created on Aug 2, 2014

@author: Dipankar

The Rule of XML
1. properties should be like : dict([ x.split('=') for x in a.split(',')])

Notes:
FRn and One2One Faluid can be added or update by normal update method
M2M can be added /removed from separete method, Shoud be implmeted in both Manager( reverse)
One2One getter Must be Avalbe in Both manger
FRN Reverse Manger can have get or Serach on list 
not allowing add./delete M2M relation while crete or update . note that They Must be  a separte Query,.
"""

import pdb
import codegen
from xml.dom import minidom
import time
import shutil
print '*'*40
print 'Welcome to XML2DJ Code Generation '
print '-'*40
time.sleep(1);
print 'This will take xml file and generate the Django APPS simply in one click.'
print 'Please Write the <project.xml> eg Student.xml .'
print 'output: It will generate the Student/<py files> '
print 'How to run : <python XML2DJ.py Student.xml >'
print '*'*40
##### helper #####
def getChildrenByTagName(node, tagName):
    if not node:return []
    return [ child  for child in node.childNodes if child.nodeType==child.ELEMENT_NODE and (tagName=='*' or child.tagName==tagName)]
        
            
def str2List(s):
  if not s: return []
  s = s.strip()
  try:
    if '[' in s:
      return eval(s)
    if ',' in s:
      return [ _i.strip() for _i in s.split(',') if _i]
    else:
      return [ _i for _i in s.split(' ') if _i ]
  except:
    D_LOG()
    print 'Error: eval Error: We support "[1,2,3]" or "aa,bb,cc" or "aa bb cc" to [1,2,3] Split Over , space or eval '
    return []
    
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


print '>>> Code Generation started'
print '    [PRE] Reading file ...'
import sys
import os
FileName = sys.argv[1]
print '    [PRE] We are parsing :', FileName
APP_NAME = FileName[:FileName.index('.')]
print '    [PRE] Apps Name is  :', APP_NAME
shutil.rmtree(APP_NAME)
os.mkdir(APP_NAME)
print '    [PRE] Folder ops Done....'

ms = codegen.CodeGenerator()
aps = codegen.CodeGenerator()
ajs = codegen.CodeGenerator()
us = codegen.CodeGenerator()
hs = codegen.CodeGenerator()
cc = codegen.CodeGenerator() # common.py

js = codegen.CodeGenerator() # sample.js
html = codegen.CodeGenerator() # sample.html


cc *="""
import sys, traceback
import os
import pdb

   
def D_LOG():
  
  print '_'*60  
  _, _, tb = sys.exc_info()
  filename, lineno, funname, line = traceback.extract_tb(tb)[-1]
  print "Exception in user code:",filename,':',lineno,')'
  print '-'*60
  os.system('sed -n '+str(lineno-5)+','+str(lineno+5)+'p '+filename)
  print '-'*60
  traceback.print_exc(file=sys.stdout)
  print '_'*60

  
def getCustomException(e,arg=''):
  msg = e.message
  if 'UNIQUE constraint failed' in e.message:
      msg=e.message.replace('UNIQUE constraint failed:','Please ensure following value must be unique:')
  elif 'NOT NULL constraint failed' in e.message:
      msg=e.message.replace('NOT NULL constraint failed:','Please ensure following field MUST have some value:')
  elif 'invalid literal for int() with base 10' in e.message:
      msg=e.message.replace('invalid literal for int() with base 10','Please ensure following value must be a integer:')
      
  #global error on Errro type
  elif isinstance(e,ValueError):
    msg='Type mismatch! You are trying to use wrong data type. Please enter valid '+e.message.split(' ')[0]+'.'
  elif e.__class__.__name__ == 'DoesNotExist':
    msg= 'The '+e.message.split(' ')[0]+' having id <'+str(arg)+'> Does not exist!'

  
  return msg
"""

ms += """
import pdb
from common import *
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField
"""

aps += """
import pdb
from common import *
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *
"""

ajs += """
import pdb
from common import *
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
"""

ajs *= """
#Helper function
def AutoHttpResponse(code=200,res=None):
  if res and isinstance(res, dict):
    return HttpResponse(json_util.json.dumps(res,default=json_util.default),content_type = 'application/json')
  if code == 400:  
    res = {'res':None,'status':'error','msg':'400(Bad Request): '+str(res)} if res else {'res':None,'status':'error','msg':'400(Bad Request): required /invalid Paranmeter passed.'}
  if code == 501:  
    res = {'res':None,'status':'error','msg':'501(Not Implemented): '+str(res)} if res else {'res':None,'status':'error','msg':'501(Not Implemented)'}
  return HttpResponse(json_util.json.dumps(res,default=json_util.default),content_type = 'application/json') 


# This is Customized Stringto List converter separted by space or comma. result remove empty string.
#We support "[1,2,3]" or 'aa,bb,cc' or 'aa bb cc' to [1,2,3] Split Over , space or eval 
#
def str2List(s):
  if not s: return []
  if isinstance(s, list): return s;
  s=str(s)
  s = s.strip()
  try:
    if '[' in s:
      return eval(s)
    if ',' in s:
      return [ _i.strip() for _i in s.split(',') if _i]
    else:
      return [ _i for _i in s.split(' ') if _i ]
  except:
    D_LOG()
    print 'Error: eval Error: We support "[1,2,3]" or "aa,bb,cc" or "aa bb cc" to [1,2,3] Split Over , space or eval '
    return []
  
#Helper Function To Perse Advance Serach parmas
#Input : <a:b:c> => (a,b,c) >
def parseTriple(s):
  if not s: # for null check..
    return s
  res = [None,None,None]
  s = s.split(':')
  if len(s) >= 3:
    s[0] = '|' if s[0].lower() == 'or' else '&'   
    res = s[:3]
  elif len(s) == 2:
    res = ['|'] + s
  elif len(s) ==1:
    res = ['|','exact']+s
  if len(res[0]) == 0 : res[0] ="|"
  if len(res[1]) == 0 : res[1] ="exact"
  # rule for in and not in
  if res[1] in ['in','notin']:
    res[2] =  str2List(res[2])  
  return res
  
"""

us += """
import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)
"""
hs += """
"""

js *= """
/*------------------------------------------------------------
sample.js
Author: Dipankar dutta
This is a auto-generated Js file, implements the following feature:
- create a app and controller to access the data
- acces the API usinh $http angular js Services

------------------------------------------------------------*/
/**** Create ****/ 

var myApp = angular.module("myApp", []);

/******* helper function *******/
myApp.filter('range', function() {
  return function(input, total) {
    total = parseInt(total);
    for (var i=0; i<total; i++)
      input.push(i);
    return input;
  };
});
/******* end of helper function *******/

"""

html *= """
<!--
sample.html
Author: Dipankar dutta
This is a auto-generated HTML file, implements the following feature:
- create a HTML form and Handaler using Angular Js.
-->
"""

html *= """
<html>
  <head> 
    <title> Sample test HTML code</title>
    <link rel="stylesheet" type="text/css" href="/media/css/concat.css">
    <script src="/media/js/jquery.min.js"></script>
    <script src="/media/js/angular.min.js"></script>
    <script src="/media/js/concat.js"></script>
    <script src="/media/js/{APP_NAME}.js"></script>
  </head>
  <style>
  </style>
  <body ng-app="myApp"> <!-- We have one module and Multile Controller -->
""".format(APP_NAME=APP_NAME)


js *= """

"""



# We have to amke two iteration of read to find out Forgain/onetoOne and manyToMany Dependency 
# ITR1: Resolve dependency
print '>>> First Scan for getting all model name....'
xmldoc = minidom.parse(FileName)
model_list =xmldoc.getElementsByTagName('model_list')[0]
models = getChildrenByTagName(model_list,'model')


# Initialized to resolve fwd dependency..
MAP_One2One={}
Rev_Many2ManyKey={}
MAP_Many2ManyKey={}
for model in models:
  mname = model.getAttribute('name') 
  MAP_One2One[mname] = [] # [ ... (fname,ref_model_name) ..], this can accessed directly Author a();a.toc ==something...
  MAP_Many2ManyKey[mname] = [] ## [ ... (fname,ref_model_name) ..], this can accessed directly by all() Author a();a.toc.all() /.add() like that 
  Rev_Many2ManyKey[mname] = [] # [ ... (fname,ref_model_name) ..] which bascially used by Author_set(...) 

# Let start again to solve loop depemdency.
print '>>> Second Scan for getting all model dependency....'
for model in models:
  mname = model.getAttribute('name') 
  MAP_One2One[mname] = [] # [ ... (fname,ref_model_name) ..], this can accessed directly Author a();a.toc ==something...
  MAP_Many2ManyKey[mname] = [] ## [ ... (fname,ref_model_name) ..], this can accessed directly by all() Author a();a.toc.all() /.add() like that 
  Rev_Many2ManyKey[mname] = [] # [ ... (fname,ref_model_name) ..] which bascially used by Author_set(...) method, also applicable for reverse forgain  key..
  fields = model.getElementsByTagName('field')
  for f in fields:
    ref = f.getAttribute('ref')
    ftype = f.getAttribute('type')
    fname = f.getAttribute('name')
    if ftype == 'ManyToManyField':
      MAP_Many2ManyKey[mname].append((fname,ref))
      Rev_Many2ManyKey[ref].append((mname.lower(),mname))    
    if ftype == 'ForeignKey':
      MAP_One2One[mname].append((fname,ref))
      Rev_Many2ManyKey[ref].append((mname.lower(),mname))    
    if ftype == 'OneToOneField':
      MAP_One2One[mname].append((fname,ref))
      MAP_One2One[ref].append((mname.lower(),mname))

################# Done ITR1 ####################
print '     MAP_One2One',MAP_One2One
print '     Rev_Many2ManyKey',Rev_Many2ManyKey
print '     MAP_Many2ManyKey',MAP_Many2ManyKey

#############  Introducing Global Add on #######
g_log_history = g_track_update = g_advance_serach = g_min_view = g_quick_search= False
g_tag_ops =[] # [..(student,string)..]

addon_list = getChildrenByTagName(getChildrenByTagName(model_list,'addon_list')[0],'addon')
for a in addon_list:
  if a.getAttribute('name') == 'log_history':
    g_log_history= True;
  elif a.getAttribute('name') == 'track_update':
    g_track_update= True;
  elif a.getAttribute('name') == 'tag_ops':
    g_tag_ops += a.getAttribute('onField').split(" ")  
  elif a.getAttribute('name') == 'advance_serach':
    g_advance_serach= True;
  elif a.getAttribute('name') == 'min_view':
    g_min_view= a.getAttribute('onField').split(" ")+['id'];
  elif a.getAttribute('name') == 'quick_search':
    g_quick_search= {'fld':a.getAttribute('onField'),'fil':a.getAttribute("filter")} #(field,filter)
####################[  End of gobal Addon]########

#############  Introducing Global page #######
PAGE_LIST =[] 
_page_list = getChildrenByTagName(getChildrenByTagName(model_list,'page_list')[0],'page')
for a in _page_list:
  page={}
  page['name'] =a.getAttribute('name')
  page['target'] =a.getAttribute('target')
  page['dependon'] =a.getAttribute('dependon')
  PAGE_LIST.append(page)  
print 'PAGE_LIST::::',PAGE_LIST

####################[  End of gobal Addon]########

#ITR3 : Third Iteration for all data gathering....
#Maps:
ftypeToptype={
  'CharField':'str',
  'IntegerField':'int',
  'DateTimeField':'date',
  'ListField':'str2List',
  'ManyToManyField':'int',
  'ForeignKey':'int',
  'DictField':'dict',
  'OneToOneField':'int',
}
print '>>> 3rd, will gather all info of model directory wise..'
ALL_XML_DATA_ONE_PLACE={}
ALL_XML_DATA_ONE_PLACE['model_list']={}
ALL_XML_DATA_ONE_PLACE['addon_list']={}


for model in models:
  mname = model.getAttribute('name')
  ALL_XML_DATA_ONE_PLACE['model_list'][mname]=[]  
  #################  Processing Filed. ##########################
  field_list_all = [] # Contain all data 
  #(fname,prop,ftype,ptype,htype,ref,choices,allow_user_input,default)
  #  0     1     2    3     4     5     6         7              8   <<< This ORDER MUST Be Maintained 
  Own_ForeignKey = []
  Own_OneToOneKey =[]
  Many2ManyKey = [] #[..(author,Author)..]  
  fields = model.getElementsByTagName('field')
  for f in fields:
    fname    = f.getAttribute('name')     
    prop     = f.getAttribute('properties')
    ftype    = f.getAttribute('type')
    ptype    = 'str'
    htype    = f.getAttribute('htype')
    ref      = f.getAttribute('ref')
    choices  = str2List(f.getAttribute('choices'))
    allow_user_input= f.getAttribute('allow_user_input')
    default = f.getAttribute('default') if f.getAttribute('default') else 'None'   
    #build Relationship...
    if ftype in ['ForeignKey']:
      Own_ForeignKey.append((fname, ref))
    elif ftype in ['OneToOneField']:
      Own_OneToOneKey.append((fname, ref))
    elif ftype in ['ManyToManyField']:
      Many2ManyKey.append((fname, ref))
    #Adding to all
    field_list_all.append((fname,prop,ftype,ptype,htype,ref,choices,allow_user_input,default))
    # loop end field
  ALL_XML_DATA_ONE_PLACE['model_list'][mname]=field_list_all
  #loop end model    
print '    [GEN] ALL_XML_DATA_ONE_PLACE :',ALL_XML_DATA_ONE_PLACE  

#################################################################################################
##
## how to use:
## 1. all model => ALL_XML_DATA_ONE_PLACE['model_list'].keys()
## 2. all filed name of a model: [ _i[0] for _i in ALL_XML_DATA_ONE_PLACE['model_list']['Author']]
## 3. all field details of model: ALL_XML_DATA_ONE_PLACE['model_list']['Author']
##
############### END Processing Filed. ###########################################################


#ITR4 : 4th Iteration for all code genaration : duplicate to be removed..TODO
print '>>> 4th Scan for code geneartion....'
print '\n>>> Model Generation is starting shortly..\n\n'
time.sleep(1);
model_count =0
for model in models:
  #initialize model info ..
  model_count += 1
  mname = model.getAttribute('name')
  print '    [GEN] Processing module'+mname
  
  ##############  process ADDON  ###########################
  ##########################################################  
  #1. Local Addon initialize by global addon but overwrite by local addon..
  log_history = g_log_history
  track_update = g_track_update
  advance_serach = g_advance_serach
  min_view = g_min_view 
  quick_search= g_quick_search
  tag_ops = g_tag_ops # [..(student,string)..]
  
  addon_list = getChildrenByTagName(getChildrenByTagName(model,'addon_list')[0],'addon')
  for a in addon_list:
    if a.getAttribute('name') == 'log_history':
      log_history= True;
    elif a.getAttribute('name') == 'track_update':
      track_update= True;
    elif a.getAttribute('name') == 'tag_ops':
      tag_ops = a.getAttribute('onField').split(" ")  # one tag ops supoted
    elif a.getAttribute('name') == 'advance_serach':
      advance_serach= True;
    elif a.getAttribute('name') == 'min_view':
      min_view= a.getAttribute('onField').split(" ")+['id'];
    elif a.getAttribute('name') == 'quick_search':
      quick_search= {'fld':a.getAttribute('onField'),'fil':a.getAttribute("filter")} #(field,filter)
  ####################[  End of Addon]###########################
  
  
  #################  Processing Filed. ##########################
  #Maps:
  ftypeToptype={
    'CharField':'str',
    'IntegerField':'int',
    'DateTimeField':'date',
    'ListField':'str2List',
    'ManyToManyField':'str2List',
    'ForeignKey':'int',
    'DictField':'dict',
    'OneToOneField':'int',
  }
  

  field_list_all = [] # Contain all data 
  #(fname,prop,ftype,ptype,htype,ref,choices,allow_user_input,default)
  #  0     1     2    3     4     5     6         7              8   <<< This ORDER MUST Be Maintained 
  Own_ForeignKey = []
  Own_OneToOneKey =[]
  Many2ManyKey = [] #[..(author,Author)..]
  
  fields = model.getElementsByTagName('field')
  for f in fields:
    fname    = f.getAttribute('name')     
    prop     = f.getAttribute('properties')
    ftype    = f.getAttribute('type')
    ptype    = 'str'
    htype    = f.getAttribute('htype')
    ref      = f.getAttribute('ref')
    choices  = f.getAttribute('choices')
    allow_user_input= f.getAttribute('allow_user_input')
    default = f.getAttribute('default') if f.getAttribute('default') else 'None'
    
    # collect all user input argumnets for other API implementations
    if ftypeToptype.has_key(ftype):
      ptype=ftypeToptype[ftype]
    else:
      raise Exception("ERROR: "+ftype+" is not yet supported !")
    
    # build Relationship...
    if ftype in ['ForeignKey']:
      Own_ForeignKey.append((fname, ref))
    elif ftype in ['OneToOneField']:
      Own_OneToOneKey.append((fname, ref))
    elif ftype in ['ManyToManyField']:
      Many2ManyKey.append((fname, ref))
    #Adding to all
    field_list_all.append((fname,prop,ftype,ptype,htype,ref,choices,allow_user_input,default))

  #get a Quick Lookup
  field_list_all_dict = {} # Contain all data 
  for _f in field_list_all:
      field_list_all_dict[_f[0]]=_f
      
  #initialize field info ..
  # arg: this bascially all input shoud be taken from user, passed to Ajax to API.
  arg = [ _f[0]  for _f in field_list_all if _f[7] != 'no']
  
  #field_list: Similar as arg by list of touple [ ..(name,filedtype,pythonEqType) ...]    
  field_list = [ (_f[0],_f[2],_f[3])  for _f in field_list_all if _f[7] != 'no'] 
  
  #arg_without_m2m: this is a collection , which can direct pass to Contractror of Djnago , m2m can't passed but they can be added by student.book_set.add(..) 
  arg_without_m2m =[ _f for _f in field_list_all if _f[2] != 'ManyToManyField']
  
  print '    [GEN] user args are :',arg
  print '    [GEN] user field_list are :',field_list
  print '    [GEN] user field_list_all are :',field_list_all
  #print '    [GEN] user field_list_all_dict are :',field_list_all_dict
  print '    [GEN] user arg_without_m2m are :',arg_without_m2m
  # Note : We need both field_list_all for maining teh order and field_list_all_dict for quick access..

  

   
  ############### END Processing Filed. ##########################
  
  
  
  ##################  Generating models.py #############################
  ######################################################################
  ms.sp()
  ms += "#*************Defining model for %s ***************" %mname
  ms += "class %s(models.Model):"%mname
  ms.indent()
  for _f in field_list_all:
    if _f[2] not in ['DictField', 'ListField']:
      ms += "%s = models.%s(%s)" % (_f[0], _f[2], _f[1])
    else:
      ms += "%s = %s(%s)" % (_f[0], _f[2], _f[1])
      
  #[ADDON]: Adding Extra Field based on addon
  if log_history:
    ms += "log_history = ListField(default=[{'type':'Unknown', 'msg':'Gods knows the event','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}],null=True,blank=True);"
  if track_update:
    ms += "created_at = models.DateTimeField(auto_now_add=True)"
    ms += "updated_at = models.DateTimeField(auto_now=True)"
    
  ms.sp()
  ms.dedent()

  ms += "\n#*************End Defining model for %s ************"%mname
  ms.sp()
  ##################  End Generating models.py #########################
  ######################################################################
  
  
  
  
  ##################  Build Templates ############################
  MODEL_ARG = genStr("{x[0]}={x[8]}",field_list_all,',')# =>a,b,c,d < We have Changed this to support default value.
  MODEL_ARG_ARG = genStr("{x}={x}",arg,',') #=> a=a,b=b,c=c,
  MODEL_ARG_ARG_CONS = genStr("{x[0]}={x[0]}",arg_without_m2m,',') #Similar as but doent include many2many as Django doent support this in constarctor.
  MODEL_ARG_NON_NULL_UPDATE = genStr("t.{x[0]} = {x[0]} if {x[0]} is not None else t.{x[0]}",arg_without_m2m,';') 
  MODEL_ARG_GET  = genStr("{x}= request.GET.get('{x}') if request.GET.get('{x}','').strip() else None",arg,';')
  MODEL_ARG_POPULATE_DEFAULT = genStr("{x[0]}={x[0]} if {x[0]} else {x[8]} ",[ _i for _i in field_list_all if _i[7] != 'no'] ,';')
  MODEL_ARG_POST = genStr("{x}= request.POST.get('{x}') if request.POST.get('{x}','').strip() else None",arg,';')
  # we have convert get of post String data to correct type. This processing shoudb be done in Ajax
  MODEL_ARG_NORM =''
  for _i in field_list:
    MODEL_ARG_NORM+= _i[0]+' = '+_i[2]+'('+_i[0]+') if( '+_i[0]+') else '+_i[0]+' ;'
  
  MODEL_ARG_VALIDATE =''
  for _i in field_list_all:
    _str =''
    if _i[6] and _i[3] =='str': # choice exist..
      _str = "if {x} and {x} not in {y} : return {{'res':None,'status':'error','msg':\"{x} must be either of {y} \",'sys_error':''}};\n      ".format( x= _i[0], y=str(str2List(_i[6])))
    elif _i[6] and _i[3] =='str2List': # choice exist..
      _str = "if {x} and not set({x}).issubset(set({y})) : return {{'res':None,'status':'error','msg':\"{x} must be either of {y} \",'sys_error':''}};\n      ".format( x= _i[0], y=str(str2List(_i[6])))
      MODEL_ARG_VALIDATE+= _str
    else:
      _str = "print \"[WARN] Ignoring validation check for {x}=>{y}\"\n      ".format( x= _i[0], y=str(str2List(_i[6])))


  
  QUERY_STR = ''
  for _f in field_list:
    if _f[1] == 'CharField':
      QUERY_STR += '\n      ' + "if {x} is not None: Query['{x}__contains']={x}".format(x=_f[0])
    else:
      QUERY_STR += '\n      ' + "if {x} is not None: Query['{x}']={x}".format(x=_f[0]) 
      
  #advance Serach Option.
  ADV_QUERY_STR = ''
  
   
  MODEL_FRN_KEY_LOOKUP =''
  MODEL_FRN_KEY_INFO = ''
  if Own_ForeignKey:
    MODEL_FRN_KEY_LOOKUP = genStr2("""
      {x}_res = {y}Manager.get{y}Obj(id={x})
      if {x}_res['res'] is None:
        {x}_res['help'] ='make sure you have a input called {x} in ur API or invalid {x} id.'
        return {x}_res
      {x} = {x}_res['res']""",Own_ForeignKey,'')
    MODEL_FRN_KEY_INFO = genStr2("res['{x}_desc'] = {y}Manager.get{y}(id=res['{x}'])['res']",Own_ForeignKey,';')
    
  MODEL_ONE2ONE_KEY_LOOKUP =''
  MODEL_ONE2ONE_KEY_INFO = ''
  if Own_OneToOneKey:
    MODEL_ONE2ONE_KEY_LOOKUP = genStr2("""
      if {x}:
        {x}_res = {y}Manager.get{y}Obj(id={x})
        if {x}_res['res'] is None:
          {x}_res['help'] ='invalid {x} id; any way this is optional..'
          return {x}_res
        {x} = {x}_res['res']""",Own_OneToOneKey,'')
    MODEL_ONE2ONE_KEY_INFO = genStr2("res['{x}_desc'] = {y}Manager.get{y}(id=res['{x}'])['res']",Own_OneToOneKey,';')
  
  LOG_HISTORY_CREATE = ''
  LOG_HISTORY_UPDATE = ''
  LOG_HISTORY_DELETE = ''
  if log_history:
    LOG_HISTORY_CREATE = "t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
    _CHANGE_MSG = genStr("changes += '< {x[0]}:'+ str(t.{x[0]}) +' -> '+str( {x[0]})+' >'  if {x[0]} is not None  else '' ",arg_without_m2m,'\n      ') 
    LOG_HISTORY_UPDATE = "changes='';\n      "+_CHANGE_MSG+"if changes: t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
    LOG_HISTORY_DELETE = ''
  
  ADD_MANY2MANY_WHEN_CREATE =genStr("if {x[0]}: "+mname+"Manager.add"+mname +"_{x[1]}(t.id,{x[0]},flush=True);",Many2ManyKey,"\n      ")
  ##################  END Build Templates ##########################
  


  ##################  Generating api.py ################################
  ######################################################################
  
  #1. Generate basic API's
  aps*="""
from .models import {MODEL_NAME}
class {MODEL_NAME}Manager:
  @staticmethod
  def create{MODEL_NAME}({MODEL_ARG}): #Crete an Obj
    try:
      {MODEL_ARG_VALIDATE}
      {MODEL_FRN_KEY_LOOKUP}
      {MODEL_ONE2ONE_KEY_LOOKUP}
      t = {MODEL_NAME}({MODEL_ARG_ARG_CONS})
      {LOG_HISTORY_CREATE}
      t.save()
      {ADD_MANY2MANY_WHEN_CREATE}
      return {{'res':model_to_dict(t),'status':'info','msg':'New {MODEL_NAME} got created.'}}    
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to create {MODEL_NAME}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def get{MODEL_NAME}(id): # get Json
    try:
      t={MODEL_NAME}.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        {MODEL_FRN_KEY_INFO}
        {MODEL_ONE2ONE_KEY_INFO}
      return {{'res':res,'status':'info','msg':'{MODEL_NAME} returned'}}
   
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not Able to retrive {MODEL_NAME}:'+getCustomException(e,id),'sys_error':str(e)}}

  @staticmethod
  def get{MODEL_NAME}Obj(id): #get Obj
    try:
      t={MODEL_NAME}.objects.get(pk=id)
      return {{'res':t,'status':'info','msg':'{MODEL_NAME} Object returned'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to retrieve object {MODEL_NAME}:'+getCustomException(e,id),'sys_error':str(e)}}

  @staticmethod
  def update{MODEL_NAME}(id,{MODEL_ARG} ): #Update Obj
    try:
      res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
      if res['res'] is None: return res
      t=res['res']
      {MODEL_ARG_VALIDATE}
      {LOG_HISTORY_UPDATE}
      {MODEL_FRN_KEY_LOOKUP}  
      {MODEL_ONE2ONE_KEY_LOOKUP}
      {MODEL_ARG_NON_NULL_UPDATE}             
      t.save()
      {ADD_MANY2MANY_WHEN_CREATE}
      return {{'res':model_to_dict(t),'status':'info','msg':'{MODEL_NAME} Updated'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to update {MODEL_NAME}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def delete{MODEL_NAME}(id): #Delete Obj
    try:
      d={MODEL_NAME}.objects.get(pk=id)
      d.delete()
      return {{'res':None,'status':'info','msg':'one {MODEL_NAME} deleted!'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to delete {MODEL_NAME}:'+getCustomException(e),'sys_error':str(e)}}


  @staticmethod
  def search{MODEL_NAME}({MODEL_ARG}page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={{}}
      if id is not None: Query['id']=id
      {QUERY_STR} #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include ={min_view}
      dd={MODEL_NAME}.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={{}}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {{'res':res,'status':'info','msg':'{MODEL_NAME} search returned'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}:'+getCustomException(e),'sys_error':str(e)}}

  """.format(MODEL_NAME=mname,MODEL_ARG=MODEL_ARG,MODEL_ARG_ARG=MODEL_ARG_ARG,
              QUERY_STR=QUERY_STR,MODEL_ARG_NON_NULL_UPDATE=MODEL_ARG_NON_NULL_UPDATE,
              MODEL_FRN_KEY_LOOKUP=MODEL_FRN_KEY_LOOKUP,
              MODEL_ONE2ONE_KEY_LOOKUP=MODEL_ONE2ONE_KEY_LOOKUP,
              LOG_HISTORY_UPDATE=LOG_HISTORY_UPDATE,
              LOG_HISTORY_CREATE=LOG_HISTORY_CREATE,
              MODEL_FRN_KEY_INFO=MODEL_FRN_KEY_INFO,
              MODEL_ARG_VALIDATE=MODEL_ARG_VALIDATE,
              MODEL_ARG_ARG_CONS=MODEL_ARG_ARG_CONS,
              ADD_MANY2MANY_WHEN_CREATE=ADD_MANY2MANY_WHEN_CREATE,
              MODEL_ONE2ONE_KEY_INFO=MODEL_ONE2ONE_KEY_INFO,min_view=min_view)

  #2A. Adding many to many Key in API <<< use author.all() >>>
  for (field_name,ref_model) in MAP_Many2ManyKey[mname]:
      pass
      aps *= """
  @staticmethod
  def get{MODEL_NAME}_{ref_model}(id):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.{field_name}.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} for the {MODEL_NAME} returned.'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to get {field_name}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def add{MODEL_NAME}_{ref_model}(id,{field_name},flush=False):
    assert (isinstance({field_name},list)),"{field_name} must be a list type."
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.{field_name}.clear()
       for i in {field_name}:
           # get the object..
           obj={ref_model}Manager.get{ref_model}Obj(i)['res']
           if obj is not None:
             t.{field_name}.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.{field_name}.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got added!'}}
    except Exception,e :
       D_LOG()
       return {{'res':None,'status':'error','msg':'Not able to get {field_name}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def remove{MODEL_NAME}_{ref_model}(id,{field_name}):
    assert (isinstance({field_name},list)),"{field_name} must be a list type."
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in {field_name}:
           # get the object..
           obj={ref_model}Manager.get{ref_model}Obj(i)['res']
           if obj is not None:
              t.{field_name}.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.{field_name}.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got removed!'}}
    except Exception,e :
       D_LOG()
       return {{'res':None,'status':'error','msg':'Some {field_name} not able to removed:'+getCustomException(e),'sys_error':str(e)}}

""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)

  #2B. Adding Reverse many2 many Key in API <<< use author_set.all() >>>
  for (field_name,ref_model) in Rev_Many2ManyKey[mname]:
      pass
      aps *= """
  @staticmethod
  def get{MODEL_NAME}_{ref_model}(id):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.{field_name}_set.all() ]
       return {{'res':res,'status':'info','msg':'all {field_name} for the {MODEL_NAME} returned.'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to get {ref_model}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def add{MODEL_NAME}_{ref_model}(id,{field_name},flush=False):
    assert (isinstance({field_name},list)),"{field_name} must be a list type."
    try:
      res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.{field_name}.clear()
      for i in {field_name}:
           # get the object..
           obj={ref_model}Manager.get{ref_model}Obj(i)['res']
           if obj is not None:
             t.{field_name}_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.{field_name}_set.all() ]
      return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got added!'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to get {field_name}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def remove{MODEL_NAME}_{ref_model}(id,{field_name}):
    assert (isinstance({field_name},list)),"{field_name} must be a list type."
    try:
      res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in {field_name}:
          # get the object..
          obj={ref_model}Manager.get{ref_model}Obj(i)['res']
          if obj is not None:
            t.{field_name}_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.{field_name}_set.all() ]
      return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got removed!'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Some {field_name} not able to removed:'+getCustomException(e),'sys_error':str(e)}}

""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)

  #2C. Adding MAP_One2One  in API <<< use author.name >>>
  for (field_name,ref_model) in MAP_One2One[mname]:
      pass
      aps *= """
  @staticmethod
  def get{MODEL_NAME}_{ref_model}(id):
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.{field_name})]
       return {{'res':res,'status':'info','msg':'all {field_name} for the {MODEL_NAME} returned.'}}  
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to get {field_name}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def add{MODEL_NAME}_{ref_model}(id,{field_name}):
    assert (isinstance({field_name},list)),"{field_name} must be a list type."
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in {field_name}:
           # get the object..
           obj={ref_model}Manager.get{ref_model}Obj(i)['res']
           if obj is not None:
             t.{field_name} = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.{field_name} )]
       return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got added!'}}
    except Exception,e :
       D_LOG()
       return {{'res':None,'status':'error','msg':'Not able to get {field_name}:'+getCustomException(e),'sys_error':str(e)}}

  @staticmethod
  def remove{MODEL_NAME}_{ref_model}(id,{field_name}):
    assert (isinstance({field_name},list)),"{field_name} must be a list type."
    try:
       res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.{field_name}=None # This is a single object..
       t.save()
       res= []
       return {{'res':res,'status':'info','msg':'all {field_name} having id <'+loc_msg+'> got removed!'}}
    except Exception,e :
       D_LOG()
       return {{'res':None,'status':'error','msg':'Some {field_name} not able to removed:'+getCustomException(e),'sys_error':str(e)}}

""".format(MODEL_NAME=mname,field_name=field_name,ref_model=ref_model)

  #Adding Append/Remove/Search API on tags
  TAG_ARG_LIST = genStr("{x}=[]",tag_ops,',')# =>a=[],b=[],c=[],d=[]
  TAG_ARG_ARG = genStr("{x}={x}",tag_ops,',') #=> a=a,b=b,c=c,
  TAG_ARG_NON_NULL_APPEND = genStr("t.{x} = sorted(list(set(t.{x}+{x}))) if {x} is not None else t.{x}",tag_ops,';') 
  TAG_ARG_NON_NULL_REMOVE = genStr("t.{x} = sorted(list(set(t.{x})-set({x}))) if {x} is not None else t.{x}",tag_ops,';') 
  TAG_POST_GET_ARG= genStr("{x} = eval(request.POST.get('{x}','[]'))",tag_ops,';') 


  TAG_QUERY_STR = genStr("\n      for x in {x}:Query['{x}__contains']= x",tag_ops,'') 
  
  #3. Adding Tags Related APIs
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
      D_LOG()
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
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}}
      
  @staticmethod
  def searchList{MODEL_NAME}({TAG_ARG_LIST}page=None,limit=None):
    try:
      Query={{}}
      {TAG_QUERY_STR} # Autogen
      include ={min_view}
      dd={MODEL_NAME}.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={{}}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {{'res':res,'status':'info','msg':'{MODEL_NAME} search returned'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}!','sys_error':str(e)}}
  

""".format(MODEL_NAME=mname,
  TAG_ARG_LIST=TAG_ARG_LIST,
  TAG_ARG_NON_NULL_APPEND=TAG_ARG_NON_NULL_APPEND,
  TAG_ARG_NON_NULL_REMOVE=TAG_ARG_NON_NULL_REMOVE,
  TAG_QUERY_STR=TAG_QUERY_STR,min_view=min_view
  ) 

  #3. Adding Advance Serach Related APIs
  ADV_QUERY_STR = genStr("\n      for x in {x}:Query['{x}__contains']= x",arg,'') 
  ADVSEARCH_POST_GET_ARG= genStr("{x} = parseTriple(request.POST.get('{x}',None))",arg,';') 
  ADVSEARCH_Q_QUERY_BUILDER =  genStr("\n      if {x}: Qstr += {x}[0]+' Q({x}__'+{x}[1]+'={x}[2]) '",arg,';') 
  #ADVSEARCH_Q_QUERY_BUILDER = ''
  
  
  if advance_serach:
      aps *= """
  #Advance search is Implemented here..
  @staticmethod
  def advSearch{MODEL_NAME}(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {{'res':None,'status':'error','msg':'{MODEL_NAME} Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}}
      if Qstr:
        dd={MODEL_NAME}.objects.filter(Qstr)
      else:
        dd={MODEL_NAME}.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include ={min_view}+['id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={{}}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {{'res':res,'status':'info','msg':'{MODEL_NAME} search returned'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}!','sys_error':str(e)}}
  

""".format(MODEL_NAME=mname,
  TAG_ARG_LIST=TAG_ARG_LIST,
  TAG_ARG_NON_NULL_APPEND=TAG_ARG_NON_NULL_APPEND,
  TAG_ARG_NON_NULL_REMOVE=TAG_ARG_NON_NULL_REMOVE,
  ADVSEARCH_Q_QUERY_BUILDER=ADVSEARCH_Q_QUERY_BUILDER,
  MODEL_ARG=MODEL_ARG,min_view=min_view
  )   

  #4. Addon: min_view
  if min_view:
      aps *= """
  #Advance search is Implemented here..
  @staticmethod
  def minView{MODEL_NAME}(page=None,limit=None):
    try:
      res =None
      include ={min_view}
      dd={MODEL_NAME}.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={{}}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {{'res':res,'status':'info','msg':'Mini View {MODEL_NAME}  returned'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}!','sys_error':str(e)}}
""".format(MODEL_NAME=mname, min_view=min_view  )   

  #4. Addon: quick_search
  if quick_search:
      aps *= """
  #Advance search is Implemented here..
  @staticmethod
  def get{MODEL_NAME}_quick_search(q,page=None,limit=None):
    try:
      res = None
      include =['id','{fld}']
      dd={MODEL_NAME}.objects.filter({fld}__{fil}=q).values(*include)
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page)      
      res = list(dd.object_list)
      if not res: return {{'res':res,'status':'info','msg':'Nothing match with your query'}} 
      return {{'res':res,'status':'success','msg':'{MODEL_NAME} match with your query'}}
    except Exception,e :
      D_LOG()
      return {{'res':None,'status':'error','msg':'Not able to search {MODEL_NAME}!','sys_error':str(e)}}
""".format(MODEL_NAME=mname,
  fld=quick_search['fld'],fil=quick_search['fil']
  )   
    
  ##################  Generating the AjaxHandaler.py file #########################
  #################################################################################
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
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      {MODEL_ARG_NORM}
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
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
    {MODEL_ARG_POPULATE_DEFAULT}    
    #data Must be Normalized to required DataType..
    try:
      {MODEL_ARG_NORM}      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
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
           MODEL_ARG_GET=MODEL_ARG_GET,MODEL_ARG_POST=MODEL_ARG_POST,MODEL_ARG_NORM = MODEL_ARG_NORM,
           MODEL_ARG_POPULATE_DEFAULT=MODEL_ARG_POPULATE_DEFAULT
           ) 

  #2A Adding many to many Key in Ajax handaler
  for (field_name,ref_model) in MAP_One2One[mname]+MAP_Many2ManyKey[mname]+Rev_Many2ManyKey[mname]:
    ajs *= """
@csrf_exempt
def ajax_{MODEL_NAME}_{ref_model}(request,id=None):
  res=None
  #If the request is coming for get to all {ref_model}_set
  if request.method == 'GET':
      res= {MODEL_NAME}Manager.get{MODEL_NAME}_{ref_model}(id=id)

  #This is the implementation for POST request to add or delete {ref_model}
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    {field_name}=str2List(request.POST.get('{field_name}',None))
    if not {field_name} : return AutoHttpResponse(400,'Missing/Bad input: <{field_name}: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res={MODEL_NAME}Manager.add{MODEL_NAME}_{ref_model}(id=id,{field_name} = {field_name})
    else:
      # do a delete action
      res={MODEL_NAME}Manager.remove{MODEL_NAME}_{ref_model}(id=id,{field_name} = {field_name})

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
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
""".format(MODEL_NAME=mname,TAG_POST_GET_ARG=TAG_POST_GET_ARG,TAG_ARG_ARG=TAG_ARG_ARG)  

  # 3.  For Advance Search Feature 
  if advance_serach:
      ajs *= """
#   query_str_builder() Will build query_str from triples
def query_str_builder(key,v):
  if v[1] in ['tagin', 'tagnotin']:
    v2 = str2List(v[2])
    if v2[0][0] != '-':
      _m = ' '+v[0]+'( Q('+key+'__contains = "'+v2[0]+'") ' # BUG ? if we have two tag c and ccc, then ?
    else:
      _m = ' '+v[0]+'( ~Q('+key+'__contains = "'+v2[0][1:]+'") '
    for L in v2[1:]:
      if L[0] != '-':
        _m += ' & Q('+key+'__contains = "'+L+'") '
      else:
        _m += ' & ~Q('+key+'__contains = "'+L[1:]+'") '
    return _m +' ) '
    
  if v[1] in ['in', 'notin']:
    return v[0]+' Q('+key+'__'+v[1]+' = '+str(v[2])+') ' # this is a list in case of in/notin
  else:
    return v[0]+' Q('+key+'__'+v[1]+' = "'+str(v[2])+'") ' # else the v[2] will be String

@csrf_exempt
def ajax_{MODEL_NAME}_asearch(request): # We support POST only .
  res=None
  # This is basically a search by a tag or list items with given arguments
  if request.method == 'GET':
    return AutoHttpResponse(501)
  # This is basically a append to a list with given arguments
  elif request.method == 'POST':
    id=request.POST.get('id',None)    
    try: 
      #{ADVSEARCH_POST_GET_ARG}
      non_field_params = ['orderBy','include','exclude']
      orderBy = request.POST.get('orderBy',None);
      if orderBy: orderBy = orderBy.split(',')
      include = request.POST.get('include',None);
      if include: include = include.split(',')
      exclude = request.POST.get('exclude',None);
      if exclude: exclude = exclude.split(',')
      
      #Define Query Strings.
      queryDict = dict(request.POST)
      for _x in non_field_params:
        if queryDict.has_key(_x):
          del queryDict[_x]
      #Now we should only have Database field.
      Qstr= ''
      for key, value in queryDict.iteritems():         
        if isinstance(value,str):
          v = parseTriple(value)
          if v: Qstr += query_str_builder(key,v)
        else:
          for v in value:
            v = parseTriple(v)
            if v: Qstr += query_str_builder(key,v)
      Qstr = Qstr[2:]         
      
    except:
      D_LOG()
      return AutoHttpResponse(400,'Wrong Pentameter format.') 	   
    
    try:
       res = {MODEL_NAME}Manager.advSearch{MODEL_NAME}(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)
""".format(MODEL_NAME=mname,ADVSEARCH_POST_GET_ARG=ADVSEARCH_POST_GET_ARG,MODEL_ARG_ARG=MODEL_ARG_ARG)     

  # 3.  For Tag Feature 
  if min_view:
      ajs *= """
@csrf_exempt
def ajax_{MODEL_NAME}_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = {MODEL_NAME}Manager.minView{MODEL_NAME}(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  
""".format(MODEL_NAME=mname)  

  # 3.  For Tag Feature 
  if quick_search:
      ajs *= """
@csrf_exempt
def ajax_{MODEL_NAME}_quick_search(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    q=request.GET.get('q',None)
    if not q:
      return AutoHttpResponse(200,'you must a input called ?q=abcd') 
    res = {MODEL_NAME}Manager.get{MODEL_NAME}_quick_search(q=q,page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  
""".format(MODEL_NAME=mname) 
  ##################  Generating the urls.py file #########################
  #########################################################################
  
  #1. Generating basic urls.....
  us*= """
urlpatterns += patterns('',
    # Read Operation
    (r'^api/{MODEL_NAME_L}/$',ajaxHandeler.ajax_{MODEL_NAME}),
    (r'^api/{MODEL_NAME_L}/(?P<id>\d+)/$',ajaxHandeler.ajax_{MODEL_NAME}),
    #(r'^{MODEL_NAME_L}/$',views.tt_home),
)
""".format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower())
  #2. Adding Reverse many to many Key in Ajax handaler
  for (field_name,ref_model) in MAP_One2One[mname]+MAP_Many2ManyKey[mname]+Rev_Many2ManyKey[mname]:
      pass
      us*= """
urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/{MODEL_NAME_L}/(?P<id>\d+)/{ref_model_L}/$',ajaxHandeler.ajax_{MODEL_NAME}_{ref_model}),
)
""".format(MODEL_NAME=mname,ref_model=ref_model,MODEL_NAME_L=mname.lower(),ref_model_L = ref_model.lower())

  #3. For Tag addon 
  if tag_ops:
    us*= """
urlpatterns += patterns('',
    # Allowing adding and removing tags..
    (r'^api/{MODEL_NAME_L}/(?P<id>\d+)/list/$',ajaxHandeler.ajax_{MODEL_NAME}_list),
    (r'^api/{MODEL_NAME_L}/list/$',ajaxHandeler.ajax_{MODEL_NAME}_list),
)
""".format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower())
  #4. For Advance Serach
  if advance_serach:
    us*= """
urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/{MODEL_NAME_L}/aq/$',ajaxHandeler.ajax_{MODEL_NAME}_asearch),
)
""".format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower())

  #4. Addon
  if min_view:
    us*= """
urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/{MODEL_NAME_L}/mv/$',ajaxHandeler.ajax_{MODEL_NAME}_min_view),
)
""".format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower())

  #4. Addon
  if quick_search:
    us*= """
urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/{MODEL_NAME_L}/qs/$',ajaxHandeler.ajax_{MODEL_NAME}_quick_search),
)
""".format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower())

  ##################  Generating the Help file #########################
  ######################################################################
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
      
  hs*= """
    List of APIs to maintain relationship with other model
    =======================================================
    ( note that for O2O and Frn Key can be done through update Method )
"""    
  #Help String for Many2ManyKey
  for (field_name,ref_model) in MAP_One2One[mname]+MAP_Many2ManyKey[mname]+Rev_Many2ManyKey[mname]:
      pass
      hs*= """
     i) Getting all {ref_model} for a {MODEL_NAME}
         HTTP: GET /api/{MODEL_NAME}/1/{ref_model}/

    ii) Adding more {ref_model} for a {MODEL_NAME}
         HTTP: POST /api/{MODEL_NAME}/1/{ref_model}/
         DATA: action=ADD&{field_name}=[1,2,3]

    iii) Removing more {ref_model} for a {MODEL_NAME}
         HTTP: POST /api/{MODEL_NAME}/1/{ref_model}/
         DATA: action=DEL&{field_name}=[1,2,3]

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

  #Help String for advance_serach
  if advance_serach:
      pass
      hs*= """
    x) Advance Search Example 
         HTTP: POST : http://192.168.56.101:7777/api/Author/aq/
         DATA : name=dipankar12322333&reg=1&tag1=%5B3%2C4%5D&action=APPEND
         orderBy=reg%2Cname&include=name%2Creg&name=%3Astartswith%3Aa
      1) Filter Data by startswith, endswith , exact, iexact etc.
          DATA format => and:startswith:abc OR <or:endswith:abc> like this
      2) Performing odrer by
         example  Data => oredrBy=name,reg 
      3) Only includes some colus
      Example1: find all item but show only name and reg column ? <include=name,reg> : OK
      4) Tag Serach :
      Example1: find all item having tag a and b and c ? Ans : <and:tagin:a,b,c> OK
      Example2: Find all item having tag a and b but not tag c ? Ans :  <and:tagin:a,b,-c> OK
      Example3: Find All item having tag a and b or tag c and d? Ans :  <and:tagin:a,b> <or:tagin:c,d> = OK
      Example4: Find All item doesn't have tag a ?                Ans  : <and:tagin:-a> OK


""".format(MODEL_NAME=mname)

 # Addon  : min_view
  if min_view:
      pass
      hs*= """
    xi) Min View 
    ===================
    Get Some Data Not all data from the table
    - It's Useful if yiu have lot of column in {MODEL_NAME} table.
         HTTP: GET : http://192.168.56.101:7777/api/Author/mv/
         DATA : page=10&limit=2
""".format(MODEL_NAME=mname)
 # Addon  : quick_search
  if quick_search:
      pass
      hs*= """
    xi) quick_search
    ===================
    You you can show lookup while typing - quick search as you type..
    - It's Useful if yiu have lot of column in {MODEL_NAME} table.
         HTTP: GET : http://192.168.56.101:7777/api/Author/qs/
         DATA : page=10&limit=2
""".format(MODEL_NAME=mname)

  # End of Processing this model table.
  
  ##################  Generate JS file Here ###########################
  # Generate JS  Head
  js*="""
  
/************ start of {MODEL_NAME} Controller*****************/
myApp.controller("{MODEL_NAME}Controller",  function ($scope,$http,$sce) {{ 

    $scope.renderHtml = function (htmlCode) {{
            return $sce.trustAsHtml(htmlCode);
    }};
/************ Initialize all Data Variable. *****************/
$scope.item ={{}}
$scope.item_list ={{}}
$scope.ref_list_items =[]
$scope.limit=10;

$scope.quick_search={{'in':'','out':''}}
""".format(MODEL_NAME=mname)
  
  #Js caller
  js*="""
/*********************  get MiniView *****************/
$scope.getMiniView=function(a) {{
  $http.get("/api/{MODEL_NAME_L}/?page="+a+"&limit="+$scope.limit+"")
      .success(function(data, status, headers, config) {{
        console.log(data)
        $scope.item_list = data.res;
        // DONT DO THIS BAD USER EXP$scope.status = data.status; $scope.msg=data.msg
        $scope.orderByField = 'id';
        $scope.reverseSort = false;
       // Not incduing this feature tableResize('#table_miniview_{MODEL_NAME}');
      }})
      .error(function(data, status, headers, config) {{ console.log('Error happen with status:'+status) }});  
}}
$scope.getMiniView(1);
/************ getting full data for an Item *****************/
$scope.getItem = function(a) {{
     $http.get("/api/{MODEL_NAME_L}/"+a+"/")
    .success(function(data, status, headers, config) {{
      console.log(data)
      $scope.item = data.res;
      $scope.status = data.status; $scope.msg=data.msg
    }})
    .error(function(data, status, headers, config) {{console.log('Error happen with status:'+status)}}); 
  }}

/************ creating a new Item  *****************/
$scope.createItem = function(a) {{
    console.log($('form#{MODEL_NAME_L}').serialize())
    $http({{
          method: "post",
          url: '/api/{MODEL_NAME_L}/',
          headers: {{ 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}},
          data:$('form#{MODEL_NAME_L}').serialize()
    }})
    .success(function(data, status, headers, config) {{
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data)
     $scope.getMiniView(1);
    }})
    .error(function(data, status, headers, config) {{

    }}); 
}}

/************ Updating an Item data  *****************/
$scope.updateItem = function(a) {{
    if($scope.item.id == null)
    {{
     $scope.status = 'error'; $scope.msg=' Please select a raw in left panel to update';
     return;
    }}
    $http({{
          method: "post",
          url: '/api/{MODEL_NAME_L}/'+$scope.item.id+'/',
          headers: {{ 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}},
          data:$('form#{MODEL_NAME_L}').serialize()
    }})
    .success(function(data, status, headers, config) {{
     $scope.status = data.status; $scope.msg=data.msg
     console.log(data);
     $scope.getMiniView(1);
    }})
    .error(function(data, status, headers, config) {{
    }}); 
}}

/************ delete an Item data  *****************/
$scope.deleteItem = function(a){{
  $http.delete("/api/{MODEL_NAME_L}/"+a+"/")
      .success(function(data, status, headers, config) {{
        $scope.item_list = data;
        $scope.status = data.status; $scope.msg=data.msg
        console.log(data);
        $scope.getMiniView(1);
      }})
      .error(function(data, status, headers, config) {{
        console.log('Error happen with status:'+status)
      }});  
}}

/*************** reset an item<used in form>***********************/
$scope.resetItem = function() {{
  $scope.getItem($scope.item.id)
}}


/************ Selectors: Retune a list of name for own model*****************/
$scope.selectItem = function(a) {{
    $http({{
          method: "post",
          url: '/api/{MODEL_NAME_L}/aq/?limit=50',
          headers: {{ 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}},
          data:{{'include':'name'}}
    }})
    .success(function(data, status, headers, config) {{
    $scope.{MODEL_NAME_L}_lookup = data.res.data;
    }})
    .error(function(data, status, headers, config) {{
    }}); 
}}
""".format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower())
  
  # Adding Js for One2One or 
  for (field_name,ref_model) in MAP_One2One[mname]+Rev_Many2ManyKey[mname]:
      js*= """
$scope.get{ref_model} = function(a) {{
     $http.get("/api/{MODEL_NAME_L}/"+a+"/{ref_model_L}/")
    .success(function(data, status, headers, config) {{
      console.log(data);
      $scope.ref_item = data.res;
      $scope.ref_list_items = {{}};
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#o2o-{MODEL_NAME_L}','show');
    }})
    .error(function(data, status, headers, config) {{ console.log('Error happen with status:'+status)}}); 
  }}
""".format(MODEL_NAME=mname,ref_model=ref_model,MODEL_NAME_L=mname.lower(),ref_model_L = ref_model.lower())

  # Adding Js for Many2many or 
  for (field_name,ref_model) in MAP_Many2ManyKey[mname]:
      js*= """
//Get
$scope.get{ref_model}= function(a) {{
     $http.get("/api/{MODEL_NAME_L}/"+a+"/{ref_model_L}/")
    .success(function(data, status, headers, config) {{
      console.log(data);
      $scope.ref_item = {{}}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
      addClass('#m2m-{MODEL_NAME_L}','show');
    }})
    .error(function(data, status, headers, config) {{ console.log('Error happen with status:'+status)}}); 
  }}
 /* Implements both Add + remove */
$scope.add{ref_model}= function(a,b,c) {{
    $http({{
          method: "post",
          url: "/api/{MODEL_NAME_L}/"+a+"/{ref_model_L}/",
          headers: {{ 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}},
          data:{{{ref_model_L}: b, action: c}}
    }})
    .success(function(data, status, headers, config) {{
      console.log(data);
      $scope.ref_item = {{}}
      $scope.ref_list_items = data.res;
      $scope.status = data.status; $scope.msg=data.msg
     
    }})
    .error(function(data, status, headers, config) {{ console.log('Error happen with status:'+status)}}); 
    //repopulate..
    $scope.get{ref_model};
  }}
""".format(MODEL_NAME=mname,ref_model=ref_model,MODEL_NAME_L=mname.lower(),ref_model_L = ref_model.lower())

  # Adding quick_search in JS
  js*= """
$scope.qs{ref_model}= function(a) {{
     $http.get("/api/{MODEL_NAME_L}/qs/?q="+$scope.quick_search.in)
    .success(function(data, status, headers, config) {{
      console.log(data);
      $scope.quick_search.out= data.res;
      $scope.status = data.status; $scope.msg=data.msg
      //addClass('#m2m-{MODEL_NAME_L}','show');
    }})
    .error(function(data, status, headers, config) {{ console.log('Error happen with status:'+status)}}); 
  }}
""".format(MODEL_NAME=mname,ref_model=ref_model,MODEL_NAME_L=mname.lower(),ref_model_L = ref_model.lower())

  #################### Define Quick LoopUp (select DropBox)for each reference mode #############################
  for (field_name,ref_model) in MAP_Many2ManyKey[mname]+MAP_One2One[mname]+Rev_Many2ManyKey[mname]:
      js*= """
$scope.select{ref_model}= function() {{
    $http({{
          method: "post",
          url: "/api/{ref_model_L}/aq/?limit=50",
          headers: {{ 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}},
          data:{{'include':'name'}},
    }})
    .success(function(data, status, headers, config) {{
      console.log(data);
      $scope.{ref_model}_lookup= data.res.data
    }})
    .error(function(data, status, headers, config) {{ console.log('Error happen with status:'+status)}}); 
  }}
  
$scope.select{ref_model}();
""".format(MODEL_NAME=mname,ref_model=ref_model,MODEL_NAME_L=mname.lower(),ref_model_L = ref_model.lower())


  # JS Tail
  js*="""
  // Populate the variable as necessary,,
  //TODO Thsi wuld not work as the caller HTML is not ahve controller
  $scope.onLoad{MODEL_NAME} =function(){{
    console.log('You have clicked {MODEL_NAME}')
    $scope.getMiniView(1);
  }}
}});
/************ End of {MODEL_NAME} Controller*****************/
""".format(MODEL_NAME=mname,ref_model=ref_model,MODEL_NAME_L=mname.lower(),ref_model_L = ref_model.lower())


  
  ##################  End Of Js file gen ##############################
  

  print '    [GEN] Complete Processing module'+mname
  print '\n\n\n'
  # End of the current model
#End loop for all model.  
print '    [GEN] Code Gen complete.'
print '    [GEN] Writing into files'


##################  Update HTML generations Must not be the part of models loop ########################

################## Start of HTML generations ########################
#1. Build Templets




#this is the biggest template

#2. code  gen  for each reference model..
#
#  HTML_QUICK_SERACH= genStr("""
#  <div>
#     <form class="group-input oneliner nolevel horz icon right">
#        <legend>Search</legend>
#        <input type="text" data-icon="\f087" name="text" ng-model="quick_search.in"  ng-keyup="qs{ref_model}()" ><i class="fa fa-spinner"></i>
#     </form>
#        <table class="table" ng-show="quick_search.out">
#        <tr ng-repeat="_i in quick_search.out">
#            <td ng-repeat="(key, val) in _i">{{{{val}}}}</td>
#            <td ><button class="btn" ng-click="add{ref_model}(item.id,_i.id,'add')">Add</button> </td>
#            <td ><button class="btn" ng-click="add{ref_model}(item.id,_i.id,'del')">del</button> </td>
#        </tr>
#        </table>
#    </div>
#""",
#
#'\n')
# 
   
# Generate Menu..
TEMPLATE_ALL_MODEL_MENU_BTN = genStr("""<a style="padding-left: 0; transition: font-size 0.3s ease 0s;" ng-click="onLoad{x}();" onclick="removeClass('.section','show');addClass('#{x}-div','show');"><i class="fa fa-home fa-fw"></i></a><p style=" padding-left: 6px;">{x}</p>""",ALL_XML_DATA_ONE_PLACE['model_list'].keys(),"")

ext_page_menu =  genStr("""<a style="padding-left: 0; transition: font-size 0.3s ease 0s;" ng-click="onLoad{x}();" onclick="removeClass('.section','show');addClass('#{x}-div','show');"><i class="fa fa-home fa-fw"></i></a><p style=" padding-left: 6px;">{x}</p>""",[ _i['name'] for _i in PAGE_LIST] ,"")

TEMPLATE_ALL_MODEL_MENU_BTN+=ext_page_menu

html*= """
<div id="menu" class="sidebar-popup left" style="width: 100px;">  
  <div class="group-btn icon-only noborder">
  {TEMPLATE_ALL_MODEL_MENU_BTN}
  </div>  
</div> 
""".format(TEMPLATE_ALL_MODEL_MENU_BTN=TEMPLATE_ALL_MODEL_MENU_BTN)
## End of generating menu

#2. Model Related div will be here..
for mname in ALL_XML_DATA_ONE_PLACE['model_list'].keys():
  
  #Generate Template spacific to model
  field_list_all = ALL_XML_DATA_ONE_PLACE['model_list'][mname]
  
  TEMPLATE_ALL_REF_BTN = genStr("""<button ng-click="get{x[1]}(item.id)">{x[1]}</button>""",MAP_One2One[mname]+MAP_Many2ManyKey[mname]+Rev_Many2ManyKey[mname],'\n') 

  
  ALL_REF_SELECT_DROP_DOWN={}
  for (f,m) in MAP_One2One[mname]+MAP_Many2ManyKey[mname]+Rev_Many2ManyKey[mname]:
    _a='<select name="'+f+'">'
    _a+= '{{'+m+'_lookup}}'
    _a+= '<option ng-repeat="_o in '+m+'_lookup" value="{{_o.id}}">{{_o.name }}</option>'
    _a+='</select>'
    ALL_REF_SELECT_DROP_DOWN[f] = _a
    


  TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW = '\n'
  for _f in field_list_all:
    TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW+="<tr>\n  <td>"+_f[0]+": </td>\n  <td>"
    if _f[4] == 'radio':
      _a = """<div class="group">"""
      for _c in _f[6]:
        _a+= '<input type="radio" checked="item.'+_f[0]+'=='+_c+ '" value="'+_c+'" name="'+_f[0]+'"><span for="rad1">'+_c+'</span>'
      _a+= '</div>'
      TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW+=_a
    elif _f[2] in ['ManyToManyField','ForeignKey','OneToOneField']:
      TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW+=ALL_REF_SELECT_DROP_DOWN[_f[0]]
    else:
     TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW+="<input name ='"+_f[0]+"' type='text' ng-model='item."+_f[0]+"'/>"    
    TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW+="</td>\n</tr>\n"

  html*= """
  <div id="{MODEL_NAME}-div" class="hide section" ng-controller="{MODEL_NAME}Controller" style="position: relative;">
  <p class="p f16 b inv-color bar"> Test Model :{MODEL_NAME} </p>

  <!-- this for Miniview Serach Result -->
    <div class="box s500X700 inline noshadow ">
       <div class="group-input horz showicon">
          <i class="fa fa-arrows-v"></i>
          <select style="width:70px" id="serach-limit" ng-model="limit" ng-change="getMiniView(1)">
            <option value="10">10</option>
            <option value="15">15</option>
            <option value="20">20</option>
          </select>
       <p style="float:right;"><i class="fa fa-search"></i><input ng-model="query" style="width:200px"></p>
       </div>
      <div style=" height: 570px;"> 
          <table id="table_miniview_{MODEL_NAME}" class="table bordered striped hover" ng-show="item_list.data" >
            <thead>
              <tr>           
                  <th ng-repeat="(key, val) in item_list.data[0]">
                  <a href="javascript:void(0)" >
                  {{{{key}}}}<i class="fa" ng-class="reverseSort? 'fa-sort-up' : 'fa-sort-down'"></i>
                  </a>
                  {{{{orderByField}}}}
                  </th>
                  <th> Actions </th>
              </tr>     
             </thead>
             <tbody>     
              <tr ng-click="getItem(item.id)" ng-repeat="item in item_list.data | orderBy:id:true| filter:query">
                  <td ng-repeat="(key, val) in item">{{{{val}}}}</td>
                  <td >
                     <div class="group-btn horz text-only" style="margin: 0px">
                     <button ng-click="deleteItem(item.id)">delete</button>
                     
                     {TEMPLATE_ALL_REF_BTN}
                     </div>
                 </td>
              </tr>
            </tbody>
          </table>
      </div>
      <!-- this for pagination -->
      <div class="pagination rfloat" ng-hide="item_list.max == '0'">
        <button ><i class="fa fa-chevron-left"></i></button>
        <button ng-repeat="n in [] | range:item_list.max" ng-click="getMiniView($index+1)">{{{{$index+1}}}}</button>
        <button ><i class="fa fa-chevron-right"></i></button>
      </div>  
    </div>
    <!-- print the Details /Full View of a Item -->  
    <div class="box s600X700 inline noshadow group-input"> 
    <!-- This is for Message -->
      <div class="notification-popup success  {{{{status}}}}">
        <strong>{{{{status}}}} ! </strong> {{{{msg}}}}
      </div>
        
      <form id="{MODEL_NAME_L}" name="form1" novalidate>
        <table>
        <tr><td>id:</td><td><input name ="id" type="text" ng-model="item.id" disabled="disabled" /></td> </tr>
        {TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW}
        </table>
        <div class="group-btn horz text-only separated">
          <button ng-click="resetItem()">RESET</button>
          <button ng-click="createItem()">CopyCrete</button>
          <button ng-click="createItem()">NewCrete</button>
          <button ng-click="updateItem()">Update</button>
        </div>
      </form>
    </div> 


    <!--- print Refer List of Item : ref_list_items -->
    <div class="sidebar-popup" id="m2m-{MODEL_NAME_L}">
      <div class="group-btn horz separated" >
        <a  class="btn sqr primary" onclick="removeClass('#m2m-{MODEL_NAME_L}','show')"> Submit</a>
        <a  class="btn sqr secondary" onclick="removeClass('#m2m-{MODEL_NAME_L}','show')"> Close </a>
      </div>    
      <table class="table" ng-show="ref_list_items">
          <tr>
              <th ng-repeat="(key, val) in ref_list_items[0]">{{{{key}}}}</th>
          </tr>
          <tr ng-repeat="_i in ref_list_items">
              <td ng-repeat="(key, val) in _i">{{{{val}}}}</td>
          </tr>
      </table>
    </div>


    <!--- print Refer of Item (Single Item) : ref_item -->
    <div class="sidebar-popup" id="o2o-{MODEL_NAME_L}">
      <table  class="table" ng-show="ref_item">
          <tr>
              <th ng-repeat="(key, val) in ref_item[0]">{{{{key}}}}</th>
          </tr>
           <tr ng-repeat="item in ref_item">
             <td ng-repeat="(key,val) in item">{{{{val}}}}</td>
           </tr>
      </table>
      <div class="group-btn horz separated" >
        <a  class="btn sqr primary" onclick="removeClass('#o2o-{MODEL_NAME_L}','show')"> Submit</a>
        <a  class="btn sqr secondary" onclick="removeClass('#o2o-{MODEL_NAME_L}','show')"> Close </a>
      </div>
    </div>
    

  </div>
    
  """.format(MODEL_NAME=mname,MODEL_NAME_L=mname.lower(),
  TEMPLATE_ALL_REF_BTN=TEMPLATE_ALL_REF_BTN,
  TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW=TEMPLATE_ALL_INPUT_FIELD_AS_TABLE_ROW,
  )
  #end of model loop


#ext_page_body
for _p in PAGE_LIST:

  f=open(_p['target'])
  html*= """
  <div id="{name}-div" class="hide section"  {dependon} style="position: relative;">
  <p class="p f16 b inv-color bar"> Test Model :{name} </p>""".format(name=_p['name'],dependon = 'ng-controller="'+_p['dependon']+'Controller"' if _p['dependon'] else '' );
  html *= f.read()
  f.close()
  html*="</div>"
 
    
  

##################   End of HTML generations ######################## 

##################  End of Independent HTML generations #################################################  

#trail of HTML and JS
html *= """
  </body>
</html>  
<!--  ---------------- End of HTML file ----------------- -->
"""
js *= """

/*** End of JS file ***/
"""


mf = open(APP_NAME+'/models.py','w+');mf.write(str(ms));mf.close() #model.py
apf = open(APP_NAME+'/api.py','w+');apf.write(str(aps));apf.close() #api.py
ajf = open(APP_NAME+'/ajaxHandeler.py','w+');ajf.write(str(ajs));ajf.close() #AjaxHandaler.py
uf = open(APP_NAME+'/mapping.py','w+');uf.write(str(us));uf.close() #mapping.py 
uf = open(APP_NAME+'/__init__.py','w+');uf.write("#Simple Init file");uf.close() #init file
hf = open(APP_NAME+'/help.txt','w+');hf.write(str(hs));hf.close() #help file
cf = open(APP_NAME+'/common.py','w+');cf.write(str(cc));cf.close()  # common functions here

jsf = open(APP_NAME+'/'+APP_NAME+'.js','w+');jsf.write(str(js));jsf.close() #js file
htmlf = open(APP_NAME+'/'+APP_NAME+'.html','w+');htmlf.write(str(html));htmlf.close()  # html code here
