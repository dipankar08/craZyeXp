from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q

from .models import Book
class BookManager:
  @staticmethod
  def createBook(name,icbn,toc,author,publication,): #Crete an Obj
    try:
      
      t = Book(name=name,icbn=icbn,toc=toc,author=author,publication=publication,)
      t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Book got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Book','sys_error':str(e)}

  @staticmethod
  def getBook(id): # get Json
    try:
      t=Book.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
      return {'res':res,'status':'info','msg':'Book returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Book','sys_error':str(e)}

  @staticmethod
  def getBookObj(id): #get Obj
    try:
      t=Book.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Book Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Book','sys_error':str(e)}

  @staticmethod
  def updateBook(id,name,icbn,toc,author,publication, ): #Update Obj
    try:
      res=BookManager.getBookObj(id)
      if res['res'] is None: return res
      t=res['res']
      changes='';changes +=str('update name:'+ str(t.name) +' to '+str( name)+' ;')  if name is not None  else '' ;changes +=str('update icbn:'+ str(t.icbn) +' to '+str( icbn)+' ;')  if icbn is not None  else '' ;changes +=str('update toc:'+ str(t.toc) +' to '+str( toc)+' ;')  if toc is not None  else '' ;changes +=str('update author:'+ str(t.author) +' to '+str( author)+' ;')  if author is not None  else '' ;changes +=str('update publication:'+ str(t.publication) +' to '+str( publication)+' ;')  if publication is not None  else '' ;t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
      t.name = name if name is not None else t.name;t.icbn = icbn if icbn is not None else t.icbn;t.toc = toc if toc is not None else t.toc;t.author = author if author is not None else t.author;t.publication = publication if publication is not None else t.publication;      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Book Updated'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to update Book','sys_error':str(e)}

  @staticmethod
  def deleteBook(id): #Delete Obj
    try:
      d=Book.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Book deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Book!','sys_error':str(e)}


  @staticmethod
  def searchBook(name,icbn,toc,author,publication,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if icbn is not None: Query['icbn']=icbn
      if toc is not None: Query['toc']=toc
      if author is not None: Query['author']=author
      if publication is not None: Query['publication']=publication #if state is not None: Query['state_contains']=state
      d=Book.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
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
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListBook(tag1=[],tag2=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag1:Query['tag1__contains']= x
      for x in tag2:Query['tag2__contains']= x # Autogen
      d=Book.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
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
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListBook(tag1=[],tag2=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag1:Query['tag1__contains']= x
      for x in tag2:Query['tag2__contains']= x # Autogen
      d=Book.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def advSearchBook(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    import pdb
    #pdb.set_trace()
    try:
      Qstr = query_str
      print "===>ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except:
          print "ERROR: something problem in Q query, try out eval("+Qstr+") .."
      if Qstr:
        d=Book.objects.filter(Qstr)
      else:
        d=Book.objects.filter()
      #Oder_by Here.
      if orderBy:
        d= d.order_by(*orderBy)        
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)     
        
      #Selecting fields.
      if include:
        res = list(d.values(*include))
      else:
        res=[model_to_dict(u) for u in d]
        #res = d.values() # Dont RUN this .
        
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
  


