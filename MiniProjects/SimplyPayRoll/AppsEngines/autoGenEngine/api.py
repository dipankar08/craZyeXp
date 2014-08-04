from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from .models import Author
class AuthorManager:
  @staticmethod
  def createAuthor(name,reg,history,tags,):
    try:
      
      new = Author(name=name,reg=reg,history=history,tags=tags,)
      new.save()
      return {'res':model_to_dict(new),'status':'info','msg':'New Author got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Author','sys_error':str(e)}
  @staticmethod
  def getAuthor(id):
    try:
      t=Author.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
      return {'res':res,'status':'info','msg':'Author returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Author','sys_error':str(e)}
  @staticmethod
  def getAuthorObj(id):
    try:
      t=Author.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Author Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Author','sys_error':str(e)}
  @staticmethod
  def updateAuthor(id,name,reg,history,tags, ):
    try:
      res=AuthorManager.getAuthorObj(id)
      if res['res'] is None: return res
      t=res['res']
      t.name = name if name is not None else t.name;t.reg = reg if reg is not None else t.reg;t.history = history if history is not None else t.history;t.tags = tags if tags is not None else t.tags;
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Author Updated'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to update Author','sys_error':str(e)}
  @staticmethod
  def deleteAuthor(id):
    try:
      d=Author.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Author deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Author!','sys_error':str(e)}
  @staticmethod
  def searchAuthor(name,reg,history,tags,page=None,limit=None,id=None):
    try:
      Query={}
      if id is not None: Query['id']=id
  
      if name is not None: Query['name']=name;
      if reg is not None: Query['reg']=reg;
      if history is not None: Query['history']=history;
      if tags is not None: Query['tags']=tags; #if state is not None: Query['state_contains']=state
      d=Author.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Author search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Author!','sys_error':str(e)}
   
from .models import Publication
class PublicationManager:
  @staticmethod
  def createPublication(name,accid,):
    try:
      
      new = Publication(name=name,accid=accid,)
      new.save()
      return {'res':model_to_dict(new),'status':'info','msg':'New Publication got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Publication','sys_error':str(e)}
  @staticmethod
  def getPublication(id):
    try:
      t=Publication.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
      return {'res':res,'status':'info','msg':'Publication returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Publication','sys_error':str(e)}
  @staticmethod
  def getPublicationObj(id):
    try:
      t=Publication.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Publication Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Publication','sys_error':str(e)}
  @staticmethod
  def updatePublication(id,name,accid, ):
    try:
      res=PublicationManager.getPublicationObj(id)
      if res['res'] is None: return res
      t=res['res']
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Publication Updated'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to update Publication','sys_error':str(e)}
  @staticmethod
  def deletePublication(id):
    try:
      d=Publication.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Publication deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Publication!','sys_error':str(e)}
  @staticmethod
  def searchPublication(name,accid,page=None,limit=None,id=None):
    try:
      Query={}
      if id is not None: Query['id']=id
  
      if name is not None: Query['name']=name;
      if accid is not None: Query['accid']=accid; #if state is not None: Query['state_contains']=state
      d=Publication.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Publication search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Publication!','sys_error':str(e)}
   
from .models import Book
class BookManager:
  @staticmethod
  def createBook(name,author,):
    try:
      
      author_res = AuthorManager.getAuthorObj(id=author)
      if author_res['res'] is None: return author_res
      author = author_res['res']
      new = Book(name=name,author=author,)
      new.save()
      return {'res':model_to_dict(new),'status':'info','msg':'New Book got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Book','sys_error':str(e)}
  @staticmethod
  def getBook(id):
    try:
      t=Book.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['author_desc'] = AuthorManager.getAuthor(id=res['author'])['res'];
      return {'res':res,'status':'info','msg':'Book returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Book','sys_error':str(e)}
  @staticmethod
  def getBookObj(id):
    try:
      t=Book.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Book Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Book','sys_error':str(e)}
  @staticmethod
  def updateBook(id,name,author, ):
    try:
      res=BookManager.getBookObj(id)
      if res['res'] is None: return res
      t=res['res']
      t.name = name if name is not None else t.name;t.author = author if author is not None else t.author;
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Book Updated'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to update Book','sys_error':str(e)}
  @staticmethod
  def deleteBook(id):
    try:
      d=Book.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Book deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Book!','sys_error':str(e)}
  @staticmethod
  def searchBook(name,author,page=None,limit=None,id=None):
    try:
      Query={}
      if id is not None: Query['id']=id
  
      if name is not None: Query['name']=name;
      if author is not None: Query['author']=author; #if state is not None: Query['state_contains']=state
      d=Book.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
   
