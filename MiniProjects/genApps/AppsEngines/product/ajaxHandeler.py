import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#Helper function
def AutoHttpResponse(code=200,res=None):
  if res and isinstance(res, dict):
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
  if code == 400:  
    res = {'res':None,'status':'error','msg':'400(Bad Request): '+str(res)} if res else {'res':None,'status':'error','msg':'400(Bad Request): required /invalid Paranmeter passed.'}
  if code == 501:  
    res = {'res':None,'status':'error','msg':'501(Not Implemented): '+str(res)} if res else {'res':None,'status':'error','msg':'501(Not Implemented)'}
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json') 

#We support "[1,2,3]" or 'aa,bb,cc' or 'aa bb cc' to [1,2,3] Split Over , space or eval 
def str2List(s):
  try:
    if '[' in s:
      return eval(s)
    if ',' in s:
      return s.split(',')
    else:
      return s.split(' ')
  except:
    print 'Error: eval Error: We support "[1,2,3]" or "aa,bb,cc" or "aa bb cc" to [1,2,3] Split Over , space or eval '
    return []
  
#Helper Function To Perse Advance Serach parmas
#Input : <a:b:c> =>(a,b,c) >
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
  


from .api import BookManager
@csrf_exempt
def ajax_Book(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name=request.GET.get('name',None);icbn=request.GET.get('icbn',None);toc=request.GET.get('toc',None);author=request.GET.get('author',None);publication=request.GET.get('publication',None);
    # if Id is null, get the perticular Book or it's a search request
    if id is not None: 
      res= BookManager.getBook(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= BookManager.searchBook(name=name,icbn=icbn,toc=toc,author=author,publication=publication,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name=request.POST.get('name',None);icbn=request.POST.get('icbn',None);toc=request.POST.get('toc',None);author=request.POST.get('author',None);publication=request.POST.get('publication',None);
    # Update request if id is not null. 
    if id is not None: 
      res=BookManager.updateBook(id=id,name=name,icbn=icbn,toc=toc,author=author,publication=publication,)
    else:
      # This is new entry request...
      res=BookManager.createBook(name=name,icbn=icbn,toc=toc,author=author,publication=publication,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =BookManager.deleteBook(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Book_list(request,id=None,):
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
      tag1 = eval(request.POST.get('tag1','[]'));tag2 = eval(request.POST.get('tag2','[]'));
      if action == 'APPEND':
        res = BookManager.appendListBook(id,tag1=tag1,tag2=tag2,)
      elif action == 'REMOVE':
        res = BookManager.removeListBook(id,tag1=tag1,tag2=tag2,)
      elif action == 'SEARCH':
        res = BookManager.searchListBook(tag1=tag1,tag2=tag2,)
    except:
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Book_asearch(request): # We support POST only .
  res=None
  #import pdb
  #pdb.set_trace()
  # This is basically a search by a tag or list items with given arguments
  if request.method == 'GET':
    return AutoHttpResponse(501)
  # This is basically a append to a list with given arguments
  elif request.method == 'POST':
    id=request.POST.get('id',None)    
    try: 
      #name = parseTriple(request.POST.get('name',None));icbn = parseTriple(request.POST.get('icbn',None));toc = parseTriple(request.POST.get('toc',None));author = parseTriple(request.POST.get('author',None));publication = parseTriple(request.POST.get('publication',None));
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
          if v:
              if v[1] in ['in', 'notin']:
                Qstr += v[0]+' Q('+key+'__'+v[1]+' = '+str(v[2])+') ' # this is a list in case of in/notin
              else:
                Qstr += v[0]+' Q('+key+'__'+v[1]+' = "'+str(v[2])+'") ' # else the v[2] will be String
        else:
          for v in value:
            v = parseTriple(v)
            if v:
              if v[1] in ['in', 'notin']:
                Qstr += v[0]+' Q('+key+'__'+v[1]+' = '+str(v[2])+') ' # this is a list in case of in/notin
              else:
                Qstr += v[0]+' Q('+key+'__'+v[1]+' = "'+str(v[2])+'") ' # else the v[2] will be String
      Qstr = Qstr[2:]
          
      
    except:
	    return AutoHttpResponse(400,'Wrong Pentameter format.') 	   
    
    try:
       res = BookManager.advSearchBook(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)

