import pdb
from common import *
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *

from .models import Author
class AuthorManager:
  @staticmethod
  def createAuthor(name='hari',date=None,life={'house_rent':0,'food':0,'traval':0},mych=['type1'],): #Crete an Obj
    try:
      if mych and not set(mych).issubset(set([u'type1', u'type2', u'type3'])) : return {'res':None,'status':'error','msg':"mych must be either of [u'type1', u'type2', u'type3'] ",'sys_error':''};
      
      
      
      t = Author(name=name,date=date,life=life,mych=mych,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Author got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Author:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getAuthor(id,mv=None): # get Json
    try:
      t=Author.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      if mv != None:
        #send Mini view only..
        include =[u'name', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'Author returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Author:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getAuthorObj(id): #get Obj
    try:
      t=Author.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Author Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Author:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateAuthor(id,name='hari',date=None,life={'house_rent':0,'food':0,'traval':0},mych=['type1'], ): #Update Obj
    try:
      res=AuthorManager.getAuthorObj(id)
      if res['res'] is None: return res
      t=res['res']
      if mych and not set(mych).issubset(set([u'type1', u'type2', u'type3'])) : return {'res':None,'status':'error','msg':"mych must be either of [u'type1', u'type2', u'type3'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.date = date if date is not None else t.date;t.life = life if life is not None else t.life;t.mych = mych if mych is not None else t.mych;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Author Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Author:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteAuthor(id): #Delete Obj
    try:
      d=Author.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Author deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Author:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchAuthor(name='hari',date=None,life={'house_rent':0,'food':0,'traval':0},mych=['type1'],page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if life is not None: Query['life']=life
      if mych is not None: Query['mych']=mych #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Author.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'Author search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Author:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getAuthor_Book(id,mv=None):
    try:
       res=AuthorManager.getAuthorObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.book_set.all() ]
       if mv:
         include =[u'name', 'id']
         res= list(t.book_set.values(*include))
       return {'res':res,'status':'info','msg':'all book for the Author returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addAuthor_Book(id,book,flush=False):
    assert (isinstance(book,list)),"book must be a list type."
    try:
      res=AuthorManager.getAuthorObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.book.clear()
      for i in book:
           # get the object..
           obj=BookManager.getBookObj(i)['res']
           if obj is not None:
             t.book_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.book_set.all() ]
      return {'res':res,'status':'info','msg':'all book having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeAuthor_Book(id,book):
    assert (isinstance(book,list)),"book must be a list type."
    try:
      res=AuthorManager.getAuthorObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in book:
          # get the object..
          obj=BookManager.getBookObj(i)['res']
          if obj is not None:
            t.book_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.book_set.all() ]
      return {'res':res,'status':'info','msg':'all book having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some book not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchAuthor(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Author Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Author.objects.filter(Qstr)
      else:
        dd=Author.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']+['id']
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

      return {'res':res,'status':'info','msg':'Author search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Author!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewAuthor(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Author.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Mini View Author  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Author!','sys_error':str(e)}


from .models import Publication
class PublicationManager:
  @staticmethod
  def createPublication(name=None,accid=None,): #Crete an Obj
    try:
      
      
      
      t = Publication(name=name,accid=accid,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Publication got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Publication:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getPublication(id,mv=None): # get Json
    try:
      t=Publication.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      if mv != None:
        #send Mini view only..
        include =[u'name', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'Publication returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Publication:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getPublicationObj(id): #get Obj
    try:
      t=Publication.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Publication Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Publication:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updatePublication(id,name=None,accid=None, ): #Update Obj
    try:
      res=PublicationManager.getPublicationObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Publication Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Publication:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deletePublication(id): #Delete Obj
    try:
      d=Publication.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Publication deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Publication:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchPublication(name=None,accid=None,page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Publication.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'Publication search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Publication:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getPublication_Book(id,mv=None):
    try:
       res=PublicationManager.getPublicationObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.book_set.all() ]
       if mv:
         include =[u'name', 'id']
         res= list(t.book_set.values(*include))
       return {'res':res,'status':'info','msg':'all book for the Publication returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addPublication_Book(id,book,flush=False):
    assert (isinstance(book,list)),"book must be a list type."
    try:
      res=PublicationManager.getPublicationObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.book.clear()
      for i in book:
           # get the object..
           obj=BookManager.getBookObj(i)['res']
           if obj is not None:
             t.book_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.book_set.all() ]
      return {'res':res,'status':'info','msg':'all book having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removePublication_Book(id,book):
    assert (isinstance(book,list)),"book must be a list type."
    try:
      res=PublicationManager.getPublicationObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in book:
          # get the object..
          obj=BookManager.getBookObj(i)['res']
          if obj is not None:
            t.book_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.book_set.all() ]
      return {'res':res,'status':'info','msg':'all book having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some book not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchPublication(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Publication Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Publication.objects.filter(Qstr)
      else:
        dd=Publication.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']+['id']
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

      return {'res':res,'status':'info','msg':'Publication search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Publication!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewPublication(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Publication.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Mini View Publication  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Publication!','sys_error':str(e)}


from .models import TOC
class TOCManager:
  @staticmethod
  def createTOC(name=None,): #Crete an Obj
    try:
      
      
      
      t = TOC(name=name,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New TOC got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create TOC:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getTOC(id,mv=None): # get Json
    try:
      t=TOC.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      if mv != None:
        #send Mini view only..
        include =[u'name', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'TOC returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive TOC:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getTOCObj(id): #get Obj
    try:
      t=TOC.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'TOC Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object TOC:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateTOC(id,name=None, ): #Update Obj
    try:
      res=TOCManager.getTOCObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'TOC Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update TOC:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteTOC(id): #Delete Obj
    try:
      d=TOC.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one TOC deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete TOC:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchTOC(name=None,page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=TOC.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'TOC search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search TOC:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getTOC_Book(id,mv=None):
    try:
       res=TOCManager.getTOCObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.book)]
       if mv:
          include =[u'name', 'id']
          res= [  t.book.values(*include) ]
       return {'res':res,'status':'info','msg':'all book for the TOC returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addTOC_Book(id,book):
    assert (isinstance(book,list)),"book must be a list type."
    try:
       res=TOCManager.getTOCObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in book:
           # get the object..
           obj=BookManager.getBookObj(i)['res']
           if obj is not None:
             t.book = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.book )]
       return {'res':res,'status':'info','msg':'all book having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeTOC_Book(id,book):
    assert (isinstance(book,list)),"book must be a list type."
    try:
       res=TOCManager.getTOCObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.book=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all book having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some book not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchTOC(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'TOC Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=TOC.objects.filter(Qstr)
      else:
        dd=TOC.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']+['id']
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

      return {'res':res,'status':'info','msg':'TOC search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search TOC!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewTOC(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=TOC.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Mini View TOC  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search TOC!','sys_error':str(e)}


from .models import Book
class BookManager:
  @staticmethod
  def createBook(name=None,authors=None,reg=None,publication=None,toc=None,tag1=None,tag2=None,mych=None,mych2=None,): #Crete an Obj
    try:
      if tag1 and not set(tag1).issubset(set([u'abc', u'def'])) : return {'res':None,'status':'error','msg':"tag1 must be either of [u'abc', u'def'] ",'sys_error':''};
      if mych and not set(mych).issubset(set([u'type1', u'type2', u'type3'])) : return {'res':None,'status':'error','msg':"mych must be either of [u'type1', u'type2', u'type3'] ",'sys_error':''};
      if mych2 and not set(mych2).issubset(set([u'type1', u'type2', u'type3'])) : return {'res':None,'status':'error','msg':"mych2 must be either of [u'type1', u'type2', u'type3'] ",'sys_error':''};
      
      
      
      if toc:
        toc_res = TOCManager.getTOCObj(id=toc)
        if toc_res['res'] is None:
          toc_res['help'] ='invalid toc id; any way this is optional..'
          return toc_res
        toc = toc_res['res']
      t = Book(name=name,reg=reg,toc=toc,tag1=tag1,tag2=tag2,mych=mych,mych2=mych2,)
      t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]
      t.save()
      if authors: BookManager.addBook_Author(t.id,authors,flush=True);
      if publication: BookManager.addBook_Publication(t.id,publication,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Book got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getBook(id,mv=None): # get Json
    try:
      t=Book.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        res['toc_desc'] = TOCManager.getTOC(id=res['toc'])['res'];
      if mv != None:
        #send Mini view only..
        include =[u'name', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'Book returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Book:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getBookObj(id): #get Obj
    try:
      t=Book.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Book Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Book:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateBook(id,name=None,authors=None,reg=None,publication=None,toc=None,tag1=None,tag2=None,mych=None,mych2=None, ): #Update Obj
    try:
      res=BookManager.getBookObj(id)
      if res['res'] is None: return res
      t=res['res']
      if tag1 and not set(tag1).issubset(set([u'abc', u'def'])) : return {'res':None,'status':'error','msg':"tag1 must be either of [u'abc', u'def'] ",'sys_error':''};
      if mych and not set(mych).issubset(set([u'type1', u'type2', u'type3'])) : return {'res':None,'status':'error','msg':"mych must be either of [u'type1', u'type2', u'type3'] ",'sys_error':''};
      if mych2 and not set(mych2).issubset(set([u'type1', u'type2', u'type3'])) : return {'res':None,'status':'error','msg':"mych2 must be either of [u'type1', u'type2', u'type3'] ",'sys_error':''};
      
      changes='';
      changes += '< name:'+ str(t.name) +' -> '+str( name)+' >'  if name is not None  else '' 
      changes += '< reg:'+ str(t.reg) +' -> '+str( reg)+' >'  if reg is not None  else '' 
      changes += '< toc:'+ str(t.toc) +' -> '+str( toc)+' >'  if toc is not None  else '' 
      changes += '< tag1:'+ str(t.tag1) +' -> '+str( tag1)+' >'  if tag1 is not None  else '' 
      changes += '< tag2:'+ str(t.tag2) +' -> '+str( tag2)+' >'  if tag2 is not None  else '' 
      changes += '< mych:'+ str(t.mych) +' -> '+str( mych)+' >'  if mych is not None  else '' 
      changes += '< mych2:'+ str(t.mych2) +' -> '+str( mych2)+' >'  if mych2 is not None  else '' 
      if changes: t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        
      
      if toc:
        toc_res = TOCManager.getTOCObj(id=toc)
        if toc_res['res'] is None:
          toc_res['help'] ='invalid toc id; any way this is optional..'
          return toc_res
        toc = toc_res['res']
      t.name = name if name is not None else t.name;t.reg = reg if reg is not None else t.reg;t.toc = toc if toc is not None else t.toc;t.tag1 = tag1 if tag1 is not None else t.tag1;t.tag2 = tag2 if tag2 is not None else t.tag2;t.mych = mych if mych is not None else t.mych;t.mych2 = mych2 if mych2 is not None else t.mych2;             
      t.save()
      if authors: BookManager.addBook_Author(t.id,authors,flush=True);
      if publication: BookManager.addBook_Publication(t.id,publication,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Book Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteBook(id): #Delete Obj
    try:
      d=Book.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Book deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Book:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchBook(name=None,authors=None,reg=None,publication=None,toc=None,tag1=None,tag2=None,mych=None,mych2=None,page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if authors is not None: Query['authors']=authors
      if reg is not None: Query['reg']=reg
      if publication is not None: Query['publication']=publication
      if toc is not None: Query['toc']=toc
      if tag1 is not None: Query['tag1']=tag1
      if tag2 is not None: Query['tag2']=tag2
      if mych is not None: Query['mych']=mych
      if mych2 is not None: Query['mych2']=mych2 #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Book.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getBook_Author(id,mv=None):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.authors.all() ]
       if mv:
          include =[u'name', 'id']
          res= [  dict_reduce(_r,include) for _r in res ]

       return {'res':res,'status':'info','msg':'all authors for the Book returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get authors:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addBook_Author(id,authors,flush=False):
    assert (isinstance(authors,list)),"authors must be a list type."
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.authors.clear()
       for i in authors:
           # get the object..
           obj=AuthorManager.getAuthorObj(i)['res']
           if obj is not None:
             t.authors.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.authors.all() ]
       return {'res':res,'status':'info','msg':'all authors having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get authors:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeBook_Author(id,authors):
    assert (isinstance(authors,list)),"authors must be a list type."
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in authors:
           # get the object..
           obj=AuthorManager.getAuthorObj(i)['res']
           if obj is not None:
              t.authors.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.authors.all() ]
       return {'res':res,'status':'info','msg':'all authors having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some authors not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getBook_Publication(id,mv=None):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.publication.all() ]
       if mv:
          include =[u'name', 'id']
          res= [  dict_reduce(_r,include) for _r in res ]

       return {'res':res,'status':'info','msg':'all publication for the Book returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get publication:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addBook_Publication(id,publication,flush=False):
    assert (isinstance(publication,list)),"publication must be a list type."
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.publication.clear()
       for i in publication:
           # get the object..
           obj=PublicationManager.getPublicationObj(i)['res']
           if obj is not None:
             t.publication.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.publication.all() ]
       return {'res':res,'status':'info','msg':'all publication having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get publication:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeBook_Publication(id,publication):
    assert (isinstance(publication,list)),"publication must be a list type."
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in publication:
           # get the object..
           obj=PublicationManager.getPublicationObj(i)['res']
           if obj is not None:
              t.publication.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.publication.all() ]
       return {'res':res,'status':'info','msg':'all publication having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some publication not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getBook_TOC(id,mv=None):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.toc)]
       if mv:
          include =[u'name', 'id']
          res= [  t.toc.values(*include) ]
       return {'res':res,'status':'info','msg':'all toc for the Book returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get toc:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addBook_TOC(id,toc):
    assert (isinstance(toc,list)),"toc must be a list type."
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in toc:
           # get the object..
           obj=TOCManager.getTOCObj(i)['res']
           if obj is not None:
             t.toc = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.toc )]
       return {'res':res,'status':'info','msg':'all toc having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get toc:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeBook_TOC(id,toc):
    assert (isinstance(toc,list)),"toc must be a list type."
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.toc=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all toc having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some toc not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def appendListBook(id,tag1=[],tag2=[],):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1+tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2+tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}

  @staticmethod
  def removeListBook(id,tag1=[],tag2=[],):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1)-set(tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2)-set(tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListBook(tag1=[],tag2=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag1:Query['tag1__contains']= x
      for x in tag2:Query['tag2__contains']= x # Autogen
      include =[u'name', 'id']
      dd=Book.objects.filter(**Query).values(*include)
      
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

      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
  



  @staticmethod
  def appendListBook(id,tag1=[],tag2=[],):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1+tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2+tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}

  @staticmethod
  def removeListBook(id,tag1=[],tag2=[],):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1)-set(tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2)-set(tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListBook(tag1=[],tag2=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag1:Query['tag1__contains']= x
      for x in tag2:Query['tag2__contains']= x # Autogen
      include =[u'name', 'id']
      dd=Book.objects.filter(**Query).values(*include)
      
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

      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def advSearchBook(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Book Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Book.objects.filter(Qstr)
      else:
        dd=Book.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']+['id']
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

      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewBook(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Book.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Mini View Book  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}


  #Advance search is Implemented here..
  @staticmethod
  def getBook_quick_search(q,page=None,limit=None):
    try:
      res = None
      include =['id','name']
      dd=Book.objects.filter(name__startswith=q).values(*include)
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page)      
      res = list(dd.object_list)
      if not res: return {'res':res,'status':'info','msg':'Nothing match with your query'} 
      return {'res':res,'status':'success','msg':'Book match with your query'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}

