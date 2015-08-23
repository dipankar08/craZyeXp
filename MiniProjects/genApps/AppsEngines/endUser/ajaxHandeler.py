import pdb
from common import *
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from stubs import authenticate # You need to define a decorator to do authenticate.

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
  


from .api import UserManager

@csrf_exempt
@authenticate
def ajax_User(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    mv=request.GET.get('mv',None) # this is an Adding to get Mini View.. 
    uname= request.GET.get('uname') if request.GET.get('uname','').strip() else None;fname= request.GET.get('fname') if request.GET.get('fname','').strip() else None;lname= request.GET.get('lname') if request.GET.get('lname','').strip() else None;passwd= request.GET.get('passwd') if request.GET.get('passwd','').strip() else None;email= request.GET.get('email') if request.GET.get('email','').strip() else None;dob= request.GET.get('dob') if request.GET.get('dob','').strip() else None;desc= request.GET.get('desc') if request.GET.get('desc','').strip() else None;pic_url= request.GET.get('pic_url') if request.GET.get('pic_url','').strip() else None;address= request.GET.get('address') if request.GET.get('address','').strip() else None;social_id= request.GET.get('social_id') if request.GET.get('social_id','').strip() else None;payload= request.GET.get('payload') if request.GET.get('payload','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      uname = str(uname) if( uname) else uname ;fname = str(fname) if( fname) else fname ;lname = str(lname) if( lname) else lname ;passwd = str(passwd) if( passwd) else passwd ;email = str(email) if( email) else email ;dob = date(dob) if( dob) else dob ;desc = str(desc) if( desc) else desc ;pic_url = str(pic_url) if( pic_url) else pic_url ;address = str(address) if( address) else address ;social_id = dict(social_id) if( social_id) else social_id ;payload = dict(payload) if( payload) else payload ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular User or it's a search request
    if id is not None: 
      res= UserManager.getUser(id,mv=mv)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= UserManager.searchUser(uname=uname,fname=fname,lname=lname,passwd=passwd,email=email,dob=dob,desc=desc,pic_url=pic_url,address=address,social_id=social_id,payload=payload,id=id,page=page,limit=limit,mv=mv  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    uname= request.POST.get('uname') if request.POST.get('uname','').strip() else None;fname= request.POST.get('fname') if request.POST.get('fname','').strip() else None;lname= request.POST.get('lname') if request.POST.get('lname','').strip() else None;passwd= request.POST.get('passwd') if request.POST.get('passwd','').strip() else None;email= request.POST.get('email') if request.POST.get('email','').strip() else None;dob= request.POST.get('dob') if request.POST.get('dob','').strip() else None;desc= request.POST.get('desc') if request.POST.get('desc','').strip() else None;pic_url= request.POST.get('pic_url') if request.POST.get('pic_url','').strip() else None;address= request.POST.get('address') if request.POST.get('address','').strip() else None;social_id= request.POST.get('social_id') if request.POST.get('social_id','').strip() else None;payload= request.POST.get('payload') if request.POST.get('payload','').strip() else None;   
    uname=uname if uname else 'newUser' ;fname=fname if fname else None ;lname=lname if lname else None ;passwd=passwd if passwd else None ;email=email if email else None ;dob=dob if dob else None ;desc=desc if desc else None ;pic_url=pic_url if pic_url else None ;address=address if address else None ;social_id=social_id if social_id else {'google':0,'facebook':0,'github':0,'linkedin':0} ;payload=payload if payload else {'allid':0,'recent_id':0} ;    
    #data Must be Normalized to required DataType..
    try:
      uname = str(uname) if( uname) else uname ;fname = str(fname) if( fname) else fname ;lname = str(lname) if( lname) else lname ;passwd = str(passwd) if( passwd) else passwd ;email = str(email) if( email) else email ;dob = date(dob) if( dob) else dob ;desc = str(desc) if( desc) else desc ;pic_url = str(pic_url) if( pic_url) else pic_url ;address = str(address) if( address) else address ;social_id = dict(social_id) if( social_id) else social_id ;payload = dict(payload) if( payload) else payload ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=UserManager.updateUser(id=id,uname=uname,fname=fname,lname=lname,passwd=passwd,email=email,dob=dob,desc=desc,pic_url=pic_url,address=address,social_id=social_id,payload=payload,)
    else:
      # This is new entry request...
      res=UserManager.createUser(uname=uname,fname=fname,lname=lname,passwd=passwd,email=email,dob=dob,desc=desc,pic_url=pic_url,address=address,social_id=social_id,payload=payload,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =UserManager.deleteUser(id)
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
@authenticate
def ajax_User_asearch(request): # We support POST only .
  res=None
  # This is basically a search by a tag or list items with given arguments
  if request.method == 'GET':
    return AutoHttpResponse(501)
  # This is basically a append to a list with given arguments
  elif request.method == 'POST':
    id=request.POST.get('id',None)    
    try: 
      #uname = parseTriple(request.POST.get('uname',None));fname = parseTriple(request.POST.get('fname',None));lname = parseTriple(request.POST.get('lname',None));passwd = parseTriple(request.POST.get('passwd',None));email = parseTriple(request.POST.get('email',None));dob = parseTriple(request.POST.get('dob',None));desc = parseTriple(request.POST.get('desc',None));pic_url = parseTriple(request.POST.get('pic_url',None));address = parseTriple(request.POST.get('address',None));social_id = parseTriple(request.POST.get('social_id',None));payload = parseTriple(request.POST.get('payload',None));
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
       res = UserManager.advSearchUser(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
@authenticate
def ajax_User_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = UserManager.minViewUser(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


@csrf_exempt
@authenticate
def ajax_User_quick_search(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    q=request.GET.get('q',None)
    if not q:
      return AutoHttpResponse(200,'you must a input called ?q=abcd') 
    res = UserManager.getUser_quick_search(q=q,page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  

