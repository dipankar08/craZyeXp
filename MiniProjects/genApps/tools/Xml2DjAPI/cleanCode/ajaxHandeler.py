import pdb
from common import *
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
  


from .api import CodeManager
@csrf_exempt
def ajax_Code(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    mv=request.GET.get('mv',None) # this is an Adding to get Mini View.. 
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;short_desc= request.GET.get('short_desc') if request.GET.get('short_desc','').strip() else None;full_desc= request.GET.get('full_desc') if request.GET.get('full_desc','').strip() else None;main= request.GET.get('main') if request.GET.get('main','').strip() else None;func= request.GET.get('func') if request.GET.get('func','').strip() else None;input= request.GET.get('input') if request.GET.get('input','').strip() else None;solution= request.GET.get('solution') if request.GET.get('solution','').strip() else None;level= request.GET.get('level') if request.GET.get('level','').strip() else None;language= request.GET.get('language') if request.GET.get('language','').strip() else None;compilation= request.GET.get('compilation') if request.GET.get('compilation','').strip() else None;tag= request.GET.get('tag') if request.GET.get('tag','').strip() else None;topic= request.GET.get('topic') if request.GET.get('topic','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;short_desc = str(short_desc) if( short_desc) else short_desc ;full_desc = str(full_desc) if( full_desc) else full_desc ;main = str(main) if( main) else main ;func = str(func) if( func) else func ;input = str(input) if( input) else input ;solution = str(solution) if( solution) else solution ;level = str(level) if( level) else level ;language = str(language) if( language) else language ;compilation = str(compilation) if( compilation) else compilation ;tag = str2List(tag) if( tag) else tag ;topic = str2List(topic) if( topic) else topic ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Code or it's a search request
    if id is not None: 
      res= CodeManager.getCode(id,mv=mv)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= CodeManager.searchCode(name=name,short_desc=short_desc,full_desc=full_desc,main=main,func=func,input=input,solution=solution,level=level,language=language,compilation=compilation,tag=tag,topic=topic,id=id,page=page,limit=limit,mv=mv  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;short_desc= request.POST.get('short_desc') if request.POST.get('short_desc','').strip() else None;full_desc= request.POST.get('full_desc') if request.POST.get('full_desc','').strip() else None;main= request.POST.get('main') if request.POST.get('main','').strip() else None;func= request.POST.get('func') if request.POST.get('func','').strip() else None;input= request.POST.get('input') if request.POST.get('input','').strip() else None;solution= request.POST.get('solution') if request.POST.get('solution','').strip() else None;level= request.POST.get('level') if request.POST.get('level','').strip() else None;language= request.POST.get('language') if request.POST.get('language','').strip() else None;compilation= request.POST.get('compilation') if request.POST.get('compilation','').strip() else None;tag= request.POST.get('tag') if request.POST.get('tag','').strip() else None;topic= request.POST.get('topic') if request.POST.get('topic','').strip() else None;   
    name=name if name else None ;short_desc=short_desc if short_desc else None ;full_desc=full_desc if full_desc else None ;main=main if main else None ;func=func if func else None ;input=input if input else None ;solution=solution if solution else None ;level=level if level else None ;language=language if language else None ;compilation=compilation if compilation else None ;tag=tag if tag else None ;topic=topic if topic else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;short_desc = str(short_desc) if( short_desc) else short_desc ;full_desc = str(full_desc) if( full_desc) else full_desc ;main = str(main) if( main) else main ;func = str(func) if( func) else func ;input = str(input) if( input) else input ;solution = str(solution) if( solution) else solution ;level = str(level) if( level) else level ;language = str(language) if( language) else language ;compilation = str(compilation) if( compilation) else compilation ;tag = str2List(tag) if( tag) else tag ;topic = str2List(topic) if( topic) else topic ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=CodeManager.updateCode(id=id,name=name,short_desc=short_desc,full_desc=full_desc,main=main,func=func,input=input,solution=solution,level=level,language=language,compilation=compilation,tag=tag,topic=topic,)
    else:
      # This is new entry request...
      res=CodeManager.createCode(name=name,short_desc=short_desc,full_desc=full_desc,main=main,func=func,input=input,solution=solution,level=level,language=language,compilation=compilation,tag=tag,topic=topic,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =CodeManager.deleteCode(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Code_list(request,id=None,):
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
      tag = eval(request.POST.get('tag','[]'));topic = eval(request.POST.get('topic','[]'));
      if action == 'APPEND':
        res = CodeManager.appendListCode(id,tag=tag,topic=topic,)
      elif action == 'REMOVE':
        res = CodeManager.removeListCode(id,tag=tag,topic=topic,)
      elif action == 'SEARCH':
        res = CodeManager.searchListCode(tag=tag,topic=topic,)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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
def ajax_Code_asearch(request): # We support POST only .
  res=None
  # This is basically a search by a tag or list items with given arguments
  if request.method == 'GET':
    return AutoHttpResponse(501)
  # This is basically a append to a list with given arguments
  elif request.method == 'POST':
    id=request.POST.get('id',None)    
    try: 
      #name = parseTriple(request.POST.get('name',None));short_desc = parseTriple(request.POST.get('short_desc',None));full_desc = parseTriple(request.POST.get('full_desc',None));main = parseTriple(request.POST.get('main',None));func = parseTriple(request.POST.get('func',None));input = parseTriple(request.POST.get('input',None));solution = parseTriple(request.POST.get('solution',None));level = parseTriple(request.POST.get('level',None));language = parseTriple(request.POST.get('language',None));compilation = parseTriple(request.POST.get('compilation',None));tag = parseTriple(request.POST.get('tag',None));topic = parseTriple(request.POST.get('topic',None));
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
       res = CodeManager.advSearchCode(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Code_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = CodeManager.minViewCode(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


@csrf_exempt
def ajax_Code_quick_search(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    q=request.GET.get('q',None)
    if not q:
      return AutoHttpResponse(200,'you must a input called ?q=abcd') 
    res = CodeManager.getCode_quick_search(q=q,page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  

