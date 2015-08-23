import pdb
from common import *
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *

from .models import User
class UserManager:
  @staticmethod
  def createUser(uname='newUser',fname=None,lname=None,passwd=None,email=None,dob=None,desc=None,pic_url=None,address=None,social_id={'google':0,'facebook':0,'github':0,'linkedin':0},payload={'allid':0,'recent_id':0},): #Crete an Obj
    try:
      
      
      
      t = User(uname=uname,fname=fname,lname=lname,passwd=passwd,email=email,dob=dob,desc=desc,pic_url=pic_url,address=address,social_id=social_id,payload=payload,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New User got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create User:'+getCustomException(e),'sys_error':str(e)}
  # Note taht to access all please call search method.. UserManager.searchUser()
  @staticmethod
  def getUser(id,mv=None): # get Json
    try:
      t=User.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      if mv != None:
        #send Mini view only..
        include =[u'uname', u'fname', u'email', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'User returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive User:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getUserObj(id): #get Obj
    try:
      t=User.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'User Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object User:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateUser(id,uname='newUser',fname=None,lname=None,passwd=None,email=None,dob=None,desc=None,pic_url=None,address=None,social_id={'google':0,'facebook':0,'github':0,'linkedin':0},payload={'allid':0,'recent_id':0}, ): #Update Obj
    try:
      res=UserManager.getUserObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
      
        
      
      t.uname = uname if uname is not None else t.uname;t.fname = fname if fname is not None else t.fname;t.lname = lname if lname is not None else t.lname;t.passwd = passwd if passwd is not None else t.passwd;t.email = email if email is not None else t.email;t.dob = dob if dob is not None else t.dob;t.desc = desc if desc is not None else t.desc;t.pic_url = pic_url if pic_url is not None else t.pic_url;t.address = address if address is not None else t.address;t.social_id = social_id if social_id is not None else t.social_id;t.payload = payload if payload is not None else t.payload;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'User Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update User:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def deleteUser(id): #Delete Obj
    
    return {'res':None,'status':'error','msg':'Entry Deletion is not allowed by configuration! '}
    
    try:
      t=User.objects.get(pk=id)
      
      t.delete()
      return {'res':None,'status':'info','msg':'one User deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete User:'+getCustomException(e,id),'sys_error':str(e)}


  @staticmethod
  def searchUser(uname='newUser',fname=None,lname=None,passwd=None,email=None,dob=None,desc=None,pic_url=None,address=None,social_id={'google':0,'facebook':0,'github':0,'linkedin':0},payload={'allid':0,'recent_id':0},page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if uname is not None: Query['uname__contains']=uname
      if fname is not None: Query['fname__contains']=fname
      if lname is not None: Query['lname__contains']=lname
      if passwd is not None: Query['passwd__contains']=passwd
      if email is not None: Query['email__contains']=email
      if dob is not None: Query['dob']=dob
      if desc is not None: Query['desc__contains']=desc
      if pic_url is not None: Query['pic_url__contains']=pic_url
      if address is not None: Query['address__contains']=address
      if social_id is not None: Query['social_id']=social_id
      if payload is not None: Query['payload']=payload #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      if mv == None:
        include =[u'uname', u'fname', u'email', 'id']
      else:
        include = mv
      dd=User.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'User search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search User:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchUser(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'User Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=User.objects.filter(Qstr)
      else:
        dd=User.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'uname', u'fname', u'email', 'id']+['id']
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

      return {'res':res,'status':'info','msg':'User search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search User!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewUser(page=None,limit=None):
    try:
      res =None
      include =[u'uname', u'fname', u'email', 'id']
      dd=User.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Mini View User  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search User!','sys_error':str(e)}


  #Advance search is Implemented here..
  @staticmethod
  def getUser_quick_search(q,page=None,limit=None):
    try:
      res = None
      include =['id','uname']
      dd=User.objects.filter(uname__startswith=q).values(*include)
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page)      
      res = list(dd.object_list)
      if not res: return {'res':res,'status':'info','msg':'Nothing match with your query'} 
      return {'res':res,'status':'success','msg':'User match with your query'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search User!','sys_error':str(e)}

