import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .api import AuthorManager
@csrf_exempt
def ajax_Author(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name=request.GET.get('name',None);reg=request.GET.get('reg',None);history=request.GET.get('history',None);tag1=request.GET.get('tag1',None);tag2=request.GET.get('tag2',None);
    # if Id is null, get the perticular Author or it's a search request
    if id is not None: 
      res= AuthorManager.getAuthor(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= AuthorManager.searchAuthor(name=name,reg=reg,history=history,tag1=tag1,tag2=tag2,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name=request.POST.get('name',None);reg=request.POST.get('reg',None);history=request.POST.get('history',None);tag1=request.POST.get('tag1',None);tag2=request.POST.get('tag2',None);
    # Update request if id is not null. 
    if id is not None: 
      res=AuthorManager.updateAuthor(id=id,name=name,reg=reg,history=history,tag1=tag1,tag2=tag2,)
    else:
      # This is new entry request...
      res=AuthorManager.createAuthor(name=name,reg=reg,history=history,tag1=tag1,tag2=tag2,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =AuthorManager.deleteAuthor(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


from .api import PublicationManager
@csrf_exempt
def ajax_Publication(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name=request.GET.get('name',None);accid=request.GET.get('accid',None);
    # if Id is null, get the perticular Publication or it's a search request
    if id is not None: 
      res= PublicationManager.getPublication(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= PublicationManager.searchPublication(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name=request.POST.get('name',None);accid=request.POST.get('accid',None);
    # Update request if id is not null. 
    if id is not None: 
      res=PublicationManager.updatePublication(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=PublicationManager.createPublication(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =PublicationManager.deletePublication(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


from .api import BookManager
@csrf_exempt
def ajax_Book(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name=request.GET.get('name',None);author=request.GET.get('author',None);
    # if Id is null, get the perticular Book or it's a search request
    if id is not None: 
      res= BookManager.getBook(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= BookManager.searchBook(name=name,author=author,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name=request.POST.get('name',None);author=request.POST.get('author',None);
    # Update request if id is not null. 
    if id is not None: 
      res=BookManager.updateBook(id=id,name=name,author=author,)
    else:
      # This is new entry request...
      res=BookManager.createBook(name=name,author=author,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =BookManager.deleteBook(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Book_Author(request,id=None):
  res=None
  #If the request is coming for get to all author
  if request.method == 'GET':
      res= BookManager.getAuthor(id=id)

  #This is the implementation for POST request to add or delete author
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    try:
      author_list=eval(request.POST.get('author_list',None))
    except:
      return HttpResponse('bad input for author_list')
    # Update request if id is not null.
    if action == 'ADD':
      res=BookManager.addAuthor(id=id,author_list = author_list)
    else:
      # do a delete action
      res=BookManager.removeAuthor(id=id,author_list = author_list)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


