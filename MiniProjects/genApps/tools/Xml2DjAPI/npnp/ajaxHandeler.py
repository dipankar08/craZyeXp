import pdb
from common import D_LOG
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
  


from .api import StudentManager
@csrf_exempt
def ajax_Student(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;email= request.GET.get('email') if request.GET.get('email','').strip() else None;phone= request.GET.get('phone') if request.GET.get('phone','').strip() else None;address= request.GET.get('address') if request.GET.get('address','').strip() else None;dob= request.GET.get('dob') if request.GET.get('dob','').strip() else None;doj= request.GET.get('doj') if request.GET.get('doj','').strip() else None;gender= request.GET.get('gender') if request.GET.get('gender','').strip() else None;Parent= request.GET.get('Parent') if request.GET.get('Parent','').strip() else None;roll= request.GET.get('roll') if request.GET.get('roll','').strip() else None;section= request.GET.get('section') if request.GET.get('section','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;address = str(address) if( address) else address ;dob = str(dob) if( dob) else dob ;doj = date(doj) if( doj) else doj ;gender = str(gender) if( gender) else gender ;Parent = int(Parent) if( Parent) else Parent ;roll = str(roll) if( roll) else roll ;section = str2List(section) if( section) else section ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Student or it's a search request
    if id is not None: 
      res= StudentManager.getStudent(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= StudentManager.searchStudent(name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,Parent=Parent,roll=roll,section=section,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;email= request.POST.get('email') if request.POST.get('email','').strip() else None;phone= request.POST.get('phone') if request.POST.get('phone','').strip() else None;address= request.POST.get('address') if request.POST.get('address','').strip() else None;dob= request.POST.get('dob') if request.POST.get('dob','').strip() else None;doj= request.POST.get('doj') if request.POST.get('doj','').strip() else None;gender= request.POST.get('gender') if request.POST.get('gender','').strip() else None;Parent= request.POST.get('Parent') if request.POST.get('Parent','').strip() else None;roll= request.POST.get('roll') if request.POST.get('roll','').strip() else None;section= request.POST.get('section') if request.POST.get('section','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;address = str(address) if( address) else address ;dob = str(dob) if( dob) else dob ;doj = date(doj) if( doj) else doj ;gender = str(gender) if( gender) else gender ;Parent = int(Parent) if( Parent) else Parent ;roll = str(roll) if( roll) else roll ;section = str2List(section) if( section) else section ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=StudentManager.updateStudent(id=id,name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,Parent=Parent,roll=roll,section=section,)
    else:
      # This is new entry request...
      res=StudentManager.createStudent(name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,Parent=Parent,roll=roll,section=section,)
    
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
    Parent=str2List(request.POST.get('Parent',None))
    if not Parent : return AutoHttpResponse(400,'Missing/Bad input: <Parent: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Parent(id=id,Parent = Parent)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Parent(id=id,Parent = Parent)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Student_Class(request,id=None):
  res=None
  #If the request is coming for get to all Class_set
  if request.method == 'GET':
      res= StudentManager.getStudent_Class(id=id)

  #This is the implementation for POST request to add or delete Class
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    class=str2List(request.POST.get('class',None))
    if not class : return AutoHttpResponse(400,'Missing/Bad input: <class: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=StudentManager.addStudent_Class(id=id,class = class)
    else:
      # do a delete action
      res=StudentManager.removeStudent_Class(id=id,class = class)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



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


from .api import EmployeeManager
@csrf_exempt
def ajax_Employee(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Employee or it's a search request
    if id is not None: 
      res= EmployeeManager.getEmployee(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= EmployeeManager.searchEmployee(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=EmployeeManager.updateEmployee(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=EmployeeManager.createEmployee(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =EmployeeManager.deleteEmployee(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Employee_Class(request,id=None):
  res=None
  #If the request is coming for get to all Class_set
  if request.method == 'GET':
      res= EmployeeManager.getEmployee_Class(id=id)

  #This is the implementation for POST request to add or delete Class
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    class=str2List(request.POST.get('class',None))
    if not class : return AutoHttpResponse(400,'Missing/Bad input: <class: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=EmployeeManager.addEmployee_Class(id=id,class = class)
    else:
      # do a delete action
      res=EmployeeManager.removeEmployee_Class(id=id,class = class)

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
def ajax_Employee_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = EmployeeManager.minViewEmployee(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import ParentManager
@csrf_exempt
def ajax_Parent(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;email= request.GET.get('email') if request.GET.get('email','').strip() else None;phone= request.GET.get('phone') if request.GET.get('phone','').strip() else None;occupation= request.GET.get('occupation') if request.GET.get('occupation','').strip() else None;address= request.GET.get('address') if request.GET.get('address','').strip() else None;income= request.GET.get('income') if request.GET.get('income','').strip() else None;relationship= request.GET.get('relationship') if request.GET.get('relationship','').strip() else None;secondary_contact= request.GET.get('secondary_contact') if request.GET.get('secondary_contact','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;occupation = str(occupation) if( occupation) else occupation ;address = str(address) if( address) else address ;income = str(income) if( income) else income ;relationship = str(relationship) if( relationship) else relationship ;secondary_contact = str(secondary_contact) if( secondary_contact) else secondary_contact ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
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
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;email = str(email) if( email) else email ;phone = str(phone) if( phone) else phone ;occupation = str(occupation) if( occupation) else occupation ;address = str(address) if( address) else address ;income = str(income) if( income) else income ;relationship = str(relationship) if( relationship) else relationship ;secondary_contact = str(secondary_contact) if( secondary_contact) else secondary_contact ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
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
def ajax_Parent_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = ParentManager.minViewParent(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import ClassManager
@csrf_exempt
def ajax_Class(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;room= request.GET.get('room') if request.GET.get('room','').strip() else None;class_teacher= request.GET.get('class_teacher') if request.GET.get('class_teacher','').strip() else None;subjects= request.GET.get('subjects') if request.GET.get('subjects','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;room = str(room) if( room) else room ;class_teacher = int(class_teacher) if( class_teacher) else class_teacher ;subjects = int(subjects) if( subjects) else subjects ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Class or it's a search request
    if id is not None: 
      res= ClassManager.getClass(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= ClassManager.searchClass(name=name,room=room,class_teacher=class_teacher,subjects=subjects,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;room= request.POST.get('room') if request.POST.get('room','').strip() else None;class_teacher= request.POST.get('class_teacher') if request.POST.get('class_teacher','').strip() else None;subjects= request.POST.get('subjects') if request.POST.get('subjects','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;room = str(room) if( room) else room ;class_teacher = int(class_teacher) if( class_teacher) else class_teacher ;subjects = int(subjects) if( subjects) else subjects ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=ClassManager.updateClass(id=id,name=name,room=room,class_teacher=class_teacher,subjects=subjects,)
    else:
      # This is new entry request...
      res=ClassManager.createClass(name=name,room=room,class_teacher=class_teacher,subjects=subjects,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =ClassManager.deleteClass(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Class_Employee(request,id=None):
  res=None
  #If the request is coming for get to all Employee_set
  if request.method == 'GET':
      res= ClassManager.getClass_Employee(id=id)

  #This is the implementation for POST request to add or delete Employee
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    class_teacher=str2List(request.POST.get('class_teacher',None))
    if not class_teacher : return AutoHttpResponse(400,'Missing/Bad input: <class_teacher: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ClassManager.addClass_Employee(id=id,class_teacher = class_teacher)
    else:
      # do a delete action
      res=ClassManager.removeClass_Employee(id=id,class_teacher = class_teacher)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Class_Subject(request,id=None):
  res=None
  #If the request is coming for get to all Subject_set
  if request.method == 'GET':
      res= ClassManager.getClass_Subject(id=id)

  #This is the implementation for POST request to add or delete Subject
  elif request.method == 'POST':
    action=request.POST.get('action',None)
    if not action: return AutoHttpResponse(400,'Missing/Bad input: <action: add|remove > ?')
    subjects=str2List(request.POST.get('subjects',None))
    if not subjects : return AutoHttpResponse(400,'Missing/Bad input: <subjects: <id> > ?')
    # Update request if id is not null.
    if action.lower() == 'add':
      res=ClassManager.addClass_Subject(id=id,subjects = subjects)
    else:
      # do a delete action
      res=ClassManager.removeClass_Subject(id=id,subjects = subjects)

  #Return the result after converting into json
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')



@csrf_exempt
def ajax_Class_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = ClassManager.minViewClass(page=page,limit=limit)
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
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;uid= request.GET.get('uid') if request.GET.get('uid','').strip() else None;syllabus= request.GET.get('syllabus') if request.GET.get('syllabus','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;teacher= request.GET.get('teacher') if request.GET.get('teacher','').strip() else None;categorise= request.GET.get('categorise') if request.GET.get('categorise','').strip() else None;group= request.GET.get('group') if request.GET.get('group','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;uid = str(uid) if( uid) else uid ;syllabus = str(syllabus) if( syllabus) else syllabus ;accid = int(accid) if( accid) else accid ;teacher = int(teacher) if( teacher) else teacher ;categorise = str2List(categorise) if( categorise) else categorise ;group = str2List(group) if( group) else group ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Subject or it's a search request
    if id is not None: 
      res= SubjectManager.getSubject(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= SubjectManager.searchSubject(name=name,uid=uid,syllabus=syllabus,accid=accid,teacher=teacher,categorise=categorise,group=group,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;uid= request.POST.get('uid') if request.POST.get('uid','').strip() else None;syllabus= request.POST.get('syllabus') if request.POST.get('syllabus','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;teacher= request.POST.get('teacher') if request.POST.get('teacher','').strip() else None;categorise= request.POST.get('categorise') if request.POST.get('categorise','').strip() else None;group= request.POST.get('group') if request.POST.get('group','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;uid = str(uid) if( uid) else uid ;syllabus = str(syllabus) if( syllabus) else syllabus ;accid = int(accid) if( accid) else accid ;teacher = int(teacher) if( teacher) else teacher ;categorise = str2List(categorise) if( categorise) else categorise ;group = str2List(group) if( group) else group ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=SubjectManager.updateSubject(id=id,name=name,uid=uid,syllabus=syllabus,accid=accid,teacher=teacher,categorise=categorise,group=group,)
    else:
      # This is new entry request...
      res=SubjectManager.createSubject(name=name,uid=uid,syllabus=syllabus,accid=accid,teacher=teacher,categorise=categorise,group=group,)
    
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
def ajax_Subject_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = SubjectManager.minViewSubject(page=page,limit=limit)
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
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Mark or it's a search request
    if id is not None: 
      res= MarkManager.getMark(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= MarkManager.searchMark(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=MarkManager.updateMark(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=MarkManager.createMark(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =MarkManager.deleteMark(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Result or it's a search request
    if id is not None: 
      res= ResultManager.getResult(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= ResultManager.searchResult(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=ResultManager.updateResult(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=ResultManager.createResult(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =ResultManager.deleteResult(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import ExamManager
@csrf_exempt
def ajax_Exam(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Exam or it's a search request
    if id is not None: 
      res= ExamManager.getExam(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= ExamManager.searchExam(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=ExamManager.updateExam(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=ExamManager.createExam(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =ExamManager.deleteExam(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import AttendanceManager
@csrf_exempt
def ajax_Attendance(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Attendance or it's a search request
    if id is not None: 
      res= AttendanceManager.getAttendance(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= AttendanceManager.searchAttendance(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=AttendanceManager.updateAttendance(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=AttendanceManager.createAttendance(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =AttendanceManager.deleteAttendance(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Fees or it's a search request
    if id is not None: 
      res= FeesManager.getFees(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= FeesManager.searchFees(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=FeesManager.updateFees(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=FeesManager.createFees(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =FeesManager.deleteFees(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import FundManager
@csrf_exempt
def ajax_Fund(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Fund or it's a search request
    if id is not None: 
      res= FundManager.getFund(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= FundManager.searchFund(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=FundManager.updateFund(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=FundManager.createFund(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =FundManager.deleteFund(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import LibBookManager
@csrf_exempt
def ajax_LibBook(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular LibBook or it's a search request
    if id is not None: 
      res= LibBookManager.getLibBook(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= LibBookManager.searchLibBook(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=LibBookManager.updateLibBook(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=LibBookManager.createLibBook(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =LibBookManager.deleteLibBook(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_LibBook_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = LibBookManager.minViewLibBook(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import LeavesManager
@csrf_exempt
def ajax_Leaves(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Leaves or it's a search request
    if id is not None: 
      res= LeavesManager.getLeaves(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= LeavesManager.searchLeaves(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=LeavesManager.updateLeaves(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=LeavesManager.createLeaves(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =LeavesManager.deleteLeaves(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


@csrf_exempt
def ajax_Leaves_min_view(request):
  res=None
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    res = LeavesManager.minViewLeaves(page=page,limit=limit)
    return AutoHttpResponse(res=res)
  else:
    return AutoHttpResponse(501)  


from .api import PayRollManager
@csrf_exempt
def ajax_PayRoll(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular PayRoll or it's a search request
    if id is not None: 
      res= PayRollManager.getPayRoll(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= PayRollManager.searchPayRoll(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=PayRollManager.updatePayRoll(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=PayRollManager.createPayRoll(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =PayRollManager.deletePayRoll(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import SportManager
@csrf_exempt
def ajax_Sport(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Sport or it's a search request
    if id is not None: 
      res= SportManager.getSport(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= SportManager.searchSport(name=name,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=SportManager.updateSport(id=id,name=name,)
    else:
      # This is new entry request...
      res=SportManager.createSport(name=name,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =SportManager.deleteSport(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import EventManager
@csrf_exempt
def ajax_Event(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Event or it's a search request
    if id is not None: 
      res= EventManager.getEvent(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= EventManager.searchEvent(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=EventManager.updateEvent(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=EventManager.createEvent(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =EventManager.deleteEvent(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Discipline or it's a search request
    if id is not None: 
      res= DisciplineManager.getDiscipline(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= DisciplineManager.searchDiscipline(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=DisciplineManager.updateDiscipline(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=DisciplineManager.createDiscipline(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =DisciplineManager.deleteDiscipline(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Notice or it's a search request
    if id is not None: 
      res= NoticeManager.getNotice(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= NoticeManager.searchNotice(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=NoticeManager.updateNotice(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=NoticeManager.createNotice(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =NoticeManager.deleteNotice(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import AccountManager
@csrf_exempt
def ajax_Account(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Account or it's a search request
    if id is not None: 
      res= AccountManager.getAccount(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= AccountManager.searchAccount(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=AccountManager.updateAccount(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=AccountManager.createAccount(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =AccountManager.deleteAccount(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import InstrumentManager
@csrf_exempt
def ajax_Instrument(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Instrument or it's a search request
    if id is not None: 
      res= InstrumentManager.getInstrument(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= InstrumentManager.searchInstrument(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=InstrumentManager.updateInstrument(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=InstrumentManager.createInstrument(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =InstrumentManager.deleteInstrument(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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


from .api import SettingManager
@csrf_exempt
def ajax_Setting(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name= request.GET.get('name') if request.GET.get('name','').strip() else None;accid= request.GET.get('accid') if request.GET.get('accid','').strip() else None;
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # if Id is null, get the perticular Setting or it's a search request
    if id is not None: 
      res= SettingManager.getSetting(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= SettingManager.searchSetting(name=name,accid=accid,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name= request.POST.get('name') if request.POST.get('name','').strip() else None;accid= request.POST.get('accid') if request.POST.get('accid','').strip() else None;    
    #data Must be Normalized to required DataType..
    try:
      name = str(name) if( name) else name ;accid = int(accid) if( accid) else accid ;
    except Exception,e:
      D_LOG()
      return AutoHttpResponse(400,'Type mismatch!you might be trying to enter Wrong datatype:help:'+str(e))
    # Update request if id is not null. 
    if id is not None: 
      res=SettingManager.updateSetting(id=id,name=name,accid=accid,)
    else:
      # This is new entry request...
      res=SettingManager.createSetting(name=name,accid=accid,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =SettingManager.deleteSetting(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')


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

