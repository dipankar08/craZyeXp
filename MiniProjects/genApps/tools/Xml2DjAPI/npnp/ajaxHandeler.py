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
  


from .api import ParentManager
@csrf_exempt
def ajax_Parent(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;email= request.GET.get('email') if request.GET.get('email','').strip() else None;phone= request.GET.get('phone') if request.GET.get('phone','').strip() else None;occupation= request.GET.get('occupation') if request.GET.get('occupation','').strip() else None;address= request.GET.get('address') if request.GET.get('address','').strip() else None;income= request.GET.get('income') if request.GET.get('income','').strip() else None;relationship= request.GET.get('relationship') if request.GET.get('relationship','').strip() else None;secondary_contact= request.GET.get('secondary_contact') if request.GET.get('secondary_contact','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;occupation = str(occupation) if( occupation) else occupation ;address = str(address) if( address) else address ;income = str(income) if( income) else income ;relationship = str(relationship) if( relationship) else relationship ;secondary_contact = str(secondary_contact) if( secondary_contact) else secondary_contact ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Parent or it's a search request
    if id is not None: 
      res= ParentManager.getParent(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= ParentManager.searchParent(name=name,email=email,phone=phone,occupation=occupation,address=address,income=income,relationship=relationship,secondary_contact=secondary_contact,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;email= request.POST.get('email') if request.POST.get('email','').strip() else None;phone= request.POST.get('phone') if request.POST.get('phone','').strip() else None;occupation= request.POST.get('occupation') if request.POST.get('occupation','').strip() else None;address= request.POST.get('address') if request.POST.get('address','').strip() else None;income= request.POST.get('income') if request.POST.get('income','').strip() else None;relationship= request.POST.get('relationship') if request.POST.get('relationship','').strip() else None;secondary_contact= request.POST.get('secondary_contact') if request.POST.get('secondary_contact','').strip() else None;   
    name=name if name else None ;email=email if email else None ;phone=phone if phone else None ;occupation=occupation if occupation else None ;address=address if address else None ;income=income if income else None ;relationship=relationship if relationship else None ;secondary_contact=secondary_contact if secondary_contact else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;occupation = str(occupation) if( occupation) else occupation ;address = str(address) if( address) else address ;income = str(income) if( income) else income ;relationship = str(relationship) if( relationship) else relationship ;secondary_contact = str(secondary_contact) if( secondary_contact) else secondary_contact ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=ParentManager.updateParent(id=id,name=name,email=email,phone=phone,occupation=occupation,address=address,income=income,relationship=relationship,secondary_contact=secondary_contact,)
    else:
      # This is new entry request...
      res=ParentManager.createParent(name=name,email=email,phone=phone,occupation=occupation,address=address,income=income,relationship=relationship,secondary_contact=secondary_contact,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =ParentManager.deleteParent(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Parent_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= ParentManager.getParent_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    student=str2List(request.POST.get('student',None))
    if not student : return AutoHttpResponse(400,'Missing/Bad input: <student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ParentManager.addParent_Student(id=id,student = student)
    else:
      # do a delete action
      res=ParentManager.removeParent_Student(id=id,student = student)

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
def ajax_Parent_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));email = parseTriple(request.POST.get('email',None));phone = parseTriple(request.POST.get('phone',None));occupation = parseTriple(request.POST.get('occupation',None));address = parseTriple(request.POST.get('address',None));income = parseTriple(request.POST.get('income',None));relationship = parseTriple(request.POST.get('relationship',None));secondary_contact = parseTriple(request.POST.get('secondary_contact',None));
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
       res = ParentManager.advSearchParent(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Parent_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = ParentManager.minViewParent(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import EmployeeManager
@csrf_exempt
def ajax_Employee(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;uid= request.GET.get('uid') if request.GET.get('uid','').strip() else None;address= request.GET.get('address') if request.GET.get('address','').strip() else None;age= request.GET.get('age') if request.GET.get('age','').strip() else None;designation= request.GET.get('designation') if request.GET.get('designation','').strip() else None;rank= request.GET.get('rank') if request.GET.get('rank','').strip() else None;max_qualification= request.GET.get('max_qualification') if request.GET.get('max_qualification','').strip() else None;meretarial_status= request.GET.get('meretarial_status') if request.GET.get('meretarial_status','').strip() else None;gender= request.GET.get('gender') if request.GET.get('gender','').strip() else None;dob= request.GET.get('dob') if request.GET.get('dob','').strip() else None;doj= request.GET.get('doj') if request.GET.get('doj','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;uid = str(uid) if( uid) else uid ;address = str(address) if( address) else address ;age = int(age) if( age) else age ;designation = str(designation) if( designation) else designation ;rank = str(rank) if( rank) else rank ;max_qualification = str(max_qualification) if( max_qualification) else max_qualification ;meretarial_status = str(meretarial_status) if( meretarial_status) else meretarial_status ;gender = str(gender) if( gender) else gender ;dob = str(dob) if( dob) else dob ;doj = date(doj) if( doj) else doj ;categories = str2List(categories) if( categories) else categories ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Employee or it's a search request
    if id is not None: 
      res= EmployeeManager.getEmployee(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= EmployeeManager.searchEmployee(name=name,uid=uid,address=address,age=age,designation=designation,rank=rank,max_qualification=max_qualification,meretarial_status=meretarial_status,gender=gender,dob=dob,doj=doj,categories=categories,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;uid= request.POST.get('uid') if request.POST.get('uid','').strip() else None;address= request.POST.get('address') if request.POST.get('address','').strip() else None;age= request.POST.get('age') if request.POST.get('age','').strip() else None;designation= request.POST.get('designation') if request.POST.get('designation','').strip() else None;rank= request.POST.get('rank') if request.POST.get('rank','').strip() else None;max_qualification= request.POST.get('max_qualification') if request.POST.get('max_qualification','').strip() else None;meretarial_status= request.POST.get('meretarial_status') if request.POST.get('meretarial_status','').strip() else None;gender= request.POST.get('gender') if request.POST.get('gender','').strip() else None;dob= request.POST.get('dob') if request.POST.get('dob','').strip() else None;doj= request.POST.get('doj') if request.POST.get('doj','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;   
    name=name if name else None ;uid=uid if uid else None ;address=address if address else None ;age=age if age else None ;designation=designation if designation else None ;rank=rank if rank else None ;max_qualification=max_qualification if max_qualification else None ;meretarial_status=meretarial_status if meretarial_status else None ;gender=gender if gender else None ;dob=dob if dob else None ;doj=doj if doj else None ;categories=categories if categories else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;uid = str(uid) if( uid) else uid ;address = str(address) if( address) else address ;age = int(age) if( age) else age ;designation = str(designation) if( designation) else designation ;rank = str(rank) if( rank) else rank ;max_qualification = str(max_qualification) if( max_qualification) else max_qualification ;meretarial_status = str(meretarial_status) if( meretarial_status) else meretarial_status ;gender = str(gender) if( gender) else gender ;dob = str(dob) if( dob) else dob ;doj = date(doj) if( doj) else doj ;categories = str2List(categories) if( categories) else categories ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=EmployeeManager.updateEmployee(id=id,name=name,uid=uid,address=address,age=age,designation=designation,rank=rank,max_qualification=max_qualification,meretarial_status=meretarial_status,gender=gender,dob=dob,doj=doj,categories=categories,)
    else:
      # This is new entry request...
      res=EmployeeManager.createEmployee(name=name,uid=uid,address=address,age=age,designation=designation,rank=rank,max_qualification=max_qualification,meretarial_status=meretarial_status,gender=gender,dob=dob,doj=doj,categories=categories,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =EmployeeManager.deleteEmployee(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Employee_Subject(request,id=None):
  res=None
  #If the request is coming for get to all Subject_set
  if request.method == 'GET':
      res= EmployeeManager.getEmployee_Subject(id=id)

  #This is the implementation for POST request to add or delete Subject
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    subject=str2List(request.POST.get('subject',None))
    if not subject : return AutoHttpResponse(400,'Missing/Bad input: <subject: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=EmployeeManager.addEmployee_Subject(id=id,subject = subject)
    else:
      # do a delete action
      res=EmployeeManager.removeEmployee_Subject(id=id,subject = subject)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Employee_MyClass(request,id=None):
  res=None
  #If the request is coming for get to all MyClass_set
  if request.method == 'GET':
      res= EmployeeManager.getEmployee_MyClass(id=id)

  #This is the implementation for POST request to add or delete MyClass
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    myclass=str2List(request.POST.get('myclass',None))
    if not myclass : return AutoHttpResponse(400,'Missing/Bad input: <myclass: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=EmployeeManager.addEmployee_MyClass(id=id,myclass = myclass)
    else:
      # do a delete action
      res=EmployeeManager.removeEmployee_MyClass(id=id,myclass = myclass)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Employee_Exam(request,id=None):
  res=None
  #If the request is coming for get to all Exam_set
  if request.method == 'GET':
      res= EmployeeManager.getEmployee_Exam(id=id)

  #This is the implementation for POST request to add or delete Exam
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    exam=str2List(request.POST.get('exam',None))
    if not exam : return AutoHttpResponse(400,'Missing/Bad input: <exam: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=EmployeeManager.addEmployee_Exam(id=id,exam = exam)
    else:
      # do a delete action
      res=EmployeeManager.removeEmployee_Exam(id=id,exam = exam)

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
def ajax_Employee_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));uid = parseTriple(request.POST.get('uid',None));address = parseTriple(request.POST.get('address',None));age = parseTriple(request.POST.get('age',None));designation = parseTriple(request.POST.get('designation',None));rank = parseTriple(request.POST.get('rank',None));max_qualification = parseTriple(request.POST.get('max_qualification',None));meretarial_status = parseTriple(request.POST.get('meretarial_status',None));gender = parseTriple(request.POST.get('gender',None));dob = parseTriple(request.POST.get('dob',None));doj = parseTriple(request.POST.get('doj',None));categories = parseTriple(request.POST.get('categories',None));
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
       res = EmployeeManager.advSearchEmployee(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Employee_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = EmployeeManager.minViewEmployee(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import SubjectManager
@csrf_exempt
def ajax_Subject(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;uid= request.GET.get('uid') if request.GET.get('uid','').strip() else None;syllabus= request.GET.get('syllabus') if request.GET.get('syllabus','').strip() else None;ref_book= request.GET.get('ref_book') if request.GET.get('ref_book','').strip() else None;teacher= request.GET.get('teacher') if request.GET.get('teacher','').strip() else None;categorise= request.GET.get('categorise') if request.GET.get('categorise','').strip() else None;group= request.GET.get('group') if request.GET.get('group','').strip() else None;mark_division= request.GET.get('mark_division') if request.GET.get('mark_division','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;uid = str(uid) if( uid) else uid ;syllabus = str(syllabus) if( syllabus) else syllabus ;ref_book = str(ref_book) if( ref_book) else ref_book ;teacher = str2List(teacher) if( teacher) else teacher ;categorise = str2List(categorise) if( categorise) else categorise ;group = str2List(group) if( group) else group ;mark_division = dict(mark_division) if( mark_division) else mark_division ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Subject or it's a search request
    if id is not None: 
      res= SubjectManager.getSubject(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= SubjectManager.searchSubject(name=name,uid=uid,syllabus=syllabus,ref_book=ref_book,teacher=teacher,categorise=categorise,group=group,mark_division=mark_division,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;uid= request.POST.get('uid') if request.POST.get('uid','').strip() else None;syllabus= request.POST.get('syllabus') if request.POST.get('syllabus','').strip() else None;ref_book= request.POST.get('ref_book') if request.POST.get('ref_book','').strip() else None;teacher= request.POST.get('teacher') if request.POST.get('teacher','').strip() else None;categorise= request.POST.get('categorise') if request.POST.get('categorise','').strip() else None;group= request.POST.get('group') if request.POST.get('group','').strip() else None;mark_division= request.POST.get('mark_division') if request.POST.get('mark_division','').strip() else None;   
    name=name if name else None ;uid=uid if uid else None ;syllabus=syllabus if syllabus else None ;ref_book=ref_book if ref_book else None ;teacher=teacher if teacher else None ;categorise=categorise if categorise else None ;group=group if group else None ;mark_division=mark_division if mark_division else {'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34} ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;uid = str(uid) if( uid) else uid ;syllabus = str(syllabus) if( syllabus) else syllabus ;ref_book = str(ref_book) if( ref_book) else ref_book ;teacher = str2List(teacher) if( teacher) else teacher ;categorise = str2List(categorise) if( categorise) else categorise ;group = str2List(group) if( group) else group ;mark_division = dict(mark_division) if( mark_division) else mark_division ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=SubjectManager.updateSubject(id=id,name=name,uid=uid,syllabus=syllabus,ref_book=ref_book,teacher=teacher,categorise=categorise,group=group,mark_division=mark_division,)
    else:
      # This is new entry request...
      res=SubjectManager.createSubject(name=name,uid=uid,syllabus=syllabus,ref_book=ref_book,teacher=teacher,categorise=categorise,group=group,mark_division=mark_division,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =SubjectManager.deleteSubject(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Subject_Employee(request,id=None):
  res=None
  #If the request is coming for get to all Employee_set
  if request.method == 'GET':
      res= SubjectManager.getSubject_Employee(id=id)

  #This is the implementation for POST request to add or delete Employee
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    teacher=str2List(request.POST.get('teacher',None))
    if not teacher : return AutoHttpResponse(400,'Missing/Bad input: <teacher: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=SubjectManager.addSubject_Employee(id=id,teacher = teacher)
    else:
      # do a delete action
      res=SubjectManager.removeSubject_Employee(id=id,teacher = teacher)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Subject_MyClass(request,id=None):
  res=None
  #If the request is coming for get to all MyClass_set
  if request.method == 'GET':
      res= SubjectManager.getSubject_MyClass(id=id)

  #This is the implementation for POST request to add or delete MyClass
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    myclass=str2List(request.POST.get('myclass',None))
    if not myclass : return AutoHttpResponse(400,'Missing/Bad input: <myclass: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=SubjectManager.addSubject_MyClass(id=id,myclass = myclass)
    else:
      # do a delete action
      res=SubjectManager.removeSubject_MyClass(id=id,myclass = myclass)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Subject_Exam(request,id=None):
  res=None
  #If the request is coming for get to all Exam_set
  if request.method == 'GET':
      res= SubjectManager.getSubject_Exam(id=id)

  #This is the implementation for POST request to add or delete Exam
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    exam=str2List(request.POST.get('exam',None))
    if not exam : return AutoHttpResponse(400,'Missing/Bad input: <exam: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=SubjectManager.addSubject_Exam(id=id,exam = exam)
    else:
      # do a delete action
      res=SubjectManager.removeSubject_Exam(id=id,exam = exam)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Subject_Mark(request,id=None):
  res=None
  #If the request is coming for get to all Mark_set
  if request.method == 'GET':
      res= SubjectManager.getSubject_Mark(id=id)

  #This is the implementation for POST request to add or delete Mark
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    mark=str2List(request.POST.get('mark',None))
    if not mark : return AutoHttpResponse(400,'Missing/Bad input: <mark: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=SubjectManager.addSubject_Mark(id=id,mark = mark)
    else:
      # do a delete action
      res=SubjectManager.removeSubject_Mark(id=id,mark = mark)

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
def ajax_Subject_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));uid = parseTriple(request.POST.get('uid',None));syllabus = parseTriple(request.POST.get('syllabus',None));ref_book = parseTriple(request.POST.get('ref_book',None));teacher = parseTriple(request.POST.get('teacher',None));categorise = parseTriple(request.POST.get('categorise',None));group = parseTriple(request.POST.get('group',None));mark_division = parseTriple(request.POST.get('mark_division',None));
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
       res = SubjectManager.advSearchSubject(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Subject_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = SubjectManager.minViewSubject(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import MyClassManager
@csrf_exempt
def ajax_MyClass(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;room= request.GET.get('room') if request.GET.get('room','').strip() else None;class_teacher= request.GET.get('class_teacher') if request.GET.get('class_teacher','').strip() else None;subjects= request.GET.get('subjects') if request.GET.get('subjects','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;room = str(room) if( room) else room ;class_teacher = str2List(class_teacher) if( class_teacher) else class_teacher ;subjects = str2List(subjects) if( subjects) else subjects ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular MyClass or it's a search request
    if id is not None: 
      res= MyClassManager.getMyClass(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= MyClassManager.searchMyClass(name=name,room=room,class_teacher=class_teacher,subjects=subjects,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;room= request.POST.get('room') if request.POST.get('room','').strip() else None;class_teacher= request.POST.get('class_teacher') if request.POST.get('class_teacher','').strip() else None;subjects= request.POST.get('subjects') if request.POST.get('subjects','').strip() else None;   
    name=name if name else None ;room=room if room else None ;class_teacher=class_teacher if class_teacher else None ;subjects=subjects if subjects else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;room = str(room) if( room) else room ;class_teacher = str2List(class_teacher) if( class_teacher) else class_teacher ;subjects = str2List(subjects) if( subjects) else subjects ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=MyClassManager.updateMyClass(id=id,name=name,room=room,class_teacher=class_teacher,subjects=subjects,)
    else:
      # This is new entry request...
      res=MyClassManager.createMyClass(name=name,room=room,class_teacher=class_teacher,subjects=subjects,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =MyClassManager.deleteMyClass(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_MyClass_Employee(request,id=None):
  res=None
  #If the request is coming for get to all Employee_set
  if request.method == 'GET':
      res= MyClassManager.getMyClass_Employee(id=id)

  #This is the implementation for POST request to add or delete Employee
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    class_teacher=str2List(request.POST.get('class_teacher',None))
    if not class_teacher : return AutoHttpResponse(400,'Missing/Bad input: <class_teacher: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MyClassManager.addMyClass_Employee(id=id,class_teacher = class_teacher)
    else:
      # do a delete action
      res=MyClassManager.removeMyClass_Employee(id=id,class_teacher = class_teacher)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_MyClass_Subject(request,id=None):
  res=None
  #If the request is coming for get to all Subject_set
  if request.method == 'GET':
      res= MyClassManager.getMyClass_Subject(id=id)

  #This is the implementation for POST request to add or delete Subject
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    subjects=str2List(request.POST.get('subjects',None))
    if not subjects : return AutoHttpResponse(400,'Missing/Bad input: <subjects: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MyClassManager.addMyClass_Subject(id=id,subjects = subjects)
    else:
      # do a delete action
      res=MyClassManager.removeMyClass_Subject(id=id,subjects = subjects)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_MyClass_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= MyClassManager.getMyClass_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    student=str2List(request.POST.get('student',None))
    if not student : return AutoHttpResponse(400,'Missing/Bad input: <student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MyClassManager.addMyClass_Student(id=id,student = student)
    else:
      # do a delete action
      res=MyClassManager.removeMyClass_Student(id=id,student = student)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_MyClass_Attendance(request,id=None):
  res=None
  #If the request is coming for get to all Attendance_set
  if request.method == 'GET':
      res= MyClassManager.getMyClass_Attendance(id=id)

  #This is the implementation for POST request to add or delete Attendance
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    attendance=str2List(request.POST.get('attendance',None))
    if not attendance : return AutoHttpResponse(400,'Missing/Bad input: <attendance: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MyClassManager.addMyClass_Attendance(id=id,attendance = attendance)
    else:
      # do a delete action
      res=MyClassManager.removeMyClass_Attendance(id=id,attendance = attendance)

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
def ajax_MyClass_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));room = parseTriple(request.POST.get('room',None));class_teacher = parseTriple(request.POST.get('class_teacher',None));subjects = parseTriple(request.POST.get('subjects',None));
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
       res = MyClassManager.advSearchMyClass(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_MyClass_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = MyClassManager.minViewMyClass(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import ExamManager
@csrf_exempt
def ajax_Exam(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;subject= request.GET.get('subject') if request.GET.get('subject','').strip() else None;classRoom= request.GET.get('classRoom') if request.GET.get('classRoom','').strip() else None;time= request.GET.get('time') if request.GET.get('time','').strip() else None;teacher= request.GET.get('teacher') if request.GET.get('teacher','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str2List(name) if( name) else name ;subject = int(subject) if( subject) else subject ;classRoom = str(classRoom) if( classRoom) else classRoom ;time = str(time) if( time) else time ;teacher = str2List(teacher) if( teacher) else teacher ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Exam or it's a search request
    if id is not None: 
      res= ExamManager.getExam(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= ExamManager.searchExam(name=name,subject=subject,classRoom=classRoom,time=time,teacher=teacher,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;subject= request.POST.get('subject') if request.POST.get('subject','').strip() else None;classRoom= request.POST.get('classRoom') if request.POST.get('classRoom','').strip() else None;time= request.POST.get('time') if request.POST.get('time','').strip() else None;teacher= request.POST.get('teacher') if request.POST.get('teacher','').strip() else None;   
    name=name if name else None ;subject=subject if subject else None ;classRoom=classRoom if classRoom else None ;time=time if time else None ;teacher=teacher if teacher else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str2List(name) if( name) else name ;subject = int(subject) if( subject) else subject ;classRoom = str(classRoom) if( classRoom) else classRoom ;time = str(time) if( time) else time ;teacher = str2List(teacher) if( teacher) else teacher ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=ExamManager.updateExam(id=id,name=name,subject=subject,classRoom=classRoom,time=time,teacher=teacher,)
    else:
      # This is new entry request...
      res=ExamManager.createExam(name=name,subject=subject,classRoom=classRoom,time=time,teacher=teacher,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =ExamManager.deleteExam(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Exam_Subject(request,id=None):
  res=None
  #If the request is coming for get to all Subject_set
  if request.method == 'GET':
      res= ExamManager.getExam_Subject(id=id)

  #This is the implementation for POST request to add or delete Subject
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    subject=str2List(request.POST.get('subject',None))
    if not subject : return AutoHttpResponse(400,'Missing/Bad input: <subject: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ExamManager.addExam_Subject(id=id,subject = subject)
    else:
      # do a delete action
      res=ExamManager.removeExam_Subject(id=id,subject = subject)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Exam_Employee(request,id=None):
  res=None
  #If the request is coming for get to all Employee_set
  if request.method == 'GET':
      res= ExamManager.getExam_Employee(id=id)

  #This is the implementation for POST request to add or delete Employee
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    teacher=str2List(request.POST.get('teacher',None))
    if not teacher : return AutoHttpResponse(400,'Missing/Bad input: <teacher: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ExamManager.addExam_Employee(id=id,teacher = teacher)
    else:
      # do a delete action
      res=ExamManager.removeExam_Employee(id=id,teacher = teacher)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Exam_Mark(request,id=None):
  res=None
  #If the request is coming for get to all Mark_set
  if request.method == 'GET':
      res= ExamManager.getExam_Mark(id=id)

  #This is the implementation for POST request to add or delete Mark
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    mark=str2List(request.POST.get('mark',None))
    if not mark : return AutoHttpResponse(400,'Missing/Bad input: <mark: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ExamManager.addExam_Mark(id=id,mark = mark)
    else:
      # do a delete action
      res=ExamManager.removeExam_Mark(id=id,mark = mark)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Exam_Result(request,id=None):
  res=None
  #If the request is coming for get to all Result_set
  if request.method == 'GET':
      res= ExamManager.getExam_Result(id=id)

  #This is the implementation for POST request to add or delete Result
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    result=str2List(request.POST.get('result',None))
    if not result : return AutoHttpResponse(400,'Missing/Bad input: <result: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ExamManager.addExam_Result(id=id,result = result)
    else:
      # do a delete action
      res=ExamManager.removeExam_Result(id=id,result = result)

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
def ajax_Exam_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));subject = parseTriple(request.POST.get('subject',None));classRoom = parseTriple(request.POST.get('classRoom',None));time = parseTriple(request.POST.get('time',None));teacher = parseTriple(request.POST.get('teacher',None));
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
       res = ExamManager.advSearchExam(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Exam_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = ExamManager.minViewExam(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import StudentManager
@csrf_exempt
def ajax_Student(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;email= request.GET.get('email') if request.GET.get('email','').strip() else None;phone= request.GET.get('phone') if request.GET.get('phone','').strip() else None;address= request.GET.get('address') if request.GET.get('address','').strip() else None;dob= request.GET.get('dob') if request.GET.get('dob','').strip() else None;doj= request.GET.get('doj') if request.GET.get('doj','').strip() else None;gender= request.GET.get('gender') if request.GET.get('gender','').strip() else None;parent= request.GET.get('parent') if request.GET.get('parent','').strip() else None;roll= request.GET.get('roll') if request.GET.get('roll','').strip() else None;section= request.GET.get('section') if request.GET.get('section','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;address = str(address) if( address) else address ;dob = str(dob) if( dob) else dob ;doj = date(doj) if( doj) else doj ;gender = str(gender) if( gender) else gender ;parent = int(parent) if( parent) else parent ;roll = str(roll) if( roll) else roll ;section = str2List(section) if( section) else section ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Student or it's a search request
    if id is not None: 
      res= StudentManager.getStudent(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= StudentManager.searchStudent(name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,parent=parent,roll=roll,section=section,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;email= request.POST.get('email') if request.POST.get('email','').strip() else None;phone= request.POST.get('phone') if request.POST.get('phone','').strip() else None;address= request.POST.get('address') if request.POST.get('address','').strip() else None;dob= request.POST.get('dob') if request.POST.get('dob','').strip() else None;doj= request.POST.get('doj') if request.POST.get('doj','').strip() else None;gender= request.POST.get('gender') if request.POST.get('gender','').strip() else None;parent= request.POST.get('parent') if request.POST.get('parent','').strip() else None;roll= request.POST.get('roll') if request.POST.get('roll','').strip() else None;section= request.POST.get('section') if request.POST.get('section','').strip() else None;   
    name=name if name else None ;email=email if email else None ;phone=phone if phone else None ;address=address if address else None ;dob=dob if dob else None ;doj=doj if doj else None ;gender=gender if gender else None ;parent=parent if parent else None ;roll=roll if roll else None ;section=section if section else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;address = str(address) if( address) else address ;dob = str(dob) if( dob) else dob ;doj = date(doj) if( doj) else doj ;gender = str(gender) if( gender) else gender ;parent = int(parent) if( parent) else parent ;roll = str(roll) if( roll) else roll ;section = str2List(section) if( section) else section ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=StudentManager.updateStudent(id=id,name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,parent=parent,roll=roll,section=section,)
    else:
      # This is new entry request...
      res=StudentManager.createStudent(name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,parent=parent,roll=roll,section=section,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =StudentManager.deleteStudent(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Student_Parent(request,id=None):
  res=None
  #If the request is coming for get to all Parent_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Parent(id=id)

  #This is the implementation for POST request to add or delete Parent
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    parent=str2List(request.POST.get('parent',None))
    if not parent : return AutoHttpResponse(400,'Missing/Bad input: <parent: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Parent(id=id,parent = parent)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Parent(id=id,parent = parent)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_MyClass(request,id=None):
  res=None
  #If the request is coming for get to all MyClass_set
  if request.method == 'GET':
      res= StudentManager.getStudent_MyClass(id=id)

  #This is the implementation for POST request to add or delete MyClass
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    myclass=str2List(request.POST.get('myclass',None))
    if not myclass : return AutoHttpResponse(400,'Missing/Bad input: <myclass: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_MyClass(id=id,myclass = myclass)
    else:
      # do a delete action
      res=StudentManager.removeStudent_MyClass(id=id,myclass = myclass)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_Mark(request,id=None):
  res=None
  #If the request is coming for get to all Mark_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Mark(id=id)

  #This is the implementation for POST request to add or delete Mark
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    mark=str2List(request.POST.get('mark',None))
    if not mark : return AutoHttpResponse(400,'Missing/Bad input: <mark: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Mark(id=id,mark = mark)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Mark(id=id,mark = mark)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_Result(request,id=None):
  res=None
  #If the request is coming for get to all Result_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Result(id=id)

  #This is the implementation for POST request to add or delete Result
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    result=str2List(request.POST.get('result',None))
    if not result : return AutoHttpResponse(400,'Missing/Bad input: <result: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Result(id=id,result = result)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Result(id=id,result = result)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_Attendance(request,id=None):
  res=None
  #If the request is coming for get to all Attendance_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Attendance(id=id)

  #This is the implementation for POST request to add or delete Attendance
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    attendance=str2List(request.POST.get('attendance',None))
    if not attendance : return AutoHttpResponse(400,'Missing/Bad input: <attendance: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Attendance(id=id,attendance = attendance)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Attendance(id=id,attendance = attendance)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_Fees(request,id=None):
  res=None
  #If the request is coming for get to all Fees_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Fees(id=id)

  #This is the implementation for POST request to add or delete Fees
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    fees=str2List(request.POST.get('fees',None))
    if not fees : return AutoHttpResponse(400,'Missing/Bad input: <fees: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Fees(id=id,fees = fees)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Fees(id=id,fees = fees)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_Sport(request,id=None):
  res=None
  #If the request is coming for get to all Sport_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Sport(id=id)

  #This is the implementation for POST request to add or delete Sport
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    sport=str2List(request.POST.get('sport',None))
    if not sport : return AutoHttpResponse(400,'Missing/Bad input: <sport: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Sport(id=id,sport = sport)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Sport(id=id,sport = sport)

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
def ajax_Student_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));email = parseTriple(request.POST.get('email',None));phone = parseTriple(request.POST.get('phone',None));address = parseTriple(request.POST.get('address',None));dob = parseTriple(request.POST.get('dob',None));doj = parseTriple(request.POST.get('doj',None));gender = parseTriple(request.POST.get('gender',None));parent = parseTriple(request.POST.get('parent',None));roll = parseTriple(request.POST.get('roll',None));section = parseTriple(request.POST.get('section',None));
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
       res = StudentManager.advSearchStudent(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Student_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = StudentManager.minViewStudent(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import MarkManager
@csrf_exempt
def ajax_Mark(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    student= request.GET.get('student') if request.GET.get('student','').strip() else None;subject= request.GET.get('subject') if request.GET.get('subject','').strip() else None;exam= request.GET.get('exam') if request.GET.get('exam','').strip() else None;written= request.GET.get('written') if request.GET.get('written','').strip() else None;viva= request.GET.get('viva') if request.GET.get('viva','').strip() else None;practical= request.GET.get('practical') if request.GET.get('practical','').strip() else None;total= request.GET.get('total') if request.GET.get('total','').strip() else None;comment= request.GET.get('comment') if request.GET.get('comment','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      student = int(student) if( student) else student ;subject = int(subject) if( subject) else subject ;exam = int(exam) if( exam) else exam ;written = int(written) if( written) else written ;viva = int(viva) if( viva) else viva ;practical = int(practical) if( practical) else practical ;total = int(total) if( total) else total ;comment = str(comment) if( comment) else comment ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Mark or it's a search request
    if id is not None: 
      res= MarkManager.getMark(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= MarkManager.searchMark(student=student,subject=subject,exam=exam,written=written,viva=viva,practical=practical,total=total,comment=comment,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    student= request.POST.get('student') if request.POST.get('student','').strip() else None;subject= request.POST.get('subject') if request.POST.get('subject','').strip() else None;exam= request.POST.get('exam') if request.POST.get('exam','').strip() else None;written= request.POST.get('written') if request.POST.get('written','').strip() else None;viva= request.POST.get('viva') if request.POST.get('viva','').strip() else None;practical= request.POST.get('practical') if request.POST.get('practical','').strip() else None;total= request.POST.get('total') if request.POST.get('total','').strip() else None;comment= request.POST.get('comment') if request.POST.get('comment','').strip() else None;   
    student=student if student else None ;subject=subject if subject else None ;exam=exam if exam else None ;written=written if written else 0 ;viva=viva if viva else 0 ;practical=practical if practical else 0 ;total=total if total else 0 ;comment=comment if comment else None ;    
    #data Must be Normalized to required DataType..
    try:
      student = int(student) if( student) else student ;subject = int(subject) if( subject) else subject ;exam = int(exam) if( exam) else exam ;written = int(written) if( written) else written ;viva = int(viva) if( viva) else viva ;practical = int(practical) if( practical) else practical ;total = int(total) if( total) else total ;comment = str(comment) if( comment) else comment ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=MarkManager.updateMark(id=id,student=student,subject=subject,exam=exam,written=written,viva=viva,practical=practical,total=total,comment=comment,)
    else:
      # This is new entry request...
      res=MarkManager.createMark(student=student,subject=subject,exam=exam,written=written,viva=viva,practical=practical,total=total,comment=comment,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =MarkManager.deleteMark(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Mark_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= MarkManager.getMark_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    student=str2List(request.POST.get('student',None))
    if not student : return AutoHttpResponse(400,'Missing/Bad input: <student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MarkManager.addMark_Student(id=id,student = student)
    else:
      # do a delete action
      res=MarkManager.removeMark_Student(id=id,student = student)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Mark_Subject(request,id=None):
  res=None
  #If the request is coming for get to all Subject_set
  if request.method == 'GET':
      res= MarkManager.getMark_Subject(id=id)

  #This is the implementation for POST request to add or delete Subject
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    subject=str2List(request.POST.get('subject',None))
    if not subject : return AutoHttpResponse(400,'Missing/Bad input: <subject: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MarkManager.addMark_Subject(id=id,subject = subject)
    else:
      # do a delete action
      res=MarkManager.removeMark_Subject(id=id,subject = subject)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Mark_Exam(request,id=None):
  res=None
  #If the request is coming for get to all Exam_set
  if request.method == 'GET':
      res= MarkManager.getMark_Exam(id=id)

  #This is the implementation for POST request to add or delete Exam
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    exam=str2List(request.POST.get('exam',None))
    if not exam : return AutoHttpResponse(400,'Missing/Bad input: <exam: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=MarkManager.addMark_Exam(id=id,exam = exam)
    else:
      # do a delete action
      res=MarkManager.removeMark_Exam(id=id,exam = exam)

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
def ajax_Mark_asearch(request): # We support POST only .
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
      #student = parseTriple(request.POST.get('student',None));subject = parseTriple(request.POST.get('subject',None));exam = parseTriple(request.POST.get('exam',None));written = parseTriple(request.POST.get('written',None));viva = parseTriple(request.POST.get('viva',None));practical = parseTriple(request.POST.get('practical',None));total = parseTriple(request.POST.get('total',None));comment = parseTriple(request.POST.get('comment',None));
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
       res = MarkManager.advSearchMark(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Mark_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = MarkManager.minViewMark(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import ResultManager
@csrf_exempt
def ajax_Result(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    exam= request.GET.get('exam') if request.GET.get('exam','').strip() else None;total= request.GET.get('total') if request.GET.get('total','').strip() else None;percentage= request.GET.get('percentage') if request.GET.get('percentage','').strip() else None;division= request.GET.get('division') if request.GET.get('division','').strip() else None;comment= request.GET.get('comment') if request.GET.get('comment','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      exam = int(exam) if( exam) else exam ;total = int(total) if( total) else total ;percentage = int(percentage) if( percentage) else percentage ;division = str2List(division) if( division) else division ;comment = str(comment) if( comment) else comment ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Result or it's a search request
    if id is not None: 
      res= ResultManager.getResult(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= ResultManager.searchResult(exam=exam,total=total,percentage=percentage,division=division,comment=comment,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    exam= request.POST.get('exam') if request.POST.get('exam','').strip() else None;total= request.POST.get('total') if request.POST.get('total','').strip() else None;percentage= request.POST.get('percentage') if request.POST.get('percentage','').strip() else None;division= request.POST.get('division') if request.POST.get('division','').strip() else None;comment= request.POST.get('comment') if request.POST.get('comment','').strip() else None;   
    exam=exam if exam else None ;total=total if total else None ;percentage=percentage if percentage else None ;division=division if division else None ;comment=comment if comment else None ;    
    #data Must be Normalized to required DataType..
    try:
      exam = int(exam) if( exam) else exam ;total = int(total) if( total) else total ;percentage = int(percentage) if( percentage) else percentage ;division = str2List(division) if( division) else division ;comment = str(comment) if( comment) else comment ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=ResultManager.updateResult(id=id,exam=exam,total=total,percentage=percentage,division=division,comment=comment,)
    else:
      # This is new entry request...
      res=ResultManager.createResult(exam=exam,total=total,percentage=percentage,division=division,comment=comment,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =ResultManager.deleteResult(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Result_Exam(request,id=None):
  res=None
  #If the request is coming for get to all Exam_set
  if request.method == 'GET':
      res= ResultManager.getResult_Exam(id=id)

  #This is the implementation for POST request to add or delete Exam
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    exam=str2List(request.POST.get('exam',None))
    if not exam : return AutoHttpResponse(400,'Missing/Bad input: <exam: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ResultManager.addResult_Exam(id=id,exam = exam)
    else:
      # do a delete action
      res=ResultManager.removeResult_Exam(id=id,exam = exam)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Result_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= ResultManager.getResult_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    Student=str2List(request.POST.get('Student',None))
    if not Student : return AutoHttpResponse(400,'Missing/Bad input: <Student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ResultManager.addResult_Student(id=id,Student = Student)
    else:
      # do a delete action
      res=ResultManager.removeResult_Student(id=id,Student = Student)

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
def ajax_Result_asearch(request): # We support POST only .
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
      #exam = parseTriple(request.POST.get('exam',None));total = parseTriple(request.POST.get('total',None));percentage = parseTriple(request.POST.get('percentage',None));division = parseTriple(request.POST.get('division',None));comment = parseTriple(request.POST.get('comment',None));
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
       res = ResultManager.advSearchResult(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Result_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = ResultManager.minViewResult(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import AttendanceManager
@csrf_exempt
def ajax_Attendance(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    student= request.GET.get('student') if request.GET.get('student','').strip() else None;myclass= request.GET.get('myclass') if request.GET.get('myclass','').strip() else None;total= request.GET.get('total') if request.GET.get('total','').strip() else None;percentage= request.GET.get('percentage') if request.GET.get('percentage','').strip() else None;comment= request.GET.get('comment') if request.GET.get('comment','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      student = int(student) if( student) else student ;myclass = int(myclass) if( myclass) else myclass ;total = int(total) if( total) else total ;percentage = int(percentage) if( percentage) else percentage ;comment = str(comment) if( comment) else comment ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Attendance or it's a search request
    if id is not None: 
      res= AttendanceManager.getAttendance(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= AttendanceManager.searchAttendance(student=student,myclass=myclass,total=total,percentage=percentage,comment=comment,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    student= request.POST.get('student') if request.POST.get('student','').strip() else None;myclass= request.POST.get('myclass') if request.POST.get('myclass','').strip() else None;total= request.POST.get('total') if request.POST.get('total','').strip() else None;percentage= request.POST.get('percentage') if request.POST.get('percentage','').strip() else None;comment= request.POST.get('comment') if request.POST.get('comment','').strip() else None;   
    student=student if student else None ;myclass=myclass if myclass else None ;total=total if total else None ;percentage=percentage if percentage else None ;comment=comment if comment else None ;    
    #data Must be Normalized to required DataType..
    try:
      student = int(student) if( student) else student ;myclass = int(myclass) if( myclass) else myclass ;total = int(total) if( total) else total ;percentage = int(percentage) if( percentage) else percentage ;comment = str(comment) if( comment) else comment ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=AttendanceManager.updateAttendance(id=id,student=student,myclass=myclass,total=total,percentage=percentage,comment=comment,)
    else:
      # This is new entry request...
      res=AttendanceManager.createAttendance(student=student,myclass=myclass,total=total,percentage=percentage,comment=comment,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =AttendanceManager.deleteAttendance(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Attendance_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= AttendanceManager.getAttendance_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    student=str2List(request.POST.get('student',None))
    if not student : return AutoHttpResponse(400,'Missing/Bad input: <student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=AttendanceManager.addAttendance_Student(id=id,student = student)
    else:
      # do a delete action
      res=AttendanceManager.removeAttendance_Student(id=id,student = student)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Attendance_MyClass(request,id=None):
  res=None
  #If the request is coming for get to all MyClass_set
  if request.method == 'GET':
      res= AttendanceManager.getAttendance_MyClass(id=id)

  #This is the implementation for POST request to add or delete MyClass
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    myclass=str2List(request.POST.get('myclass',None))
    if not myclass : return AutoHttpResponse(400,'Missing/Bad input: <myclass: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=AttendanceManager.addAttendance_MyClass(id=id,myclass = myclass)
    else:
      # do a delete action
      res=AttendanceManager.removeAttendance_MyClass(id=id,myclass = myclass)

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
def ajax_Attendance_asearch(request): # We support POST only .
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
      #student = parseTriple(request.POST.get('student',None));myclass = parseTriple(request.POST.get('myclass',None));total = parseTriple(request.POST.get('total',None));percentage = parseTriple(request.POST.get('percentage',None));comment = parseTriple(request.POST.get('comment',None));
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
       res = AttendanceManager.advSearchAttendance(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Attendance_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = AttendanceManager.minViewAttendance(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import FeesManager
@csrf_exempt
def ajax_Fees(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;total= request.GET.get('total') if request.GET.get('total','').strip() else None;breakup= request.GET.get('breakup') if request.GET.get('breakup','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;total = int(total) if( total) else total ;breakup = dict(breakup) if( breakup) else breakup ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Fees or it's a search request
    if id is not None: 
      res= FeesManager.getFees(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= FeesManager.searchFees(name=name,accid=accid,total=total,breakup=breakup,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;total= request.POST.get('total') if request.POST.get('total','').strip() else None;breakup= request.POST.get('breakup') if request.POST.get('breakup','').strip() else None;   
    name=name if name else None ;accid=accid if accid else None ;total=total if total else None ;breakup=breakup if breakup else {'house_rent':0,'food':0,'traval':0} ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;total = int(total) if( total) else total ;breakup = dict(breakup) if( breakup) else breakup ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=FeesManager.updateFees(id=id,name=name,accid=accid,total=total,breakup=breakup,)
    else:
      # This is new entry request...
      res=FeesManager.createFees(name=name,accid=accid,total=total,breakup=breakup,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =FeesManager.deleteFees(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Fees_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= FeesManager.getFees_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    Student=str2List(request.POST.get('Student',None))
    if not Student : return AutoHttpResponse(400,'Missing/Bad input: <Student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=FeesManager.addFees_Student(id=id,Student = Student)
    else:
      # do a delete action
      res=FeesManager.removeFees_Student(id=id,Student = Student)

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
def ajax_Fees_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));accid = parseTriple(request.POST.get('accid',None));total = parseTriple(request.POST.get('total',None));breakup = parseTriple(request.POST.get('breakup',None));
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
       res = FeesManager.advSearchFees(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Fees_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = FeesManager.minViewFees(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import SportManager
@csrf_exempt
def ajax_Sport(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;position= request.GET.get('position') if request.GET.get('position','').strip() else None;student= request.GET.get('student') if request.GET.get('student','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;position = dict(position) if( position) else position ;student = str2List(student) if( student) else student ;categories = str2List(categories) if( categories) else categories ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Sport or it's a search request
    if id is not None: 
      res= SportManager.getSport(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= SportManager.searchSport(name=name,position=position,student=student,categories=categories,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;position= request.POST.get('position') if request.POST.get('position','').strip() else None;student= request.POST.get('student') if request.POST.get('student','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;   
    name=name if name else None ;position=position if position else {'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34} ;student=student if student else None ;categories=categories if categories else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;position = dict(position) if( position) else position ;student = str2List(student) if( student) else student ;categories = str2List(categories) if( categories) else categories ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=SportManager.updateSport(id=id,name=name,position=position,student=student,categories=categories,)
    else:
      # This is new entry request...
      res=SportManager.createSport(name=name,position=position,student=student,categories=categories,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =SportManager.deleteSport(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Sport_Student(request,id=None):
  res=None
  #If the request is coming for get to all Student_set
  if request.method == 'GET':
      res= SportManager.getSport_Student(id=id)

  #This is the implementation for POST request to add or delete Student
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    student=str2List(request.POST.get('student',None))
    if not student : return AutoHttpResponse(400,'Missing/Bad input: <student: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=SportManager.addSport_Student(id=id,student = student)
    else:
      # do a delete action
      res=SportManager.removeSport_Student(id=id,student = student)

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
def ajax_Sport_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));position = parseTriple(request.POST.get('position',None));student = parseTriple(request.POST.get('student',None));categories = parseTriple(request.POST.get('categories',None));
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
       res = SportManager.advSearchSport(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Sport_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = SportManager.minViewSport(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import AccountManager
@csrf_exempt
def ajax_Account(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;email= request.GET.get('email') if request.GET.get('email','').strip() else None;password_hash= request.GET.get('password_hash') if request.GET.get('password_hash','').strip() else None;salt_hash= request.GET.get('salt_hash') if request.GET.get('salt_hash','').strip() else None;active= request.GET.get('active') if request.GET.get('active','').strip() else None;clue= request.GET.get('clue') if request.GET.get('clue','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;password_hash = str(password_hash) if( password_hash) else password_hash ;salt_hash = str(salt_hash) if( salt_hash) else salt_hash ;active = str(active) if( active) else active ;clue = str(clue) if( clue) else clue ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Account or it's a search request
    if id is not None: 
      res= AccountManager.getAccount(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= AccountManager.searchAccount(name=name,email=email,password_hash=password_hash,salt_hash=salt_hash,active=active,clue=clue,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;email= request.POST.get('email') if request.POST.get('email','').strip() else None;password_hash= request.POST.get('password_hash') if request.POST.get('password_hash','').strip() else None;salt_hash= request.POST.get('salt_hash') if request.POST.get('salt_hash','').strip() else None;active= request.POST.get('active') if request.POST.get('active','').strip() else None;clue= request.POST.get('clue') if request.POST.get('clue','').strip() else None;   
    name=name if name else None ;email=email if email else None ;password_hash=password_hash if password_hash else None ;salt_hash=salt_hash if salt_hash else None ;active=active if active else None ;clue=clue if clue else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;password_hash = str(password_hash) if( password_hash) else password_hash ;salt_hash = str(salt_hash) if( salt_hash) else salt_hash ;active = str(active) if( active) else active ;clue = str(clue) if( clue) else clue ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=AccountManager.updateAccount(id=id,name=name,email=email,password_hash=password_hash,salt_hash=salt_hash,active=active,clue=clue,)
    else:
      # This is new entry request...
      res=AccountManager.createAccount(name=name,email=email,password_hash=password_hash,salt_hash=salt_hash,active=active,clue=clue,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =AccountManager.deleteAccount(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Account_Setting(request,id=None):
  res=None
  #If the request is coming for get to all Setting_set
  if request.method == 'GET':
      res= AccountManager.getAccount_Setting(id=id)

  #This is the implementation for POST request to add or delete Setting
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    setting=str2List(request.POST.get('setting',None))
    if not setting : return AutoHttpResponse(400,'Missing/Bad input: <setting: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=AccountManager.addAccount_Setting(id=id,setting = setting)
    else:
      # do a delete action
      res=AccountManager.removeAccount_Setting(id=id,setting = setting)

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
def ajax_Account_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));email = parseTriple(request.POST.get('email',None));password_hash = parseTriple(request.POST.get('password_hash',None));salt_hash = parseTriple(request.POST.get('salt_hash',None));active = parseTriple(request.POST.get('active',None));clue = parseTriple(request.POST.get('clue',None));
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
       res = AccountManager.advSearchAccount(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Account_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = AccountManager.minViewAccount(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import SettingManager
@csrf_exempt
def ajax_Setting(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;account= request.GET.get('account') if request.GET.get('account','').strip() else None;theme= request.GET.get('theme') if request.GET.get('theme','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;account = str2List(account) if( account) else account ;theme = str2List(theme) if( theme) else theme ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Setting or it's a search request
    if id is not None: 
      res= SettingManager.getSetting(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= SettingManager.searchSetting(name=name,account=account,theme=theme,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;account= request.POST.get('account') if request.POST.get('account','').strip() else None;theme= request.POST.get('theme') if request.POST.get('theme','').strip() else None;   
    name=name if name else None ;account=account if account else None ;theme=theme if theme else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;account = str2List(account) if( account) else account ;theme = str2List(theme) if( theme) else theme ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=SettingManager.updateSetting(id=id,name=name,account=account,theme=theme,)
    else:
      # This is new entry request...
      res=SettingManager.createSetting(name=name,account=account,theme=theme,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =SettingManager.deleteSetting(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Setting_Account(request,id=None):
  res=None
  #If the request is coming for get to all Account_set
  if request.method == 'GET':
      res= SettingManager.getSetting_Account(id=id)

  #This is the implementation for POST request to add or delete Account
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    account=str2List(request.POST.get('account',None))
    if not account : return AutoHttpResponse(400,'Missing/Bad input: <account: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=SettingManager.addSetting_Account(id=id,account = account)
    else:
      # do a delete action
      res=SettingManager.removeSetting_Account(id=id,account = account)

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
def ajax_Setting_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));account = parseTriple(request.POST.get('account',None));theme = parseTriple(request.POST.get('theme',None));
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
       res = SettingManager.advSearchSetting(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Setting_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = SettingManager.minViewSetting(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import FundManager
@csrf_exempt
def ajax_Fund(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;tenant= request.GET.get('tenant') if request.GET.get('tenant','').strip() else None;purpose= request.GET.get('purpose') if request.GET.get('purpose','').strip() else None;type= request.GET.get('type') if request.GET.get('type','').strip() else None;amount= request.GET.get('amount') if request.GET.get('amount','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;tenant = str(tenant) if( tenant) else tenant ;purpose = str(purpose) if( purpose) else purpose ;type = str2List(type) if( type) else type ;amount = int(amount) if( amount) else amount ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Fund or it's a search request
    if id is not None: 
      res= FundManager.getFund(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= FundManager.searchFund(name=name,tenant=tenant,purpose=purpose,type=type,amount=amount,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;tenant= request.POST.get('tenant') if request.POST.get('tenant','').strip() else None;purpose= request.POST.get('purpose') if request.POST.get('purpose','').strip() else None;type= request.POST.get('type') if request.POST.get('type','').strip() else None;amount= request.POST.get('amount') if request.POST.get('amount','').strip() else None;   
    name=name if name else None ;tenant=tenant if tenant else None ;purpose=purpose if purpose else None ;type=type if type else None ;amount=amount if amount else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;tenant = str(tenant) if( tenant) else tenant ;purpose = str(purpose) if( purpose) else purpose ;type = str2List(type) if( type) else type ;amount = int(amount) if( amount) else amount ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=FundManager.updateFund(id=id,name=name,tenant=tenant,purpose=purpose,type=type,amount=amount,)
    else:
      # This is new entry request...
      res=FundManager.createFund(name=name,tenant=tenant,purpose=purpose,type=type,amount=amount,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =FundManager.deleteFund(id)
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
def ajax_Fund_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));tenant = parseTriple(request.POST.get('tenant',None));purpose = parseTriple(request.POST.get('purpose',None));type = parseTriple(request.POST.get('type',None));amount = parseTriple(request.POST.get('amount',None));
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
       res = FundManager.advSearchFund(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Fund_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = FundManager.minViewFund(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import BookManager
@csrf_exempt
def ajax_Book(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;author= request.GET.get('author') if request.GET.get('author','').strip() else None;desc= request.GET.get('desc') if request.GET.get('desc','').strip() else None;count= request.GET.get('count') if request.GET.get('count','').strip() else None;price= request.GET.get('price') if request.GET.get('price','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;author = str(author) if( author) else author ;desc = str(desc) if( desc) else desc ;count = int(count) if( count) else count ;price = int(price) if( price) else price ;categories = str2List(categories) if( categories) else categories ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Book or it's a search request
    if id is not None: 
      res= BookManager.getBook(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= BookManager.searchBook(name=name,author=author,desc=desc,count=count,price=price,categories=categories,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;author= request.POST.get('author') if request.POST.get('author','').strip() else None;desc= request.POST.get('desc') if request.POST.get('desc','').strip() else None;count= request.POST.get('count') if request.POST.get('count','').strip() else None;price= request.POST.get('price') if request.POST.get('price','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;   
    name=name if name else None ;author=author if author else None ;desc=desc if desc else None ;count=count if count else None ;price=price if price else None ;categories=categories if categories else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;author = str(author) if( author) else author ;desc = str(desc) if( desc) else desc ;count = int(count) if( count) else count ;price = int(price) if( price) else price ;categories = str2List(categories) if( categories) else categories ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=BookManager.updateBook(id=id,name=name,author=author,desc=desc,count=count,price=price,categories=categories,)
    else:
      # This is new entry request...
      res=BookManager.createBook(name=name,author=author,desc=desc,count=count,price=price,categories=categories,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =BookManager.deleteBook(id)
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
      #name = parseTriple(request.POST.get('name',None));author = parseTriple(request.POST.get('author',None));desc = parseTriple(request.POST.get('desc',None));count = parseTriple(request.POST.get('count',None));price = parseTriple(request.POST.get('price',None));categories = parseTriple(request.POST.get('categories',None));
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
       res = BookManager.advSearchBook(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Book_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = BookManager.minViewBook(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import EventManager
@csrf_exempt
def ajax_Event(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;details= request.GET.get('details') if request.GET.get('details','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;date= request.GET.get('date') if request.GET.get('date','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;date = date(date) if( date) else date ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Event or it's a search request
    if id is not None: 
      res= EventManager.getEvent(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= EventManager.searchEvent(name=name,details=details,categories=categories,date=date,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;details= request.POST.get('details') if request.POST.get('details','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;date= request.POST.get('date') if request.POST.get('date','').strip() else None;   
    name=name if name else None ;details=details if details else None ;categories=categories if categories else None ;date=date if date else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;date = date(date) if( date) else date ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=EventManager.updateEvent(id=id,name=name,details=details,categories=categories,date=date,)
    else:
      # This is new entry request...
      res=EventManager.createEvent(name=name,details=details,categories=categories,date=date,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =EventManager.deleteEvent(id)
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
def ajax_Event_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));details = parseTriple(request.POST.get('details',None));categories = parseTriple(request.POST.get('categories',None));date = parseTriple(request.POST.get('date',None));
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
       res = EventManager.advSearchEvent(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Event_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = EventManager.minViewEvent(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import DisciplineManager
@csrf_exempt
def ajax_Discipline(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;details= request.GET.get('details') if request.GET.get('details','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Discipline or it's a search request
    if id is not None: 
      res= DisciplineManager.getDiscipline(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= DisciplineManager.searchDiscipline(name=name,details=details,categories=categories,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;details= request.POST.get('details') if request.POST.get('details','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;   
    name=name if name else None ;details=details if details else None ;categories=categories if categories else None ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=DisciplineManager.updateDiscipline(id=id,name=name,details=details,categories=categories,)
    else:
      # This is new entry request...
      res=DisciplineManager.createDiscipline(name=name,details=details,categories=categories,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =DisciplineManager.deleteDiscipline(id)
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
def ajax_Discipline_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));details = parseTriple(request.POST.get('details',None));categories = parseTriple(request.POST.get('categories',None));
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
       res = DisciplineManager.advSearchDiscipline(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Discipline_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = DisciplineManager.minViewDiscipline(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import NoticeManager
@csrf_exempt
def ajax_Notice(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    title= request.GET.get('title') if request.GET.get('title','').strip() else None;details= request.GET.get('details') if request.GET.get('details','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      title = str(title) if( title) else title ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Notice or it's a search request
    if id is not None: 
      res= NoticeManager.getNotice(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= NoticeManager.searchNotice(title=title,details=details,categories=categories,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    title= request.POST.get('title') if request.POST.get('title','').strip() else None;details= request.POST.get('details') if request.POST.get('details','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;   
    title=title if title else None ;details=details if details else None ;categories=categories if categories else None ;    
    #data Must be Normalized to required DataType..
    try:
      title = str(title) if( title) else title ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=NoticeManager.updateNotice(id=id,title=title,details=details,categories=categories,)
    else:
      # This is new entry request...
      res=NoticeManager.createNotice(title=title,details=details,categories=categories,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =NoticeManager.deleteNotice(id)
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
def ajax_Notice_asearch(request): # We support POST only .
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
      #title = parseTriple(request.POST.get('title',None));details = parseTriple(request.POST.get('details',None));categories = parseTriple(request.POST.get('categories',None));
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
       res = NoticeManager.advSearchNotice(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Notice_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = NoticeManager.minViewNotice(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import InstrumentManager
@csrf_exempt
def ajax_Instrument(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;details= request.GET.get('details') if request.GET.get('details','').strip() else None;categories= request.GET.get('categories') if request.GET.get('categories','').strip() else None;count= request.GET.get('count') if request.GET.get('count','').strip() else None;
    # NOTE: DONT POPULATE DEFAULT HERE.. WE WANT TO SEARCH HERE ONLY....
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;count = int(count) if( count) else count ;
      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # if Id is null, get the perticular Instrument or it's a search request
    if id is not None: 
      res= InstrumentManager.getInstrument(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= InstrumentManager.searchInstrument(name=name,details=details,categories=categories,count=count,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;details= request.POST.get('details') if request.POST.get('details','').strip() else None;categories= request.POST.get('categories') if request.POST.get('categories','').strip() else None;count= request.POST.get('count') if request.POST.get('count','').strip() else None;   
    name=name if name else None ;details=details if details else None ;categories=categories if categories else None ;count=count if count else 0 ;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;details = str(details) if( details) else details ;categories = str2List(categories) if( categories) else categories ;count = int(count) if( count) else count ;      
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,getCustomException(e))
    # Update request if id is not null. 
    if id is not None: 
      res=InstrumentManager.updateInstrument(id=id,name=name,details=details,categories=categories,count=count,)
    else:
      # This is new entry request...
      res=InstrumentManager.createInstrument(name=name,details=details,categories=categories,count=count,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =InstrumentManager.deleteInstrument(id)
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
def ajax_Instrument_asearch(request): # We support POST only .
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
      #name = parseTriple(request.POST.get('name',None));details = parseTriple(request.POST.get('details',None));categories = parseTriple(request.POST.get('categories',None));count = parseTriple(request.POST.get('count',None));
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
       res = InstrumentManager.advSearchInstrument(id=id,query_str=Qstr,orderBy=orderBy,include=include,exclude=exclude)
    except:
      D_LOG()
      return AutoHttpResponse(400,'list item is not speared properly! Is your list field looks like: tags = [1,2,3] or tag1=%5B1%2C2%2C3%5D ?')
  return AutoHttpResponse(res=res)


@csrf_exempt
def ajax_Instrument_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = InstrumentManager.minViewInstrument(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  

