import pdb
from common import *
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *

from .models import Code
class CodeManager:
  @staticmethod
  def createCode(name=None,short_desc=None,full_desc=None,main=None,func=None,input=None,solution=None,level=None,language=None,compilation=None,tag=None,topic=None,): #Crete an Obj
    try:
      if tag and not set(tag).issubset(set([u'Recent', u'fevarite', u'Todo'])) : return {'res':None,'status':'error','msg':"tag must be either of [u'Recent', u'fevarite', u'Todo'] ",'sys_error':''};
      if topic and not set(topic).issubset(set([u'DS', u'ALGO', u'Bit', u'Array', u'String', u'LinkedList', u'Tree', u'Graph', u'DP', u'Greedy', u'Backtrack', u'DivideConc', u'Recursion', u'RealTime', u'Funny', u'NP'])) : return {'res':None,'status':'error','msg':"topic must be either of [u'DS', u'ALGO', u'Bit', u'Array', u'String', u'LinkedList', u'Tree', u'Graph', u'DP', u'Greedy', u'Backtrack', u'DivideConc', u'Recursion', u'RealTime', u'Funny', u'NP'] ",'sys_error':''};
      
      
      
      t = Code(name=name,short_desc=short_desc,full_desc=full_desc,main=main,func=func,input=input,solution=solution,level=level,language=language,compilation=compilation,tag=tag,topic=topic,)
      t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Code got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Code:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getCode(id,mv=None): # get Json
    try:
      t=Code.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      if mv != None:
        #send Mini view only..
        include =[u'name', u'short_desc', u'level', u'topic', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'Code returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Code:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getCodeObj(id): #get Obj
    try:
      t=Code.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Code Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Code:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateCode(id,name=None,short_desc=None,full_desc=None,main=None,func=None,input=None,solution=None,level=None,language=None,compilation=None,tag=None,topic=None, ): #Update Obj
    try:
      res=CodeManager.getCodeObj(id)
      if res['res'] is None: return res
      t=res['res']
      if tag and not set(tag).issubset(set([u'Recent', u'fevarite', u'Todo'])) : return {'res':None,'status':'error','msg':"tag must be either of [u'Recent', u'fevarite', u'Todo'] ",'sys_error':''};
      if topic and not set(topic).issubset(set([u'DS', u'ALGO', u'Bit', u'Array', u'String', u'LinkedList', u'Tree', u'Graph', u'DP', u'Greedy', u'Backtrack', u'DivideConc', u'Recursion', u'RealTime', u'Funny', u'NP'])) : return {'res':None,'status':'error','msg':"topic must be either of [u'DS', u'ALGO', u'Bit', u'Array', u'String', u'LinkedList', u'Tree', u'Graph', u'DP', u'Greedy', u'Backtrack', u'DivideConc', u'Recursion', u'RealTime', u'Funny', u'NP'] ",'sys_error':''};
      
      changes='';
      changes += '< name:'+ str(t.name) +' -> '+str( name)+' >'  if name is not None  else '' 
      changes += '< short_desc:'+ str(t.short_desc) +' -> '+str( short_desc)+' >'  if short_desc is not None  else '' 
      changes += '< full_desc:'+ str(t.full_desc) +' -> '+str( full_desc)+' >'  if full_desc is not None  else '' 
      changes += '< main:'+ str(t.main) +' -> '+str( main)+' >'  if main is not None  else '' 
      changes += '< func:'+ str(t.func) +' -> '+str( func)+' >'  if func is not None  else '' 
      changes += '< input:'+ str(t.input) +' -> '+str( input)+' >'  if input is not None  else '' 
      changes += '< solution:'+ str(t.solution) +' -> '+str( solution)+' >'  if solution is not None  else '' 
      changes += '< level:'+ str(t.level) +' -> '+str( level)+' >'  if level is not None  else '' 
      changes += '< language:'+ str(t.language) +' -> '+str( language)+' >'  if language is not None  else '' 
      changes += '< compilation:'+ str(t.compilation) +' -> '+str( compilation)+' >'  if compilation is not None  else '' 
      changes += '< tag:'+ str(t.tag) +' -> '+str( tag)+' >'  if tag is not None  else '' 
      changes += '< topic:'+ str(t.topic) +' -> '+str( topic)+' >'  if topic is not None  else '' 
      if changes: t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        
      
      t.name = name if name is not None else t.name;t.short_desc = short_desc if short_desc is not None else t.short_desc;t.full_desc = full_desc if full_desc is not None else t.full_desc;t.main = main if main is not None else t.main;t.func = func if func is not None else t.func;t.input = input if input is not None else t.input;t.solution = solution if solution is not None else t.solution;t.level = level if level is not None else t.level;t.language = language if language is not None else t.language;t.compilation = compilation if compilation is not None else t.compilation;t.tag = tag if tag is not None else t.tag;t.topic = topic if topic is not None else t.topic;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Code Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Code:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteCode(id): #Delete Obj
    try:
      d=Code.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Code deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Code:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchCode(name=None,short_desc=None,full_desc=None,main=None,func=None,input=None,solution=None,level=None,language=None,compilation=None,tag=None,topic=None,page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if short_desc is not None: Query['short_desc__contains']=short_desc
      if full_desc is not None: Query['full_desc__contains']=full_desc
      if main is not None: Query['main__contains']=main
      if func is not None: Query['func__contains']=func
      if input is not None: Query['input__contains']=input
      if solution is not None: Query['solution__contains']=solution
      if level is not None: Query['level__contains']=level
      if language is not None: Query['language__contains']=language
      if compilation is not None: Query['compilation__contains']=compilation
      if tag is not None: Query['tag']=tag
      if topic is not None: Query['topic']=topic #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'short_desc', u'level', u'topic', 'id']
      dd=Code.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Code search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Code:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def appendListCode(id,tag=[],topic=[],):
    try:
       res=CodeManager.getCodeObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag = sorted(list(set(t.tag+tag))) if tag is not None else t.tag;t.topic = sorted(list(set(t.topic+topic))) if topic is not None else t.topic;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}

  @staticmethod
  def removeListCode(id,tag=[],topic=[],):
    try:
       res=CodeManager.getCodeObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag = sorted(list(set(t.tag)-set(tag))) if tag is not None else t.tag;t.topic = sorted(list(set(t.topic)-set(topic))) if topic is not None else t.topic;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListCode(tag=[],topic=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag:Query['tag__contains']= x
      for x in topic:Query['topic__contains']= x # Autogen
      include =[u'name', u'short_desc', u'level', u'topic', 'id']
      dd=Code.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Code search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Code!','sys_error':str(e)}
  



  @staticmethod
  def appendListCode(id,tag=[],topic=[],):
    try:
       res=CodeManager.getCodeObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag = sorted(list(set(t.tag+tag))) if tag is not None else t.tag;t.topic = sorted(list(set(t.topic+topic))) if topic is not None else t.topic;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}

  @staticmethod
  def removeListCode(id,tag=[],topic=[],):
    try:
       res=CodeManager.getCodeObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag = sorted(list(set(t.tag)-set(tag))) if tag is not None else t.tag;t.topic = sorted(list(set(t.topic)-set(topic))) if topic is not None else t.topic;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListCode(tag=[],topic=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag:Query['tag__contains']= x
      for x in topic:Query['topic__contains']= x # Autogen
      include =[u'name', u'short_desc', u'level', u'topic', 'id']
      dd=Code.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Code search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Code!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def advSearchCode(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Code Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Code.objects.filter(Qstr)
      else:
        dd=Code.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'short_desc', u'level', u'topic', 'id']+['id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Code search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Code!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewCode(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'short_desc', u'level', u'topic', 'id']
      dd=Code.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Code  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Code!','sys_error':str(e)}


  #Advance search is Implemented here..
  @staticmethod
  def getCode_quick_search(q,page=None,limit=None):
    try:
      res = None
      include =['id','name']
      dd=Code.objects.filter(name__startswith=q).values(*include)
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page)      
      res = list(dd.object_list)
      if not res: return {'res':res,'status':'info','msg':'Nothing match with your query'} 
      return {'res':res,'status':'success','msg':'Code match with your query'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Code!','sys_error':str(e)}

