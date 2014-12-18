import pdb
from common import *
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *

from .models import Parent
class ParentManager:
  @staticmethod
  def createParent(name=None,email=None,phone=None,occupation=None,address=None,income=None,relationship=None,secondary_contact=None,): #Crete an Obj
    try:
      
      
      
      t = Parent(name=name,email=email,phone=phone,occupation=occupation,address=address,income=income,relationship=relationship,secondary_contact=secondary_contact,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Parent got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Parent:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getParent(id): # get Json
    try:
      t=Parent.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Parent returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Parent:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getParentObj(id): #get Obj
    try:
      t=Parent.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Parent Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Parent:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateParent(id,name=None,email=None,phone=None,occupation=None,address=None,income=None,relationship=None,secondary_contact=None, ): #Update Obj
    try:
      res=ParentManager.getParentObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;t.email = email if email is not None else t.email;t.phone = phone if phone is not None else t.phone;t.occupation = occupation if occupation is not None else t.occupation;t.address = address if address is not None else t.address;t.income = income if income is not None else t.income;t.relationship = relationship if relationship is not None else t.relationship;t.secondary_contact = secondary_contact if secondary_contact is not None else t.secondary_contact;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Parent Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Parent:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteParent(id): #Delete Obj
    try:
      d=Parent.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Parent deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Parent:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchParent(name=None,email=None,phone=None,occupation=None,address=None,income=None,relationship=None,secondary_contact=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if email is not None: Query['email__contains']=email
      if phone is not None: Query['phone__contains']=phone
      if occupation is not None: Query['occupation__contains']=occupation
      if address is not None: Query['address__contains']=address
      if income is not None: Query['income__contains']=income
      if relationship is not None: Query['relationship__contains']=relationship
      if secondary_contact is not None: Query['secondary_contact__contains']=secondary_contact #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'phone', 'id']
      dd=Parent.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Parent search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Parent:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getParent_Student(id):
    try:
       res=ParentManager.getParentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.student_set.all() ]
       return {'res':res,'status':'info','msg':'all student for the Parent returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addParent_Student(id,student,flush=False):
    assert (isinstance(student,list)),"student must be a list type."
    try:
      res=ParentManager.getParentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.student.clear()
      for i in student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.student_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.student_set.all() ]
      return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeParent_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
      res=ParentManager.getParentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in student:
          # get the object..
          obj=StudentManager.getStudentObj(i)['res']
          if obj is not None:
            t.student_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.student_set.all() ]
      return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchParent(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Parent Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Parent.objects.filter(Qstr)
      else:
        dd=Parent.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'phone', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Parent search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Parent!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewParent(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'phone', 'id']
      dd=Parent.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Parent  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Parent!','sys_error':str(e)}


from .models import Employee
class EmployeeManager:
  @staticmethod
  def createEmployee(name=None,uid=None,address=None,age=None,designation=None,rank=None,max_qualification=None,meretarial_status=None,gender=None,dob=None,doj=None,categories=None,): #Crete an Obj
    try:
      
      
      
      t = Employee(name=name,uid=uid,address=address,age=age,designation=designation,rank=rank,max_qualification=max_qualification,meretarial_status=meretarial_status,gender=gender,dob=dob,doj=doj,categories=categories,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Employee got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Employee:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getEmployee(id): # get Json
    try:
      t=Employee.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Employee returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Employee:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getEmployeeObj(id): #get Obj
    try:
      t=Employee.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Employee Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Employee:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateEmployee(id,name=None,uid=None,address=None,age=None,designation=None,rank=None,max_qualification=None,meretarial_status=None,gender=None,dob=None,doj=None,categories=None, ): #Update Obj
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;t.uid = uid if uid is not None else t.uid;t.address = address if address is not None else t.address;t.age = age if age is not None else t.age;t.designation = designation if designation is not None else t.designation;t.rank = rank if rank is not None else t.rank;t.max_qualification = max_qualification if max_qualification is not None else t.max_qualification;t.meretarial_status = meretarial_status if meretarial_status is not None else t.meretarial_status;t.gender = gender if gender is not None else t.gender;t.dob = dob if dob is not None else t.dob;t.doj = doj if doj is not None else t.doj;t.categories = categories if categories is not None else t.categories;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Employee Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Employee:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteEmployee(id): #Delete Obj
    try:
      d=Employee.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Employee deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Employee:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchEmployee(name=None,uid=None,address=None,age=None,designation=None,rank=None,max_qualification=None,meretarial_status=None,gender=None,dob=None,doj=None,categories=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if uid is not None: Query['uid__contains']=uid
      if address is not None: Query['address__contains']=address
      if age is not None: Query['age']=age
      if designation is not None: Query['designation__contains']=designation
      if rank is not None: Query['rank__contains']=rank
      if max_qualification is not None: Query['max_qualification__contains']=max_qualification
      if meretarial_status is not None: Query['meretarial_status__contains']=meretarial_status
      if gender is not None: Query['gender__contains']=gender
      if dob is not None: Query['dob__contains']=dob
      if doj is not None: Query['doj']=doj
      if categories is not None: Query['categories']=categories #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'uid', u'name', 'id']
      dd=Employee.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Employee search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Employee:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getEmployee_Subject(id):
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.subject_set.all() ]
       return {'res':res,'status':'info','msg':'all subject for the Employee returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addEmployee_Subject(id,subject,flush=False):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.subject.clear()
      for i in subject:
           # get the object..
           obj=SubjectManager.getSubjectObj(i)['res']
           if obj is not None:
             t.subject_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.subject_set.all() ]
      return {'res':res,'status':'info','msg':'all subject having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeEmployee_Subject(id,subject):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in subject:
          # get the object..
          obj=SubjectManager.getSubjectObj(i)['res']
          if obj is not None:
            t.subject_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.subject_set.all() ]
      return {'res':res,'status':'info','msg':'all subject having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some subject not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getEmployee_MyClass(id):
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.myclass_set.all() ]
       return {'res':res,'status':'info','msg':'all myclass for the Employee returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get MyClass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addEmployee_MyClass(id,myclass,flush=False):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.myclass.clear()
      for i in myclass:
           # get the object..
           obj=MyClassManager.getMyClassObj(i)['res']
           if obj is not None:
             t.myclass_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.myclass_set.all() ]
      return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get myclass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeEmployee_MyClass(id,myclass):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in myclass:
          # get the object..
          obj=MyClassManager.getMyClassObj(i)['res']
          if obj is not None:
            t.myclass_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.myclass_set.all() ]
      return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some myclass not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getEmployee_Exam(id):
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.exam_set.all() ]
       return {'res':res,'status':'info','msg':'all exam for the Employee returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addEmployee_Exam(id,exam,flush=False):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.exam.clear()
      for i in exam:
           # get the object..
           obj=ExamManager.getExamObj(i)['res']
           if obj is not None:
             t.exam_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.exam_set.all() ]
      return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeEmployee_Exam(id,exam):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in exam:
          # get the object..
          obj=ExamManager.getExamObj(i)['res']
          if obj is not None:
            t.exam_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.exam_set.all() ]
      return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some exam not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchEmployee(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Employee Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Employee.objects.filter(Qstr)
      else:
        dd=Employee.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'uid', u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Employee search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Employee!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewEmployee(page=None,limit=None):
    try:
      res =None
      include =[u'uid', u'name', 'id']
      dd=Employee.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Employee  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Employee!','sys_error':str(e)}


from .models import Subject
class SubjectManager:
  @staticmethod
  def createSubject(name=None,uid=None,syllabus=None,ref_book=None,teacher=None,categorise=None,group=None,mark_division={'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34},): #Crete an Obj
    try:
      if categorise and not set(categorise).issubset(set([u'practical', u'theoretical'])) : return {'res':None,'status':'error','msg':"categorise must be either of [u'practical', u'theoretical'] ",'sys_error':''};
      if group and not set(group).issubset(set([u'science', u'arts', u'comm'])) : return {'res':None,'status':'error','msg':"group must be either of [u'science', u'arts', u'comm'] ",'sys_error':''};
      
      
      
      t = Subject(name=name,uid=uid,syllabus=syllabus,ref_book=ref_book,categorise=categorise,group=group,mark_division=mark_division,)
      
      t.save()
      if teacher: SubjectManager.addSubject_Employee(t.id,teacher,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Subject got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getSubject(id): # get Json
    try:
      t=Subject.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Subject returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Subject:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getSubjectObj(id): #get Obj
    try:
      t=Subject.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Subject Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Subject:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateSubject(id,name=None,uid=None,syllabus=None,ref_book=None,teacher=None,categorise=None,group=None,mark_division={'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34}, ): #Update Obj
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categorise and not set(categorise).issubset(set([u'practical', u'theoretical'])) : return {'res':None,'status':'error','msg':"categorise must be either of [u'practical', u'theoretical'] ",'sys_error':''};
      if group and not set(group).issubset(set([u'science', u'arts', u'comm'])) : return {'res':None,'status':'error','msg':"group must be either of [u'science', u'arts', u'comm'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.uid = uid if uid is not None else t.uid;t.syllabus = syllabus if syllabus is not None else t.syllabus;t.ref_book = ref_book if ref_book is not None else t.ref_book;t.categorise = categorise if categorise is not None else t.categorise;t.group = group if group is not None else t.group;t.mark_division = mark_division if mark_division is not None else t.mark_division;             
      t.save()
      if teacher: SubjectManager.addSubject_Employee(t.id,teacher,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Subject Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteSubject(id): #Delete Obj
    try:
      d=Subject.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Subject deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Subject:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchSubject(name=None,uid=None,syllabus=None,ref_book=None,teacher=None,categorise=None,group=None,mark_division={'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34},page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if uid is not None: Query['uid__contains']=uid
      if syllabus is not None: Query['syllabus__contains']=syllabus
      if ref_book is not None: Query['ref_book__contains']=ref_book
      if teacher is not None: Query['teacher']=teacher
      if categorise is not None: Query['categorise']=categorise
      if group is not None: Query['group']=group
      if mark_division is not None: Query['mark_division']=mark_division #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'categorise', u'group', 'id']
      dd=Subject.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Subject search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Subject:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getSubject_Employee(id):
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.teacher.all() ]
       return {'res':res,'status':'info','msg':'all teacher for the Subject returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get teacher:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addSubject_Employee(id,teacher,flush=False):
    assert (isinstance(teacher,list)),"teacher must be a list type."
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.teacher.clear()
       for i in teacher:
           # get the object..
           obj=EmployeeManager.getEmployeeObj(i)['res']
           if obj is not None:
             t.teacher.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.teacher.all() ]
       return {'res':res,'status':'info','msg':'all teacher having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get teacher:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeSubject_Employee(id,teacher):
    assert (isinstance(teacher,list)),"teacher must be a list type."
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in teacher:
           # get the object..
           obj=EmployeeManager.getEmployeeObj(i)['res']
           if obj is not None:
              t.teacher.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.teacher.all() ]
       return {'res':res,'status':'info','msg':'all teacher having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some teacher not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getSubject_MyClass(id):
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.myclass_set.all() ]
       return {'res':res,'status':'info','msg':'all myclass for the Subject returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get MyClass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addSubject_MyClass(id,myclass,flush=False):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.myclass.clear()
      for i in myclass:
           # get the object..
           obj=MyClassManager.getMyClassObj(i)['res']
           if obj is not None:
             t.myclass_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.myclass_set.all() ]
      return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get myclass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeSubject_MyClass(id,myclass):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in myclass:
          # get the object..
          obj=MyClassManager.getMyClassObj(i)['res']
          if obj is not None:
            t.myclass_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.myclass_set.all() ]
      return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some myclass not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getSubject_Exam(id):
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.exam_set.all() ]
       return {'res':res,'status':'info','msg':'all exam for the Subject returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addSubject_Exam(id,exam,flush=False):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.exam.clear()
      for i in exam:
           # get the object..
           obj=ExamManager.getExamObj(i)['res']
           if obj is not None:
             t.exam_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.exam_set.all() ]
      return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeSubject_Exam(id,exam):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in exam:
          # get the object..
          obj=ExamManager.getExamObj(i)['res']
          if obj is not None:
            t.exam_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.exam_set.all() ]
      return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some exam not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getSubject_Mark(id):
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.mark_set.all() ]
       return {'res':res,'status':'info','msg':'all mark for the Subject returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addSubject_Mark(id,mark,flush=False):
    assert (isinstance(mark,list)),"mark must be a list type."
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.mark.clear()
      for i in mark:
           # get the object..
           obj=MarkManager.getMarkObj(i)['res']
           if obj is not None:
             t.mark_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.mark_set.all() ]
      return {'res':res,'status':'info','msg':'all mark having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeSubject_Mark(id,mark):
    assert (isinstance(mark,list)),"mark must be a list type."
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in mark:
          # get the object..
          obj=MarkManager.getMarkObj(i)['res']
          if obj is not None:
            t.mark_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.mark_set.all() ]
      return {'res':res,'status':'info','msg':'all mark having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some mark not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchSubject(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Subject Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Subject.objects.filter(Qstr)
      else:
        dd=Subject.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'categorise', u'group', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Subject search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Subject!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewSubject(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'categorise', u'group', 'id']
      dd=Subject.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Subject  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Subject!','sys_error':str(e)}


from .models import MyClass
class MyClassManager:
  @staticmethod
  def createMyClass(name=None,room=None,class_teacher=None,subjects=None,): #Crete an Obj
    try:
      
      
      
      t = MyClass(name=name,room=room,)
      
      t.save()
      if class_teacher: MyClassManager.addMyClass_Employee(t.id,class_teacher,flush=True);
      if subjects: MyClassManager.addMyClass_Subject(t.id,subjects,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New MyClass got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create MyClass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getMyClass(id): # get Json
    try:
      t=MyClass.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'MyClass returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive MyClass:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getMyClassObj(id): #get Obj
    try:
      t=MyClass.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'MyClass Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object MyClass:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateMyClass(id,name=None,room=None,class_teacher=None,subjects=None, ): #Update Obj
    try:
      res=MyClassManager.getMyClassObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;t.room = room if room is not None else t.room;             
      t.save()
      if class_teacher: MyClassManager.addMyClass_Employee(t.id,class_teacher,flush=True);
      if subjects: MyClassManager.addMyClass_Subject(t.id,subjects,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'MyClass Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update MyClass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteMyClass(id): #Delete Obj
    try:
      d=MyClass.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one MyClass deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete MyClass:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchMyClass(name=None,room=None,class_teacher=None,subjects=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if room is not None: Query['room__contains']=room
      if class_teacher is not None: Query['class_teacher']=class_teacher
      if subjects is not None: Query['subjects']=subjects #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=MyClass.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'MyClass search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search MyClass:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getMyClass_Employee(id):
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.class_teacher.all() ]
       return {'res':res,'status':'info','msg':'all class_teacher for the MyClass returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get class_teacher:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMyClass_Employee(id,class_teacher,flush=False):
    assert (isinstance(class_teacher,list)),"class_teacher must be a list type."
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.class_teacher.clear()
       for i in class_teacher:
           # get the object..
           obj=EmployeeManager.getEmployeeObj(i)['res']
           if obj is not None:
             t.class_teacher.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.class_teacher.all() ]
       return {'res':res,'status':'info','msg':'all class_teacher having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get class_teacher:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMyClass_Employee(id,class_teacher):
    assert (isinstance(class_teacher,list)),"class_teacher must be a list type."
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in class_teacher:
           # get the object..
           obj=EmployeeManager.getEmployeeObj(i)['res']
           if obj is not None:
              t.class_teacher.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.class_teacher.all() ]
       return {'res':res,'status':'info','msg':'all class_teacher having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some class_teacher not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getMyClass_Subject(id):
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.subjects.all() ]
       return {'res':res,'status':'info','msg':'all subjects for the MyClass returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get subjects:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMyClass_Subject(id,subjects,flush=False):
    assert (isinstance(subjects,list)),"subjects must be a list type."
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.subjects.clear()
       for i in subjects:
           # get the object..
           obj=SubjectManager.getSubjectObj(i)['res']
           if obj is not None:
             t.subjects.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.subjects.all() ]
       return {'res':res,'status':'info','msg':'all subjects having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get subjects:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMyClass_Subject(id,subjects):
    assert (isinstance(subjects,list)),"subjects must be a list type."
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in subjects:
           # get the object..
           obj=SubjectManager.getSubjectObj(i)['res']
           if obj is not None:
              t.subjects.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.subjects.all() ]
       return {'res':res,'status':'info','msg':'all subjects having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some subjects not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getMyClass_Student(id):
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.student_set.all() ]
       return {'res':res,'status':'info','msg':'all student for the MyClass returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMyClass_Student(id,student,flush=False):
    assert (isinstance(student,list)),"student must be a list type."
    try:
      res=MyClassManager.getMyClassObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.student.clear()
      for i in student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.student_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.student_set.all() ]
      return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMyClass_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
      res=MyClassManager.getMyClassObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in student:
          # get the object..
          obj=StudentManager.getStudentObj(i)['res']
          if obj is not None:
            t.student_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.student_set.all() ]
      return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getMyClass_Attendance(id):
    try:
       res=MyClassManager.getMyClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.attendance_set.all() ]
       return {'res':res,'status':'info','msg':'all attendance for the MyClass returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Attendance:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMyClass_Attendance(id,attendance,flush=False):
    assert (isinstance(attendance,list)),"attendance must be a list type."
    try:
      res=MyClassManager.getMyClassObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.attendance.clear()
      for i in attendance:
           # get the object..
           obj=AttendanceManager.getAttendanceObj(i)['res']
           if obj is not None:
             t.attendance_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.attendance_set.all() ]
      return {'res':res,'status':'info','msg':'all attendance having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get attendance:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMyClass_Attendance(id,attendance):
    assert (isinstance(attendance,list)),"attendance must be a list type."
    try:
      res=MyClassManager.getMyClassObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in attendance:
          # get the object..
          obj=AttendanceManager.getAttendanceObj(i)['res']
          if obj is not None:
            t.attendance_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.attendance_set.all() ]
      return {'res':res,'status':'info','msg':'all attendance having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some attendance not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchMyClass(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'MyClass Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=MyClass.objects.filter(Qstr)
      else:
        dd=MyClass.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'MyClass search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search MyClass!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewMyClass(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=MyClass.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View MyClass  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search MyClass!','sys_error':str(e)}


from .models import Exam
class ExamManager:
  @staticmethod
  def createExam(name=None,subject=None,date=None,classRoom=None,time=None,teacher=None,): #Crete an Obj
    try:
      if name and not set(name).issubset(set([u'half', u'annual', u'final'])) : return {'res':None,'status':'error','msg':"name must be either of [u'half', u'annual', u'final'] ",'sys_error':''};
      
      
      subject_res = SubjectManager.getSubjectObj(id=subject)
      if subject_res['res'] is None:
        subject_res['help'] ='make sure you have a input called subject in ur API or invalid subject id.'
        return subject_res
      subject = subject_res['res']
      
      t = Exam(name=name,subject=subject,date=date,classRoom=classRoom,time=time,)
      
      t.save()
      if teacher: ExamManager.addExam_Employee(t.id,teacher,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Exam got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getExam(id): # get Json
    try:
      t=Exam.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['subject_desc'] = SubjectManager.getSubject(id=res['subject'])['res'];
        
      return {'res':res,'status':'info','msg':'Exam returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Exam:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getExamObj(id): #get Obj
    try:
      t=Exam.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Exam Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Exam:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateExam(id,name=None,subject=None,date=None,classRoom=None,time=None,teacher=None, ): #Update Obj
    try:
      res=ExamManager.getExamObj(id)
      if res['res'] is None: return res
      t=res['res']
      if name and not set(name).issubset(set([u'half', u'annual', u'final'])) : return {'res':None,'status':'error','msg':"name must be either of [u'half', u'annual', u'final'] ",'sys_error':''};
      
      
      
      subject_res = SubjectManager.getSubjectObj(id=subject)
      if subject_res['res'] is None:
        subject_res['help'] ='make sure you have a input called subject in ur API or invalid subject id.'
        return subject_res
      subject = subject_res['res']  
      
      t.name = name if name is not None else t.name;t.subject = subject if subject is not None else t.subject;t.date = date if date is not None else t.date;t.classRoom = classRoom if classRoom is not None else t.classRoom;t.time = time if time is not None else t.time;             
      t.save()
      if teacher: ExamManager.addExam_Employee(t.id,teacher,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Exam Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteExam(id): #Delete Obj
    try:
      d=Exam.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Exam deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Exam:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchExam(name=None,subject=None,date=None,classRoom=None,time=None,teacher=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name']=name
      if subject is not None: Query['subject']=subject
      if classRoom is not None: Query['classRoom__contains']=classRoom
      if time is not None: Query['time__contains']=time
      if teacher is not None: Query['teacher']=teacher #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Exam.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Exam search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Exam:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getExam_Employee(id):
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.teacher.all() ]
       return {'res':res,'status':'info','msg':'all teacher for the Exam returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get teacher:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addExam_Employee(id,teacher,flush=False):
    assert (isinstance(teacher,list)),"teacher must be a list type."
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.teacher.clear()
       for i in teacher:
           # get the object..
           obj=EmployeeManager.getEmployeeObj(i)['res']
           if obj is not None:
             t.teacher.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.teacher.all() ]
       return {'res':res,'status':'info','msg':'all teacher having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get teacher:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeExam_Employee(id,teacher):
    assert (isinstance(teacher,list)),"teacher must be a list type."
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in teacher:
           # get the object..
           obj=EmployeeManager.getEmployeeObj(i)['res']
           if obj is not None:
              t.teacher.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.teacher.all() ]
       return {'res':res,'status':'info','msg':'all teacher having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some teacher not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getExam_Mark(id):
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.mark_set.all() ]
       return {'res':res,'status':'info','msg':'all mark for the Exam returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addExam_Mark(id,mark,flush=False):
    assert (isinstance(mark,list)),"mark must be a list type."
    try:
      res=ExamManager.getExamObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.mark.clear()
      for i in mark:
           # get the object..
           obj=MarkManager.getMarkObj(i)['res']
           if obj is not None:
             t.mark_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.mark_set.all() ]
      return {'res':res,'status':'info','msg':'all mark having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeExam_Mark(id,mark):
    assert (isinstance(mark,list)),"mark must be a list type."
    try:
      res=ExamManager.getExamObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in mark:
          # get the object..
          obj=MarkManager.getMarkObj(i)['res']
          if obj is not None:
            t.mark_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.mark_set.all() ]
      return {'res':res,'status':'info','msg':'all mark having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some mark not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getExam_Result(id):
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.result_set.all() ]
       return {'res':res,'status':'info','msg':'all result for the Exam returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Result:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addExam_Result(id,result,flush=False):
    assert (isinstance(result,list)),"result must be a list type."
    try:
      res=ExamManager.getExamObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.result.clear()
      for i in result:
           # get the object..
           obj=ResultManager.getResultObj(i)['res']
           if obj is not None:
             t.result_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.result_set.all() ]
      return {'res':res,'status':'info','msg':'all result having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get result:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeExam_Result(id,result):
    assert (isinstance(result,list)),"result must be a list type."
    try:
      res=ExamManager.getExamObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in result:
          # get the object..
          obj=ResultManager.getResultObj(i)['res']
          if obj is not None:
            t.result_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.result_set.all() ]
      return {'res':res,'status':'info','msg':'all result having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some result not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getExam_Subject(id):
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.subject)]
       return {'res':res,'status':'info','msg':'all subject for the Exam returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addExam_Subject(id,subject):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in subject:
           # get the object..
           obj=SubjectManager.getSubjectObj(i)['res']
           if obj is not None:
             t.subject = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.subject )]
       return {'res':res,'status':'info','msg':'all subject having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeExam_Subject(id,subject):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
       res=ExamManager.getExamObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.subject=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all subject having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some subject not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchExam(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Exam Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Exam.objects.filter(Qstr)
      else:
        dd=Exam.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Exam search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Exam!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewExam(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Exam.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Exam  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Exam!','sys_error':str(e)}


from .models import Student
class StudentManager:
  @staticmethod
  def createStudent(uid=None,name=None,email=None,phone=None,address=None,dob=None,doj=None,gender=None,parent=None,myclass=None,roll=None,section=None,): #Crete an Obj
    try:
      
      
      parent_res = ParentManager.getParentObj(id=parent)
      if parent_res['res'] is None:
        parent_res['help'] ='make sure you have a input called parent in ur API or invalid parent id.'
        return parent_res
      parent = parent_res['res']
      
      t = Student(uid=uid,name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,parent=parent,roll=roll,section=section,)
      
      t.save()
      if myclass: StudentManager.addStudent_MyClass(t.id,myclass,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Student got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getStudent(id): # get Json
    try:
      t=Student.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['parent_desc'] = ParentManager.getParent(id=res['parent'])['res'];
        
      return {'res':res,'status':'info','msg':'Student returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Student:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getStudentObj(id): #get Obj
    try:
      t=Student.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Student Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Student:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateStudent(id,uid=None,name=None,email=None,phone=None,address=None,dob=None,doj=None,gender=None,parent=None,myclass=None,roll=None,section=None, ): #Update Obj
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
      
      parent_res = ParentManager.getParentObj(id=parent)
      if parent_res['res'] is None:
        parent_res['help'] ='make sure you have a input called parent in ur API or invalid parent id.'
        return parent_res
      parent = parent_res['res']  
      
      t.uid = uid if uid is not None else t.uid;t.name = name if name is not None else t.name;t.email = email if email is not None else t.email;t.phone = phone if phone is not None else t.phone;t.address = address if address is not None else t.address;t.dob = dob if dob is not None else t.dob;t.doj = doj if doj is not None else t.doj;t.gender = gender if gender is not None else t.gender;t.parent = parent if parent is not None else t.parent;t.roll = roll if roll is not None else t.roll;t.section = section if section is not None else t.section;             
      t.save()
      if myclass: StudentManager.addStudent_MyClass(t.id,myclass,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Student Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteStudent(id): #Delete Obj
    try:
      d=Student.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Student deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Student:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchStudent(uid=None,name=None,email=None,phone=None,address=None,dob=None,doj=None,gender=None,parent=None,myclass=None,roll=None,section=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if email is not None: Query['email__contains']=email
      if phone is not None: Query['phone__contains']=phone
      if address is not None: Query['address__contains']=address
      if dob is not None: Query['dob__contains']=dob
      if doj is not None: Query['doj']=doj
      if gender is not None: Query['gender__contains']=gender
      if parent is not None: Query['parent']=parent
      if roll is not None: Query['roll__contains']=roll
      if section is not None: Query['section']=section #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'myclass', 'id']
      dd=Student.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Student search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Student:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getStudent_MyClass(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.myclass.all() ]
       return {'res':res,'status':'info','msg':'all myclass for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get myclass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_MyClass(id,myclass,flush=False):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.myclass.clear()
       for i in myclass:
           # get the object..
           obj=MyClassManager.getMyClassObj(i)['res']
           if obj is not None:
             t.myclass.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.myclass.all() ]
       return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get myclass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_MyClass(id,myclass):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in myclass:
           # get the object..
           obj=MyClassManager.getMyClassObj(i)['res']
           if obj is not None:
              t.myclass.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.myclass.all() ]
       return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some myclass not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getStudent_Mark(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.mark_set.all() ]
       return {'res':res,'status':'info','msg':'all mark for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_Mark(id,mark,flush=False):
    assert (isinstance(mark,list)),"mark must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.mark.clear()
      for i in mark:
           # get the object..
           obj=MarkManager.getMarkObj(i)['res']
           if obj is not None:
             t.mark_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.mark_set.all() ]
      return {'res':res,'status':'info','msg':'all mark having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_Mark(id,mark):
    assert (isinstance(mark,list)),"mark must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in mark:
          # get the object..
          obj=MarkManager.getMarkObj(i)['res']
          if obj is not None:
            t.mark_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.mark_set.all() ]
      return {'res':res,'status':'info','msg':'all mark having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some mark not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getStudent_Result(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.result_set.all() ]
       return {'res':res,'status':'info','msg':'all result for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Result:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_Result(id,result,flush=False):
    assert (isinstance(result,list)),"result must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.result.clear()
      for i in result:
           # get the object..
           obj=ResultManager.getResultObj(i)['res']
           if obj is not None:
             t.result_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.result_set.all() ]
      return {'res':res,'status':'info','msg':'all result having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get result:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_Result(id,result):
    assert (isinstance(result,list)),"result must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in result:
          # get the object..
          obj=ResultManager.getResultObj(i)['res']
          if obj is not None:
            t.result_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.result_set.all() ]
      return {'res':res,'status':'info','msg':'all result having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some result not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getStudent_Attendance(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.attendance_set.all() ]
       return {'res':res,'status':'info','msg':'all attendance for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Attendance:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_Attendance(id,attendance,flush=False):
    assert (isinstance(attendance,list)),"attendance must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.attendance.clear()
      for i in attendance:
           # get the object..
           obj=AttendanceManager.getAttendanceObj(i)['res']
           if obj is not None:
             t.attendance_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.attendance_set.all() ]
      return {'res':res,'status':'info','msg':'all attendance having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get attendance:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_Attendance(id,attendance):
    assert (isinstance(attendance,list)),"attendance must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in attendance:
          # get the object..
          obj=AttendanceManager.getAttendanceObj(i)['res']
          if obj is not None:
            t.attendance_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.attendance_set.all() ]
      return {'res':res,'status':'info','msg':'all attendance having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some attendance not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getStudent_Fees(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.fees_set.all() ]
       return {'res':res,'status':'info','msg':'all fees for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Fees:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_Fees(id,fees,flush=False):
    assert (isinstance(fees,list)),"fees must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.fees.clear()
      for i in fees:
           # get the object..
           obj=FeesManager.getFeesObj(i)['res']
           if obj is not None:
             t.fees_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.fees_set.all() ]
      return {'res':res,'status':'info','msg':'all fees having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get fees:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_Fees(id,fees):
    assert (isinstance(fees,list)),"fees must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in fees:
          # get the object..
          obj=FeesManager.getFeesObj(i)['res']
          if obj is not None:
            t.fees_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.fees_set.all() ]
      return {'res':res,'status':'info','msg':'all fees having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some fees not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getStudent_Sport(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.sport_set.all() ]
       return {'res':res,'status':'info','msg':'all sport for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Sport:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_Sport(id,sport,flush=False):
    assert (isinstance(sport,list)),"sport must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.sport.clear()
      for i in sport:
           # get the object..
           obj=SportManager.getSportObj(i)['res']
           if obj is not None:
             t.sport_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.sport_set.all() ]
      return {'res':res,'status':'info','msg':'all sport having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get sport:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_Sport(id,sport):
    assert (isinstance(sport,list)),"sport must be a list type."
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in sport:
          # get the object..
          obj=SportManager.getSportObj(i)['res']
          if obj is not None:
            t.sport_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.sport_set.all() ]
      return {'res':res,'status':'info','msg':'all sport having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some sport not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getStudent_Parent(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.parent)]
       return {'res':res,'status':'info','msg':'all parent for the Student returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get parent:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addStudent_Parent(id,parent):
    assert (isinstance(parent,list)),"parent must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in parent:
           # get the object..
           obj=ParentManager.getParentObj(i)['res']
           if obj is not None:
             t.parent = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.parent )]
       return {'res':res,'status':'info','msg':'all parent having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get parent:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeStudent_Parent(id,parent):
    assert (isinstance(parent,list)),"parent must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.parent=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all parent having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some parent not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchStudent(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Student Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Student.objects.filter(Qstr)
      else:
        dd=Student.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'myclass', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Student search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Student!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewStudent(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'myclass', 'id']
      dd=Student.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Student  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Student!','sys_error':str(e)}


from .models import Mark
class MarkManager:
  @staticmethod
  def createMark(student=None,subject=None,exam=None,written=0,viva=0,practical=0,total=0,comment=None,): #Crete an Obj
    try:
      
      
      student_res = StudentManager.getStudentObj(id=student)
      if student_res['res'] is None:
        student_res['help'] ='make sure you have a input called student in ur API or invalid student id.'
        return student_res
      student = student_res['res']
      subject_res = SubjectManager.getSubjectObj(id=subject)
      if subject_res['res'] is None:
        subject_res['help'] ='make sure you have a input called subject in ur API or invalid subject id.'
        return subject_res
      subject = subject_res['res']
      exam_res = ExamManager.getExamObj(id=exam)
      if exam_res['res'] is None:
        exam_res['help'] ='make sure you have a input called exam in ur API or invalid exam id.'
        return exam_res
      exam = exam_res['res']
      
      t = Mark(student=student,subject=subject,exam=exam,written=written,viva=viva,practical=practical,total=total,comment=comment,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Mark got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getMark(id): # get Json
    try:
      t=Mark.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['student_desc'] = StudentManager.getStudent(id=res['student'])['res'];res['subject_desc'] = SubjectManager.getSubject(id=res['subject'])['res'];res['exam_desc'] = ExamManager.getExam(id=res['exam'])['res'];
        
      return {'res':res,'status':'info','msg':'Mark returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Mark:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getMarkObj(id): #get Obj
    try:
      t=Mark.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Mark Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Mark:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateMark(id,student=None,subject=None,exam=None,written=0,viva=0,practical=0,total=0,comment=None, ): #Update Obj
    try:
      res=MarkManager.getMarkObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
      
      student_res = StudentManager.getStudentObj(id=student)
      if student_res['res'] is None:
        student_res['help'] ='make sure you have a input called student in ur API or invalid student id.'
        return student_res
      student = student_res['res']
      subject_res = SubjectManager.getSubjectObj(id=subject)
      if subject_res['res'] is None:
        subject_res['help'] ='make sure you have a input called subject in ur API or invalid subject id.'
        return subject_res
      subject = subject_res['res']
      exam_res = ExamManager.getExamObj(id=exam)
      if exam_res['res'] is None:
        exam_res['help'] ='make sure you have a input called exam in ur API or invalid exam id.'
        return exam_res
      exam = exam_res['res']  
      
      t.student = student if student is not None else t.student;t.subject = subject if subject is not None else t.subject;t.exam = exam if exam is not None else t.exam;t.written = written if written is not None else t.written;t.viva = viva if viva is not None else t.viva;t.practical = practical if practical is not None else t.practical;t.total = total if total is not None else t.total;t.comment = comment if comment is not None else t.comment;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Mark Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Mark:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteMark(id): #Delete Obj
    try:
      d=Mark.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Mark deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Mark:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchMark(student=None,subject=None,exam=None,written=0,viva=0,practical=0,total=0,comment=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if student is not None: Query['student']=student
      if subject is not None: Query['subject']=subject
      if exam is not None: Query['exam']=exam
      if written is not None: Query['written']=written
      if viva is not None: Query['viva']=viva
      if practical is not None: Query['practical']=practical
      if total is not None: Query['total']=total
      if comment is not None: Query['comment__contains']=comment #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'student', u'subject', 'id']
      dd=Mark.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Mark search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Mark:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getMark_Student(id):
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.student)]
       return {'res':res,'status':'info','msg':'all student for the Mark returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMark_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.student = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.student )]
       return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMark_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.student=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getMark_Subject(id):
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.subject)]
       return {'res':res,'status':'info','msg':'all subject for the Mark returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMark_Subject(id,subject):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in subject:
           # get the object..
           obj=SubjectManager.getSubjectObj(i)['res']
           if obj is not None:
             t.subject = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.subject )]
       return {'res':res,'status':'info','msg':'all subject having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get subject:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMark_Subject(id,subject):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.subject=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all subject having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some subject not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getMark_Exam(id):
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.exam)]
       return {'res':res,'status':'info','msg':'all exam for the Mark returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addMark_Exam(id,exam):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in exam:
           # get the object..
           obj=ExamManager.getExamObj(i)['res']
           if obj is not None:
             t.exam = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.exam )]
       return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeMark_Exam(id,exam):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
       res=MarkManager.getMarkObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.exam=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some exam not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchMark(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Mark Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Mark.objects.filter(Qstr)
      else:
        dd=Mark.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'student', u'subject', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Mark search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Mark!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewMark(page=None,limit=None):
    try:
      res =None
      include =[u'student', u'subject', 'id']
      dd=Mark.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Mark  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Mark!','sys_error':str(e)}


from .models import Result
class ResultManager:
  @staticmethod
  def createResult(exam=None,Student=None,total=None,percentage=None,division=None,comment=None,): #Crete an Obj
    try:
      if division and not set(division).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"division must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      exam_res = ExamManager.getExamObj(id=exam)
      if exam_res['res'] is None:
        exam_res['help'] ='make sure you have a input called exam in ur API or invalid exam id.'
        return exam_res
      exam = exam_res['res']
      
      t = Result(exam=exam,total=total,percentage=percentage,division=division,comment=comment,)
      
      t.save()
      if Student: ResultManager.addResult_Student(t.id,Student,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Result got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Result:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getResult(id): # get Json
    try:
      t=Result.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['exam_desc'] = ExamManager.getExam(id=res['exam'])['res'];
        
      return {'res':res,'status':'info','msg':'Result returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Result:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getResultObj(id): #get Obj
    try:
      t=Result.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Result Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Result:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateResult(id,exam=None,Student=None,total=None,percentage=None,division=None,comment=None, ): #Update Obj
    try:
      res=ResultManager.getResultObj(id)
      if res['res'] is None: return res
      t=res['res']
      if division and not set(division).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"division must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      exam_res = ExamManager.getExamObj(id=exam)
      if exam_res['res'] is None:
        exam_res['help'] ='make sure you have a input called exam in ur API or invalid exam id.'
        return exam_res
      exam = exam_res['res']  
      
      t.exam = exam if exam is not None else t.exam;t.total = total if total is not None else t.total;t.percentage = percentage if percentage is not None else t.percentage;t.division = division if division is not None else t.division;t.comment = comment if comment is not None else t.comment;             
      t.save()
      if Student: ResultManager.addResult_Student(t.id,Student,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Result Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Result:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteResult(id): #Delete Obj
    try:
      d=Result.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Result deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Result:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchResult(exam=None,Student=None,total=None,percentage=None,division=None,comment=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if exam is not None: Query['exam']=exam
      if total is not None: Query['total']=total
      if percentage is not None: Query['percentage']=percentage
      if division is not None: Query['division']=division
      if comment is not None: Query['comment__contains']=comment #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'exam', 'id']
      dd=Result.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Result search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Result:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getResult_Student(id):
    try:
       res=ResultManager.getResultObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.Student.all() ]
       return {'res':res,'status':'info','msg':'all Student for the Result returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addResult_Student(id,Student,flush=False):
    assert (isinstance(Student,list)),"Student must be a list type."
    try:
       res=ResultManager.getResultObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.Student.clear()
       for i in Student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.Student.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.Student.all() ]
       return {'res':res,'status':'info','msg':'all Student having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeResult_Student(id,Student):
    assert (isinstance(Student,list)),"Student must be a list type."
    try:
       res=ResultManager.getResultObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in Student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
              t.Student.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.Student.all() ]
       return {'res':res,'status':'info','msg':'all Student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some Student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getResult_Exam(id):
    try:
       res=ResultManager.getResultObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.exam)]
       return {'res':res,'status':'info','msg':'all exam for the Result returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addResult_Exam(id,exam):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
       res=ResultManager.getResultObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in exam:
           # get the object..
           obj=ExamManager.getExamObj(i)['res']
           if obj is not None:
             t.exam = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.exam )]
       return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get exam:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeResult_Exam(id,exam):
    assert (isinstance(exam,list)),"exam must be a list type."
    try:
       res=ResultManager.getResultObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.exam=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all exam having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some exam not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchResult(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Result Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Result.objects.filter(Qstr)
      else:
        dd=Result.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'exam', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Result search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Result!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewResult(page=None,limit=None):
    try:
      res =None
      include =[u'exam', 'id']
      dd=Result.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Result  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Result!','sys_error':str(e)}


from .models import Attendance
class AttendanceManager:
  @staticmethod
  def createAttendance(student=None,myclass=None,total=None,percentage=None,comment=None,): #Crete an Obj
    try:
      
      
      student_res = StudentManager.getStudentObj(id=student)
      if student_res['res'] is None:
        student_res['help'] ='make sure you have a input called student in ur API or invalid student id.'
        return student_res
      student = student_res['res']
      myclass_res = MyClassManager.getMyClassObj(id=myclass)
      if myclass_res['res'] is None:
        myclass_res['help'] ='make sure you have a input called myclass in ur API or invalid myclass id.'
        return myclass_res
      myclass = myclass_res['res']
      
      t = Attendance(student=student,myclass=myclass,total=total,percentage=percentage,comment=comment,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Attendance got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Attendance:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getAttendance(id): # get Json
    try:
      t=Attendance.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['student_desc'] = StudentManager.getStudent(id=res['student'])['res'];res['myclass_desc'] = MyClassManager.getMyClass(id=res['myclass'])['res'];
        
      return {'res':res,'status':'info','msg':'Attendance returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Attendance:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getAttendanceObj(id): #get Obj
    try:
      t=Attendance.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Attendance Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Attendance:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateAttendance(id,student=None,myclass=None,total=None,percentage=None,comment=None, ): #Update Obj
    try:
      res=AttendanceManager.getAttendanceObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
      
      student_res = StudentManager.getStudentObj(id=student)
      if student_res['res'] is None:
        student_res['help'] ='make sure you have a input called student in ur API or invalid student id.'
        return student_res
      student = student_res['res']
      myclass_res = MyClassManager.getMyClassObj(id=myclass)
      if myclass_res['res'] is None:
        myclass_res['help'] ='make sure you have a input called myclass in ur API or invalid myclass id.'
        return myclass_res
      myclass = myclass_res['res']  
      
      t.student = student if student is not None else t.student;t.myclass = myclass if myclass is not None else t.myclass;t.total = total if total is not None else t.total;t.percentage = percentage if percentage is not None else t.percentage;t.comment = comment if comment is not None else t.comment;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Attendance Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Attendance:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteAttendance(id): #Delete Obj
    try:
      d=Attendance.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Attendance deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Attendance:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchAttendance(student=None,myclass=None,total=None,percentage=None,comment=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if student is not None: Query['student']=student
      if myclass is not None: Query['myclass']=myclass
      if total is not None: Query['total']=total
      if percentage is not None: Query['percentage']=percentage
      if comment is not None: Query['comment__contains']=comment #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'student', 'id']
      dd=Attendance.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Attendance search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Attendance:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getAttendance_Student(id):
    try:
       res=AttendanceManager.getAttendanceObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.student)]
       return {'res':res,'status':'info','msg':'all student for the Attendance returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addAttendance_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
       res=AttendanceManager.getAttendanceObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.student = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.student )]
       return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeAttendance_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
       res=AttendanceManager.getAttendanceObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.student=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  @staticmethod
  def getAttendance_MyClass(id):
    try:
       res=AttendanceManager.getAttendanceObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.myclass)]
       return {'res':res,'status':'info','msg':'all myclass for the Attendance returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get myclass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addAttendance_MyClass(id,myclass):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
       res=AttendanceManager.getAttendanceObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in myclass:
           # get the object..
           obj=MyClassManager.getMyClassObj(i)['res']
           if obj is not None:
             t.myclass = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.myclass )]
       return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get myclass:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeAttendance_MyClass(id,myclass):
    assert (isinstance(myclass,list)),"myclass must be a list type."
    try:
       res=AttendanceManager.getAttendanceObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.myclass=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all myclass having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some myclass not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchAttendance(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Attendance Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Attendance.objects.filter(Qstr)
      else:
        dd=Attendance.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'student', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Attendance search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Attendance!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewAttendance(page=None,limit=None):
    try:
      res =None
      include =[u'student', 'id']
      dd=Attendance.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Attendance  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Attendance!','sys_error':str(e)}


from .models import Fees
class FeesManager:
  @staticmethod
  def createFees(name=None,accid=None,total=None,breakup={'house_rent':0,'food':0,'traval':0},Student=None,): #Crete an Obj
    try:
      
      
      
      t = Fees(name=name,accid=accid,total=total,breakup=breakup,)
      
      t.save()
      if Student: FeesManager.addFees_Student(t.id,Student,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Fees got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fees:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getFees(id): # get Json
    try:
      t=Fees.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Fees returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Fees:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getFeesObj(id): #get Obj
    try:
      t=Fees.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Fees Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Fees:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateFees(id,name=None,accid=None,total=None,breakup={'house_rent':0,'food':0,'traval':0},Student=None, ): #Update Obj
    try:
      res=FeesManager.getFeesObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;t.total = total if total is not None else t.total;t.breakup = breakup if breakup is not None else t.breakup;             
      t.save()
      if Student: FeesManager.addFees_Student(t.id,Student,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Fees Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Fees:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteFees(id): #Delete Obj
    try:
      d=Fees.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Fees deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Fees:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchFees(name=None,accid=None,total=None,breakup={'house_rent':0,'food':0,'traval':0},Student=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid
      if total is not None: Query['total']=total
      if breakup is not None: Query['breakup']=breakup #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Fees.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Fees search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fees:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getFees_Student(id):
    try:
       res=FeesManager.getFeesObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.Student.all() ]
       return {'res':res,'status':'info','msg':'all Student for the Fees returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addFees_Student(id,Student,flush=False):
    assert (isinstance(Student,list)),"Student must be a list type."
    try:
       res=FeesManager.getFeesObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.Student.clear()
       for i in Student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.Student.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.Student.all() ]
       return {'res':res,'status':'info','msg':'all Student having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get Student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeFees_Student(id,Student):
    assert (isinstance(Student,list)),"Student must be a list type."
    try:
       res=FeesManager.getFeesObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in Student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
              t.Student.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.Student.all() ]
       return {'res':res,'status':'info','msg':'all Student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some Student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchFees(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Fees Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Fees.objects.filter(Qstr)
      else:
        dd=Fees.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Fees search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fees!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewFees(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Fees.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Fees  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fees!','sys_error':str(e)}


from .models import Sport
class SportManager:
  @staticmethod
  def createSport(name=None,position={'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34},student=None,categories=None,): #Crete an Obj
    try:
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      t = Sport(name=name,position=position,categories=categories,)
      
      t.save()
      if student: SportManager.addSport_Student(t.id,student,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Sport got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Sport:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getSport(id): # get Json
    try:
      t=Sport.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Sport returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Sport:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getSportObj(id): #get Obj
    try:
      t=Sport.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Sport Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Sport:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateSport(id,name=None,position={'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34},student=None,categories=None, ): #Update Obj
    try:
      res=SportManager.getSportObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.position = position if position is not None else t.position;t.categories = categories if categories is not None else t.categories;             
      t.save()
      if student: SportManager.addSport_Student(t.id,student,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Sport Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Sport:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteSport(id): #Delete Obj
    try:
      d=Sport.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Sport deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Sport:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchSport(name=None,position={'full_mark':100,'written':90,'viva':10,'practical':0,'pass_mark':34},student=None,categories=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if position is not None: Query['position']=position
      if student is not None: Query['student']=student
      if categories is not None: Query['categories']=categories #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'categories', 'id']
      dd=Sport.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Sport search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Sport:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getSport_Student(id):
    try:
       res=SportManager.getSportObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.student.all() ]
       return {'res':res,'status':'info','msg':'all student for the Sport returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addSport_Student(id,student,flush=False):
    assert (isinstance(student,list)),"student must be a list type."
    try:
       res=SportManager.getSportObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.student.clear()
       for i in student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
             t.student.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.student.all() ]
       return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get student:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeSport_Student(id,student):
    assert (isinstance(student,list)),"student must be a list type."
    try:
       res=SportManager.getSportObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in student:
           # get the object..
           obj=StudentManager.getStudentObj(i)['res']
           if obj is not None:
              t.student.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.student.all() ]
       return {'res':res,'status':'info','msg':'all student having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some student not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchSport(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Sport Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Sport.objects.filter(Qstr)
      else:
        dd=Sport.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'categories', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Sport search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Sport!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewSport(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'categories', 'id']
      dd=Sport.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Sport  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Sport!','sys_error':str(e)}


from .models import Account
class AccountManager:
  @staticmethod
  def createAccount(name=None,email=None,password_hash=None,salt_hash=None,active=None,clue=None,): #Crete an Obj
    try:
      
      
      
      t = Account(name=name,email=email,password_hash=password_hash,salt_hash=salt_hash,active=active,clue=clue,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Account got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Account:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getAccount(id): # get Json
    try:
      t=Account.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Account returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Account:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getAccountObj(id): #get Obj
    try:
      t=Account.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Account Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Account:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateAccount(id,name=None,email=None,password_hash=None,salt_hash=None,active=None,clue=None, ): #Update Obj
    try:
      res=AccountManager.getAccountObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
        
      
      t.name = name if name is not None else t.name;t.email = email if email is not None else t.email;t.password_hash = password_hash if password_hash is not None else t.password_hash;t.salt_hash = salt_hash if salt_hash is not None else t.salt_hash;t.active = active if active is not None else t.active;t.clue = clue if clue is not None else t.clue;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Account Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Account:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteAccount(id): #Delete Obj
    try:
      d=Account.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Account deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Account:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchAccount(name=None,email=None,password_hash=None,salt_hash=None,active=None,clue=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if email is not None: Query['email__contains']=email
      if password_hash is not None: Query['password_hash__contains']=password_hash
      if salt_hash is not None: Query['salt_hash__contains']=salt_hash
      if active is not None: Query['active__contains']=active
      if clue is not None: Query['clue__contains']=clue #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Account.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Account search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Account:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getAccount_Setting(id):
    try:
       res=AccountManager.getAccountObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.setting_set.all() ]
       return {'res':res,'status':'info','msg':'all setting for the Account returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Setting:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addAccount_Setting(id,setting,flush=False):
    assert (isinstance(setting,list)),"setting must be a list type."
    try:
      res=AccountManager.getAccountObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg =''
      if flush:
        t.setting.clear()
      for i in setting:
           # get the object..
           obj=SettingManager.getSettingObj(i)['res']
           if obj is not None:
             t.setting_set.add(obj)
             loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.setting_set.all() ]
      return {'res':res,'status':'info','msg':'all setting having id <'+loc_msg+'> got added!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get setting:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeAccount_Setting(id,setting):
    assert (isinstance(setting,list)),"setting must be a list type."
    try:
      res=AccountManager.getAccountObj(id)
      if res['res'] is None: return res
      t=res['res']
      loc_msg=''
      for i in setting:
          # get the object..
          obj=SettingManager.getSettingObj(i)['res']
          if obj is not None:
            t.setting_set.remove(obj)
            loc_msg+= str(obj.id)+','
      res= [  model_to_dict(i) for i in t.setting_set.all() ]
      return {'res':res,'status':'info','msg':'all setting having id <'+loc_msg+'> got removed!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Some setting not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchAccount(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Account Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Account.objects.filter(Qstr)
      else:
        dd=Account.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Account search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Account!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewAccount(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Account.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Account  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Account!','sys_error':str(e)}


from .models import Setting
class SettingManager:
  @staticmethod
  def createSetting(name=None,account=None,theme=None,): #Crete an Obj
    try:
      if theme and not set(theme).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"theme must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      t = Setting(name=name,theme=theme,)
      
      t.save()
      if account: SettingManager.addSetting_Account(t.id,account,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Setting got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Setting:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getSetting(id): # get Json
    try:
      t=Setting.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Setting returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Setting:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getSettingObj(id): #get Obj
    try:
      t=Setting.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Setting Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Setting:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateSetting(id,name=None,account=None,theme=None, ): #Update Obj
    try:
      res=SettingManager.getSettingObj(id)
      if res['res'] is None: return res
      t=res['res']
      if theme and not set(theme).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"theme must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.theme = theme if theme is not None else t.theme;             
      t.save()
      if account: SettingManager.addSetting_Account(t.id,account,flush=True);
      
      return {'res':model_to_dict(t),'status':'info','msg':'Setting Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Setting:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteSetting(id): #Delete Obj
    try:
      d=Setting.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Setting deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Setting:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchSetting(name=None,account=None,theme=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if account is not None: Query['account']=account
      if theme is not None: Query['theme']=theme #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'theme', 'id']
      dd=Setting.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Setting search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Setting:'+getCustomException(e),'sys_error':str(e)}

  

  @staticmethod
  def getSetting_Account(id):
    try:
       res=SettingManager.getSettingObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.account.all() ]
       return {'res':res,'status':'info','msg':'all account for the Setting returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get account:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def addSetting_Account(id,account,flush=False):
    assert (isinstance(account,list)),"account must be a list type."
    try:
       res=SettingManager.getSettingObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       if flush:
         t.account.clear()
       for i in account:
           # get the object..
           obj=AccountManager.getAccountObj(i)['res']
           if obj is not None:
             t.account.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.account.all() ]
       return {'res':res,'status':'info','msg':'all account having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get account:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def removeSetting_Account(id,account):
    assert (isinstance(account,list)),"account must be a list type."
    try:
       res=SettingManager.getSettingObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in account:
           # get the object..
           obj=AccountManager.getAccountObj(i)['res']
           if obj is not None:
              t.account.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.account.all() ]
       return {'res':res,'status':'info','msg':'all account having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some account not able to removed:'+getCustomException(e),'sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def advSearchSetting(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Setting Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Setting.objects.filter(Qstr)
      else:
        dd=Setting.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'theme', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Setting search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Setting!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewSetting(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'theme', 'id']
      dd=Setting.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Setting  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Setting!','sys_error':str(e)}


from .models import Fund
class FundManager:
  @staticmethod
  def createFund(name=None,tenant=None,purpose=None,type=None,amount=None,): #Crete an Obj
    try:
      if type and not set(type).issubset(set([u'Debit', u'Credit'])) : return {'res':None,'status':'error','msg':"type must be either of [u'Debit', u'Credit'] ",'sys_error':''};
      
      
      
      t = Fund(name=name,tenant=tenant,purpose=purpose,type=type,amount=amount,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Fund got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fund:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getFund(id): # get Json
    try:
      t=Fund.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Fund returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Fund:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getFundObj(id): #get Obj
    try:
      t=Fund.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Fund Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Fund:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateFund(id,name=None,tenant=None,purpose=None,type=None,amount=None, ): #Update Obj
    try:
      res=FundManager.getFundObj(id)
      if res['res'] is None: return res
      t=res['res']
      if type and not set(type).issubset(set([u'Debit', u'Credit'])) : return {'res':None,'status':'error','msg':"type must be either of [u'Debit', u'Credit'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.tenant = tenant if tenant is not None else t.tenant;t.purpose = purpose if purpose is not None else t.purpose;t.type = type if type is not None else t.type;t.amount = amount if amount is not None else t.amount;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Fund Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Fund:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteFund(id): #Delete Obj
    try:
      d=Fund.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Fund deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Fund:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchFund(name=None,tenant=None,purpose=None,type=None,amount=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if tenant is not None: Query['tenant__contains']=tenant
      if purpose is not None: Query['purpose__contains']=purpose
      if type is not None: Query['type']=type
      if amount is not None: Query['amount']=amount #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Fund.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Fund search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fund:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchFund(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Fund Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Fund.objects.filter(Qstr)
      else:
        dd=Fund.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Fund search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fund!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewFund(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Fund.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Fund  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fund!','sys_error':str(e)}


from .models import Book
class BookManager:
  @staticmethod
  def createBook(name=None,author=None,desc=None,count=None,price=None,categories=None,): #Crete an Obj
    try:
      if categories and not set(categories).issubset(set([u'Debit', u'Credit'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'Debit', u'Credit'] ",'sys_error':''};
      
      
      
      t = Book(name=name,author=author,desc=desc,count=count,price=price,categories=categories,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Book got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getBook(id): # get Json
    try:
      t=Book.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Book returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Book:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getBookObj(id): #get Obj
    try:
      t=Book.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Book Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Book:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateBook(id,name=None,author=None,desc=None,count=None,price=None,categories=None, ): #Update Obj
    try:
      res=BookManager.getBookObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categories and not set(categories).issubset(set([u'Debit', u'Credit'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'Debit', u'Credit'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.author = author if author is not None else t.author;t.desc = desc if desc is not None else t.desc;t.count = count if count is not None else t.count;t.price = price if price is not None else t.price;t.categories = categories if categories is not None else t.categories;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Book Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Book:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteBook(id): #Delete Obj
    try:
      d=Book.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Book deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Book:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchBook(name=None,author=None,desc=None,count=None,price=None,categories=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if author is not None: Query['author__contains']=author
      if desc is not None: Query['desc__contains']=desc
      if count is not None: Query['count']=count
      if price is not None: Query['price']=price
      if categories is not None: Query['categories']=categories #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Book.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchBook(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Book Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Book.objects.filter(Qstr)
      else:
        dd=Book.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Book search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewBook(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Book.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Book  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Book!','sys_error':str(e)}


from .models import Event
class EventManager:
  @staticmethod
  def createEvent(name=None,details=None,categories=None,date=None,): #Crete an Obj
    try:
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      t = Event(name=name,details=details,categories=categories,date=date,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Event got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Event:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getEvent(id): # get Json
    try:
      t=Event.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Event returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Event:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getEventObj(id): #get Obj
    try:
      t=Event.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Event Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Event:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateEvent(id,name=None,details=None,categories=None,date=None, ): #Update Obj
    try:
      res=EventManager.getEventObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.details = details if details is not None else t.details;t.categories = categories if categories is not None else t.categories;t.date = date if date is not None else t.date;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Event Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Event:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteEvent(id): #Delete Obj
    try:
      d=Event.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Event deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Event:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchEvent(name=None,details=None,categories=None,date=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if details is not None: Query['details__contains']=details
      if categories is not None: Query['categories']=categories
      if date is not None: Query['date']=date #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'categories', 'id']
      dd=Event.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Event search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Event:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchEvent(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Event Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Event.objects.filter(Qstr)
      else:
        dd=Event.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'categories', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Event search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Event!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewEvent(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'categories', 'id']
      dd=Event.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Event  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Event!','sys_error':str(e)}


from .models import Discipline
class DisciplineManager:
  @staticmethod
  def createDiscipline(name=None,details=None,categories=None,): #Crete an Obj
    try:
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      t = Discipline(name=name,details=details,categories=categories,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Discipline got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Discipline:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getDiscipline(id): # get Json
    try:
      t=Discipline.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Discipline returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Discipline:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getDisciplineObj(id): #get Obj
    try:
      t=Discipline.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Discipline Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Discipline:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateDiscipline(id,name=None,details=None,categories=None, ): #Update Obj
    try:
      res=DisciplineManager.getDisciplineObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.details = details if details is not None else t.details;t.categories = categories if categories is not None else t.categories;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Discipline Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Discipline:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteDiscipline(id): #Delete Obj
    try:
      d=Discipline.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Discipline deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Discipline:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchDiscipline(name=None,details=None,categories=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if details is not None: Query['details__contains']=details
      if categories is not None: Query['categories']=categories #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'categories', 'id']
      dd=Discipline.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Discipline search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Discipline:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchDiscipline(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Discipline Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Discipline.objects.filter(Qstr)
      else:
        dd=Discipline.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'name', u'categories', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Discipline search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Discipline!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewDiscipline(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'categories', 'id']
      dd=Discipline.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Discipline  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Discipline!','sys_error':str(e)}


from .models import Notice
class NoticeManager:
  @staticmethod
  def createNotice(title=None,details=None,categories=None,date=None,): #Crete an Obj
    try:
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      t = Notice(title=title,details=details,categories=categories,date=date,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Notice got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Notice:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getNotice(id): # get Json
    try:
      t=Notice.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Notice returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Notice:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getNoticeObj(id): #get Obj
    try:
      t=Notice.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Notice Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Notice:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateNotice(id,title=None,details=None,categories=None,date=None, ): #Update Obj
    try:
      res=NoticeManager.getNoticeObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
        
      
      t.title = title if title is not None else t.title;t.details = details if details is not None else t.details;t.categories = categories if categories is not None else t.categories;t.date = date if date is not None else t.date;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Notice Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Notice:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteNotice(id): #Delete Obj
    try:
      d=Notice.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Notice deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Notice:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchNotice(title=None,details=None,categories=None,date=None,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if title is not None: Query['title__contains']=title
      if details is not None: Query['details__contains']=details
      if categories is not None: Query['categories']=categories #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'title', u'categories', 'id']
      dd=Notice.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Notice search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Notice:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchNotice(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Notice Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Notice.objects.filter(Qstr)
      else:
        dd=Notice.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'title', u'categories', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Notice search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Notice!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewNotice(page=None,limit=None):
    try:
      res =None
      include =[u'title', u'categories', 'id']
      dd=Notice.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Notice  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Notice!','sys_error':str(e)}


from .models import Instrument
class InstrumentManager:
  @staticmethod
  def createInstrument(name=None,details=None,categories=None,purchage_date=None,count=0,): #Crete an Obj
    try:
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
      
      t = Instrument(name=name,details=details,categories=categories,purchage_date=purchage_date,count=count,)
      
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New Instrument got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Instrument:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def getInstrument(id): # get Json
    try:
      t=Instrument.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Instrument returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Instrument:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getInstrumentObj(id): #get Obj
    try:
      t=Instrument.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Instrument Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object Instrument:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updateInstrument(id,name=None,details=None,categories=None,purchage_date=None,count=0, ): #Update Obj
    try:
      res=InstrumentManager.getInstrumentObj(id)
      if res['res'] is None: return res
      t=res['res']
      if categories and not set(categories).issubset(set([u'First', u'Second', u'Third', u'PassWithCons', u'Failed'])) : return {'res':None,'status':'error','msg':"categories must be either of [u'First', u'Second', u'Third', u'PassWithCons', u'Failed'] ",'sys_error':''};
      
      
        
      
      t.name = name if name is not None else t.name;t.details = details if details is not None else t.details;t.categories = categories if categories is not None else t.categories;t.purchage_date = purchage_date if purchage_date is not None else t.purchage_date;t.count = count if count is not None else t.count;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'Instrument Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Instrument:'+getCustomException(e),'sys_error':str(e)}

  @staticmethod
  def deleteInstrument(id): #Delete Obj
    try:
      d=Instrument.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Instrument deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Instrument:'+getCustomException(e),'sys_error':str(e)}


  @staticmethod
  def searchInstrument(name=None,details=None,categories=None,purchage_date=None,count=0,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if details is not None: Query['details__contains']=details
      if categories is not None: Query['categories']=categories
      if count is not None: Query['count']=count #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'title', u'categories', 'id']
      dd=Instrument.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'Instrument search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Instrument:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchInstrument(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'Instrument Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=Instrument.objects.filter(Qstr)
      else:
        dd=Instrument.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'title', u'categories', 'id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'Instrument search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Instrument!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewInstrument(page=None,limit=None):
    try:
      res =None
      include =[u'title', u'categories', 'id']
      dd=Instrument.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View Instrument  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Instrument!','sys_error':str(e)}

