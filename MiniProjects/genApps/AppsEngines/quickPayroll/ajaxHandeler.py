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
  


from .api import PayRollManager
@csrf_exempt
def ajax_PayRoll(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    mv=request.GET.get('mv',None) # this is an Adding to get Mini View.. 
    type= request.GET.get('type') if request.GET.get('type','').strip() else None;month= request.GET.get('month') if request.GET.get('month','').strip() else None;year= request.GET.get('year') if request.GET.get('year','').strip() else None;source= request.GET.get('source') if request.GET.get('source','').strip() else None;category= request.GET.get('category') if request.GET.get('category','').strip() else None;subcategory= request.GET.get('subcategory') if request.GET.get('subcategory','').strip() else None;amount= request.GET.get('amount') if request.GET.get('amount','').strip() else None;actualamount= request.GET.get('actualamount') if request.GET.get('actualamount','').strip() else None;breakup= request.GET.get('breakup') if request.GET.get('breakup','').strip() else None;comment= request.GET.get('comment') if request.GET.get('comment','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      type = str2List(type) if( type) else type ;month = str2List(month) if( month) else month ;year = str2List(year) if( year) else year ;source = str2List(source) if( source) else source ;category = str2List(category) if( category) else category ;subcategory = str(subcategory) if( subcategory) else subcategory ;amount = int(amount) if( amount) else amount ;actualamount = int(actualamount) if( actualamount) else actualamount ;breakup = dict(breakup) if( breakup) else breakup ;comment = str(comment) if( comment) else comment ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular PayRoll or it's a search request
    if id is not None: 
      res= PayRollManager.getPayRoll(id,mv=mv)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= PayRollManager.searchPayRoll(type=type,month=month,year=year,source=source,category=category,subcategory=subcategory,amount=amount,actualamount=actualamount,breakup=breakup,comment=comment,id=id,page=page,limit=limit,mv=mv  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    type= request.POST.get('type') if request.POST.get('type','').strip() else None;month= request.POST.get('month') if request.POST.get('month','').strip() else None;year= request.POST.get('year') if request.POST.get('year','').strip() else None;source= request.POST.get('source') if request.POST.get('source','').strip() else None;category= request.POST.get('category') if request.POST.get('category','').strip() else None;subcategory= request.POST.get('subcategory') if request.POST.get('subcategory','').strip() else None;amount= request.POST.get('amount') if request.POST.get('amount','').strip() else None;actualamount= request.POST.get('actualamount') if request.POST.get('actualamount','').strip() else None;breakup= request.POST.get('breakup') if request.POST.get('breakup','').strip() else None;comment= request.POST.get('comment') if request.POST.get('comment','').strip() else None;   
    type=type if type else None ;month=month if month else None ;year=year if year else None ;source=source if source else None ;category=category if category else None ;subcategory=subcategory if subcategory else None ;amount=amount if amount else None ;actualamount=actualamount if actualamount else None ;breakup=breakup if breakup else {'hello':0} ;comment=comment if comment else None ;    
    #data Must be Normalized to required DataType..
    try:
      type = str2List(type) if( type) else type ;month = str2List(month) if( month) else month ;year = str2List(year) if( year) else year ;source = str2List(source) if( source) else source ;category = str2List(category) if( category) else category ;subcategory = str(subcategory) if( subcategory) else subcategory ;amount = int(amount) if( amount) else amount ;actualamount = int(actualamount) if( actualamount) else actualamount ;breakup = dict(breakup) if( breakup) else breakup ;comment = str(comment) if( comment) else comment ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=PayRollManager.updatePayRoll(id=id,type=type,month=month,year=year,source=source,category=category,subcategory=subcategory,amount=amount,actualamount=actualamount,breakup=breakup,comment=comment,)
    else:
      # This is new entry request...
      res=PayRollManager.createPayRoll(type=type,month=month,year=year,source=source,category=category,subcategory=subcategory,amount=amount,actualamount=actualamount,breakup=breakup,comment=comment,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =PayRollManager.deletePayRoll(id)
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
def ajax_PayRoll_asearch(request): # We support POST only .
  res=None
  # This is basically a search by a tag or list items with given arguments
  if request.method == 'GET':
    return AutoHttpResponse(501)
  # This is basically a append to a list with given arguments
  elif request.method == 'POST':
    id=request.POST.get('id',None)    
    try: 
      #type = parseTriple(request.POST.get('type',None));month = parseTriple(request.POST.get('month',None));year = parseTriple(request.POST.get('year',None));source = parseTriple(request.POST.get('source',None));category = parseTriple(request.POST.get('category',None));subcategory = parseTriple(request.POST.get('subcategory',None));amount = parseTriple(request.POST.get('amount',None));actualamount = parseTriple(request.POST.get('actualamount',None));breakup = parseTriple(request.POST.get('breakup',None));comment = parseTriple(request.POST.get('comment',None));
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
       res = PayRollManager.advSearchPayRoll(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_PayRoll_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = PayRollManager.minViewPayRoll(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


@csrf_exempt
def ajax_PayRoll_quick_search(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    q=request.GET.get('q',None)
    if not q:
      return AutoHttpResponse(200,'you must a input called ?q=abcd') 
    res = PayRollManager.getPayRoll_quick_search(q=q,page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  

