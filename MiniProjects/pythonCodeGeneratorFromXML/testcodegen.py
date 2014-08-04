"""
Created on Aug 2, 2014

@author: Dipankar

The Rule of XML
1. properties should be like : dict([ x.split('=') for x in a.split(',')])
"""
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

import codegen
from xml.dom import minidom
print '[GEN] Code Generation started'

ms = codegen.CodeGenerator()
aps = codegen.CodeGenerator()
ajs = codegen.CodeGenerator()
us = codegen.CodeGenerator()

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
us += """
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)
"""

xmldoc = minidom.parse('sample.xml')
models = xmldoc.getElementsByTagName('model')


for model in models:
  mname = model.getAttribute('name')
  print '[GEN] Processing module'+mname
  ms += "class %s(models.Model):"%mname
  ms.indent()
  arg = []
  OneOrFrnKey = []
  Many2ManyKey = []
  fields = model.getElementsByTagName('field')
  for f in fields:
    fname = f.getAttribute('name')
    prop = f.getAttribute('properties')
    if f.getAttribute('type')not in ['DictField', 'ListField']:
      ms += "%s = models.%s(%s)" % (f.getAttribute('name'), f.getAttribute('type'), f.getAttribute('properties'))
    else:
      ms += "%s = %s(%s)" % (f.getAttribute('name'), f.getAttribute('type'), f.getAttribute('properties'))

    if f.getAttribute('user_input') == 'yes':
      arg.append(fname)      
    elif f.getAttribute('user_input') == 'default':
      arg.append(fname)

    if f.getAttribute('type') in ['ForeignKey','OneToOneField']:
      OneOrFrnKey.append((fname, f.getAttribute('ref')))
    elif f.getAttribute('type') in ['ManyToManyField']:
      Many2ManyKey.append((fname, f.getAttribute('ref')))

  # Construct the Args
  print '[GEN] user args are :'+str(arg)
  MODEL_ARG = genStr("{x}",arg,',')# =>a,b,c,d
  MODEL_ARG_ARG = genStr("{x}={x}",arg,',') #=> a=a,b=b,c=c,
  MODEL_ARG_NON_NULL_UPDATE = genStr("t.{x} = {x} if {x} is not None else t.{x}",arg,';') #=> a=a,b=b,c=c,
  #QUERY_STR = genStr("t.{x} = {x} if {x} is not None else t.{x}",arg,';')
  QUERY_STR = genStr("\n      if {x} is not None: Query['{x}']={x}",arg,';')
  MODEL_ARG_GET =genStr("{x}=request.GET.get('{x}',None)",arg,';')
  MODEL_ARG_POST =genStr("{x}=request.POST.get('{x}',None)",arg,';')
  MODEL_FRN_KEY_LOOKUP =''
  MODEL_FRN_KEY_INFO = ''

  print OneOrFrnKey
  if OneOrFrnKey:
    MODEL_FRN_KEY_LOOKUP = genStr2("""
      {x}_res = {y}Manager.get{y}Obj(id={x})
      if {x}_res['res'] is None: return {x}_res
      {x} = {x}_res['res']""",OneOrFrnKey,'')
    MODEL_FRN_KEY_INFO = genStr2("res['{x}_desc'] = {y}Manager.get{y}(id=res['{x}'])['res']",OneOrFrnKey,';')
  # Makeing model methods
  ms.sp()
  ms += "def __unicode__(self):"
  ms.indent()
  ms += 'return u"'+model.getAttribute('name')+' : %s",  (self.id)'
  ms.dedent()
  ms.dedent()
  ms.sp()
  ms.sp()

  # Generating api.py
  aps*="""
from .models import {MODEL_NAME}
class {MODEL_NAME}Manager:
  @staticmethod
  def create{MODEL_NAME}({MODEL_ARG}):
    try:
      {MODEL_FRN_KEY_LOOKUP}
      new = {MODEL_NAME}({MODEL_ARG_ARG})
      new.save()
      return {{'res':model_to_dict(new),'status':'info','msg':'New {MODEL_NAME} got created.'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to create {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def get{MODEL_NAME}(id):
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
  def get{MODEL_NAME}Obj(id):
    try:
      t={MODEL_NAME}.objects.get(pk=id)
      return {{'res':t,'status':'info','msg':'{MODEL_NAME} Object returned'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to retrive object {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def update{MODEL_NAME}(id,{MODEL_ARG} ):
    try:
      res={MODEL_NAME}Manager.get{MODEL_NAME}Obj(id)
      if res['res'] is None: return res
      t=res['res']
      {MODEL_ARG_NON_NULL_UPDATE}
      t.save()
      return {{'res':model_to_dict(t),'status':'info','msg':'{MODEL_NAME} Updated'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to update {MODEL_NAME}','sys_error':str(e)}}

  @staticmethod
  def delete{MODEL_NAME}(id):
    try:
      d={MODEL_NAME}.objects.get(pk=id)
      d.delete()
      return {{'res':d,'status':'info','msg':'one {MODEL_NAME} deleted!'}}
    except Exception,e :
      return {{'res':None,'status':'error','msg':'Not able to delete {MODEL_NAME}!','sys_error':str(e)}}


  @staticmethod
  def search{MODEL_NAME}({MODEL_ARG}page=None,limit=None,id=None):
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
              MODEL_FRN_KEY_INFO=MODEL_FRN_KEY_INFO)
   
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
  return HttpResponse(json.dumps(res,default=json_util.default),mimetype = 'application/json')
""".format(MODEL_NAME=mname,MODEL_ARG=MODEL_ARG,MODEL_ARG_ARG=MODEL_ARG_ARG,
           MODEL_ARG_GET=MODEL_ARG_GET,MODEL_ARG_POST=MODEL_ARG_POST) 
  
  # Generating urls.py 
  us*= """
urlpatterns += patterns('',
    # Read Operation
    (r'^api/{MODEL_NAME}/$',ajaxHandeler.ajax_{MODEL_NAME}),
    (r'^api/{MODEL_NAME}/(?P<id>\d+)/$',ajaxHandeler.ajax_{MODEL_NAME}),
    #(r'^{MODEL_NAME}/$',views.tt_home),
)
""".format(MODEL_NAME=mname)
  
print '[GEN] Code Gen complete.'
print '[GEN] Writing into files'
mf = open('autoGenEngine/models.py','w+');mf.write(str(ms));mf.close()
apf = open('autoGenEngine/api.py','w+');apf.write(str(aps));apf.close()
ajf = open('autoGenEngine/ajaxHandeler.py','w+');ajf.write(str(ajs));ajf.close()
uf = open('autoGenEngine/mapping.py','w+');uf.write(str(us));uf.close()
uf = open('autoGenEngine/__init__.py','w+');uf.write("#Simple Init file");uf.close()