from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

from .models import Author
class AuthorManager:
  @staticmethod
  def createAuthor(name,reg,history,tag1,tag2,): #Crete an Obj
    try:
      
      t = Author(name=name,reg=reg,history=history,tag1=tag1,tag2=tag2,)
      t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Author got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Author','sys_error':str(e)}

  @staticmethod
  def getAuthor(id): # get Json
    try:
      t=Author.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
      return {'res':res,'status':'info','msg':'Author returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Author','sys_error':str(e)}

  @staticmethod
  def getAuthorObj(id): #get Obj
    try:
      t=Author.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Author Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Author','sys_error':str(e)}

  @staticmethod
  def updateAuthor(id,name,reg,history,tag1,tag2, ): #Update Obj
    try:
      res=AuthorManager.getAuthorObj(id)
      if res['res'] is None: return res
      t=res['res']
      changes='';changes +=str('update name:'+ str(t.name) +' to '+str( name)+' ;')  if name is not None  else '' ;changes +=str('update reg:'+ str(t.reg) +' to '+str( reg)+' ;')  if reg is not None  else '' ;changes +=str('update history:'+ str(t.history) +' to '+str( history)+' ;')  if history is not None  else '' ;changes +=str('update tag1:'+ str(t.tag1) +' to '+str( tag1)+' ;')  if tag1 is not None  else '' ;changes +=str('update tag2:'+ str(t.tag2) +' to '+str( tag2)+' ;')  if tag2 is not None  else '' ;t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
      t.name = name if name is not None else t.name;t.reg = reg if reg is not None else t.reg;t.history = history if history is not None else t.history;t.tag1 = tag1 if tag1 is not None else t.tag1;t.tag2 = tag2 if tag2 is not None else t.tag2;      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Author Updated'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to update Author','sys_error':str(e)}

  @staticmethod
  def deleteAuthor(id): #Delete Obj
    try:
      d=Author.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Author deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Author!','sys_error':str(e)}


  @staticmethod
  def searchAuthor(name,reg,history,tag1,tag2,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if reg is not None: Query['reg']=reg
      if history is not None: Query['history']=history
      if tag1 is not None: Query['tag1']=tag1
      if tag2 is not None: Query['tag2']=tag2 #if state is not None: Query['state_contains']=state
      d=Author.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Author search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Author!','sys_error':str(e)}

  

  @staticmethod
  def appendListAuthor(id,tag1=[],tag2=[],):
    try:
       res=AuthorManager.getAuthorObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1+tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2+tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}

  @staticmethod
  def removeListAuthor(id,tag1=[],tag2=[],):
    try:
       res=AuthorManager.getAuthorObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1)-set(tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2)-set(tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListAuthor(tag1=[],tag2=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag1:Query['tag1__contains']= x
      for x in tag2:Query['tag2__contains']= x # Autogen
      d=Author.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Author search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Author!','sys_error':str(e)}
  



  @staticmethod
  def appendListAuthor(id,tag1=[],tag2=[],):
    try:
       res=AuthorManager.getAuthorObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1+tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2+tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}

  @staticmethod
  def removeListAuthor(id,tag1=[],tag2=[],):
    try:
       res=AuthorManager.getAuthorObj(id)
       if res['res'] is None: return res
       t=res['res']
       t.tag1 = sorted(list(set(t.tag1)-set(tag1))) if tag1 is not None else t.tag1;t.tag2 = sorted(list(set(t.tag2)-set(tag2))) if tag2 is not None else t.tag2;
       t.save()
       res= model_to_dict(t)
       return {'res':res,'status':'info','msg':'tag added'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to add tags ','sys_error':str(e)}
      
  @staticmethod
  def searchListAuthor(tag1=[],tag2=[],page=None,limit=None):
    try:
      Query={}
      
      for x in tag1:Query['tag1__contains']= x
      for x in tag2:Query['tag2__contains']= x # Autogen
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
  def createPublication(name,accid,): #Crete an Obj
    try:
      
      t = Publication(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Publication got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Publication','sys_error':str(e)}

  @staticmethod
  def getPublication(id): # get Json
    try:
      t=Publication.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
      return {'res':res,'status':'info','msg':'Publication returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Publication','sys_error':str(e)}

  @staticmethod
  def getPublicationObj(id): #get Obj
    try:
      t=Publication.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Publication Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Publication','sys_error':str(e)}

  @staticmethod
  def updatePublication(id,name,accid, ): #Update Obj
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
  def deletePublication(id): #Delete Obj
    try:
      d=Publication.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Publication deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Publication!','sys_error':str(e)}


  @staticmethod
  def searchPublication(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
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
  def createBook(name,author,): #Crete an Obj
    try:
      
      publications_res = PublicationManager.getPublicationObj(id=publications)
      if publications_res['res'] is None: return publications_res
      publications = publications_res['res']
      t = Book(name=name,author=author,)
      
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
        res['publications_desc'] = PublicationManager.getPublication(id=res['publications'])['res'];
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
  def updateBook(id,name,author, ): #Update Obj
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
  def deleteBook(id): #Delete Obj
    try:
      d=Book.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Book deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Book!','sys_error':str(e)}


  @staticmethod
  def searchBook(name,author,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if author is not None: Query['author']=author #if state is not None: Query['state_contains']=state
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
  def getAuthor(id):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.author.all() ]
       return {'res':res,'status':'info','msg':'all author for the Book returned.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to get author ','sys_error':str(e)}

  @staticmethod
  def addAuthor(id,author_list):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if isinstance(author_list,list):
         for i in author_list:
           # get the object..
           obj=AuthorManager.getAuthorObj(i)['res']
           if obj is not None:
             t.author.add(obj)
             loc_msg+= str(obj.id)+','
       else:
         obj=AuthorManager.getAuthorObj(author_list)['res']
         if obj is not None:
            t.author.add(obj)
            loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.author.all() ]
       return {'res':res,'status':'info','msg':'all author having id <'+loc_msg+'> got added!'}
    except Exception,e :
       return {'res':None,'status':'error','msg':'Not able to get author ','sys_error':str(e)}

  @staticmethod
  def removeAuthor(id,author_list):
    try:
       res=BookManager.getBookObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       if isinstance(author_list,list):
         for i in author_list:
           # get the object..
           obj=AuthorManager.getAuthorObj(i)['res']
           if obj is not None:
              t.author.remove(obj)
              loc_msg+= str(obj.id)+','
       else:
         obj=AuthorManager.getAuthorObj(author_list)['res']
         if obj is not None:
            t.author.remove(obj)
            loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.author.all() ]
       return {'res':res,'status':'info','msg':'all author having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       return {'res':None,'status':'error','msg':'Some author not able to removed! ','sys_error':str(e)}


