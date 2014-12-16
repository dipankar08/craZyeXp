import pdb
from common import D_LOG
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *

from .models import Student
class StudentManager:
  @staticmethod
  def createStudent(name,email,phone,address,dob,doj,gender,Parent,roll,section,): #Crete an Obj
    try:
      
      Parent_res = ParentManager.getParentObj(id=Parent)
      if Parent_res['res'] is None:
        Parent_res['help'] ='make sure you have a input called Parent in ur API or invalid Parent id.'
        return Parent_res
      Parent = Parent_res['res']
      
      t = Student(name=name,email=email,phone=phone,address=address,dob=dob,doj=doj,gender=gender,Parent=Parent,roll=roll,section=section,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Student got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Student','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Student','sys_error':str(e)}

  @staticmethod
  def getStudent(id): # get Json
    try:
      t=Student.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        res['Parent_desc'] = ParentManager.getParent(id=res['Parent'])['res'];
        
      return {'res':res,'status':'info','msg':'Student returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Student having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Student','sys_error':str(e)}

  @staticmethod
  def getStudentObj(id): #get Obj
    try:
      t=Student.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Student Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Student having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Student','sys_error':str(e)}

  @staticmethod
  def updateStudent(id,name,email,phone,address,dob,doj,gender,Parent,roll,section, ): #Update Obj
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      
      Parent_res = ParentManager.getParentObj(id=Parent)
      if Parent_res['res'] is None:
        Parent_res['help'] ='make sure you have a input called Parent in ur API or invalid Parent id.'
        return Parent_res
      Parent = Parent_res['res']  
      
      t.name = name if name is not None else t.name;t.email = email if email is not None else t.email;t.phone = phone if phone is not None else t.phone;t.address = address if address is not None else t.address;t.dob = dob if dob is not None else t.dob;t.doj = doj if doj is not None else t.doj;t.gender = gender if gender is not None else t.gender;t.Parent = Parent if Parent is not None else t.Parent;t.roll = roll if roll is not None else t.roll;t.section = section if section is not None else t.section;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Student Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Student','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Student','sys_error':str(e)}

  @staticmethod
  def deleteStudent(id): #Delete Obj
    try:
      d=Student.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Student deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Student!','sys_error':str(e)}


  @staticmethod
  def searchStudent(name,email,phone,address,dob,doj,gender,Parent,roll,section,page=None,limit=None,id=None): # Simple Serach 
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
      if Parent is not None: Query['Parent']=Parent
      if roll is not None: Query['roll__contains']=roll
      if section is not None: Query['section']=section #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', u'class', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Student!','sys_error':str(e)}

  

  @staticmethod
  def getStudent_Class(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.class.all() ]
       return {'res':res,'status':'info','msg':'all class for the Student returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get class ','sys_error':str(e)}

  @staticmethod
  def addStudent_Class(id,class):
    assert (isinstance(class,list)),"class must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in class:
           # get the object..
           obj=ClassManager.getClassObj(i)['res']
           if obj is not None:
             t.class.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.class.all() ]
       return {'res':res,'status':'info','msg':'all class having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get class ','sys_error':str(e)}

  @staticmethod
  def removeStudent_Class(id,class):
    assert (isinstance(class,list)),"class must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in class:
           # get the object..
           obj=ClassManager.getClassObj(i)['res']
           if obj is not None:
              t.class.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.class.all() ]
       return {'res':res,'status':'info','msg':'all class having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some class not able to removed! ','sys_error':str(e)}



  @staticmethod
  def getStudent_Parent(id):
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [ model_to_dict(t.Parent)]
       return {'res':res,'status':'info','msg':'all Parent for the Student returned.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Parent ','sys_error':str(e)}

  @staticmethod
  def addStudent_Parent(id,Parent):
    assert (isinstance(Parent,list)),"Parent must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in Parent:
           # get the object..
           obj=ParentManager.getParentObj(i)['res']
           if obj is not None:
             t.Parent = obj
             t.save()
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(t.Parent )]
       return {'res':res,'status':'info','msg':'all Parent having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get Parent ','sys_error':str(e)}

  @staticmethod
  def removeStudent_Parent(id,Parent):
    assert (isinstance(Parent,list)),"Parent must be a list type."
    try:
       res=StudentManager.getStudentObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       t.Parent=None # This is a single object..
       t.save()
       res= []
       return {'res':res,'status':'info','msg':'all Parent having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some Parent not able to removed! ','sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def minViewStudent(page=None,limit=None):
    try:
      res =None
      include =[u'name', u'class', 'id']
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
      
      return {'res':res,'status':'info','msg':'Student Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Student!','sys_error':str(e)}


from .models import Employee
class EmployeeManager:
  @staticmethod
  def createEmployee(name,accid,): #Crete an Obj
    try:
      
      
      t = Employee(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Employee got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Employee','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Employee','sys_error':str(e)}

  @staticmethod
  def getEmployee(id): # get Json
    try:
      t=Employee.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Employee returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Employee having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Employee','sys_error':str(e)}

  @staticmethod
  def getEmployeeObj(id): #get Obj
    try:
      t=Employee.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Employee Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Employee having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Employee','sys_error':str(e)}

  @staticmethod
  def updateEmployee(id,name,accid, ): #Update Obj
    try:
      res=EmployeeManager.getEmployeeObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Employee Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Employee','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Employee','sys_error':str(e)}

  @staticmethod
  def deleteEmployee(id): #Delete Obj
    try:
      d=Employee.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Employee deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Employee!','sys_error':str(e)}


  @staticmethod
  def searchEmployee(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Employee!','sys_error':str(e)}

  

  @staticmethod
  def getEmployee_Class(id):
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.class_set.all() ]
       return {'res':res,'status':'info','msg':'all class for the Employee returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get Class ','sys_error':str(e)}

  @staticmethod
  def addEmployee_Class(id,class):
    assert (isinstance(class,list)),"class must be a list type."
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
       for i in class:
           # get the object..
           obj=ClassManager.getClassObj(i)['res']
           if obj is not None:
             t.class_set.add(obj)
             loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.class_set.all() ]
       return {'res':res,'status':'info','msg':'all class having id <'+loc_msg+'> got added!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Not able to get class ','sys_error':str(e)}

  @staticmethod
  def removeEmployee_Class(id,class):
    assert (isinstance(class,list)),"class must be a list type."
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg=''
       for i in class:
           # get the object..
           obj=ClassManager.getClassObj(i)['res']
           if obj is not None:
              t.class_set.remove(obj)
              loc_msg+= str(obj.id)+','
       res= [  model_to_dict(i) for i in t.class_set.all() ]
       return {'res':res,'status':'info','msg':'all class having id <'+loc_msg+'> got removed!'}
    except Exception,e :
       D_LOG()
       return {'res':None,'status':'error','msg':'Some class not able to removed! ','sys_error':str(e)}



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
      return {'res':None,'status':'error','msg':'Not able to get Subject ','sys_error':str(e)}

  @staticmethod
  def addEmployee_Subject(id,subject):
    assert (isinstance(subject,list)),"subject must be a list type."
    try:
       res=EmployeeManager.getEmployeeObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
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
       return {'res':None,'status':'error','msg':'Not able to get subject ','sys_error':str(e)}

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
       return {'res':None,'status':'error','msg':'Some subject not able to removed! ','sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def minViewEmployee(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Employee Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Employee!','sys_error':str(e)}


from .models import Parent
class ParentManager:
  @staticmethod
  def createParent(name,email,phone,occupation,address,income,relationship,secondary_contact,): #Crete an Obj
    try:
      
      
      t = Parent(name=name,email=email,phone=phone,occupation=occupation,address=address,income=income,relationship=relationship,secondary_contact=secondary_contact,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Parent got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Parent','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Parent','sys_error':str(e)}

  @staticmethod
  def getParent(id): # get Json
    try:
      t=Parent.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Parent returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Parent having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Parent','sys_error':str(e)}

  @staticmethod
  def getParentObj(id): #get Obj
    try:
      t=Parent.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Parent Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Parent having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Parent','sys_error':str(e)}

  @staticmethod
  def updateParent(id,name,email,phone,occupation,address,income,relationship,secondary_contact, ): #Update Obj
    try:
      res=ParentManager.getParentObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.email = email if email is not None else t.email;t.phone = phone if phone is not None else t.phone;t.occupation = occupation if occupation is not None else t.occupation;t.address = address if address is not None else t.address;t.income = income if income is not None else t.income;t.relationship = relationship if relationship is not None else t.relationship;t.secondary_contact = secondary_contact if secondary_contact is not None else t.secondary_contact;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Parent Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Parent','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Parent','sys_error':str(e)}

  @staticmethod
  def deleteParent(id): #Delete Obj
    try:
      d=Parent.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Parent deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Parent!','sys_error':str(e)}


  @staticmethod
  def searchParent(name,email,phone,occupation,address,income,relationship,secondary_contact,page=None,limit=None,id=None): # Simple Serach 
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
      
      return {'res':res,'status':'info','msg':'Parent Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Parent!','sys_error':str(e)}


from .models import Class
class ClassManager:
  @staticmethod
  def createClass(name,room,class_teacher,subjects,): #Crete an Obj
    try:
      
      
      t = Class(name=name,room=room,class_teacher=class_teacher,subjects=subjects,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Class got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Class','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Class','sys_error':str(e)}

  @staticmethod
  def getClass(id): # get Json
    try:
      t=Class.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Class returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Class having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Class','sys_error':str(e)}

  @staticmethod
  def getClassObj(id): #get Obj
    try:
      t=Class.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Class Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Class having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Class','sys_error':str(e)}

  @staticmethod
  def updateClass(id,name,room,class_teacher,subjects, ): #Update Obj
    try:
      res=ClassManager.getClassObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.room = room if room is not None else t.room;t.class_teacher = class_teacher if class_teacher is not None else t.class_teacher;t.subjects = subjects if subjects is not None else t.subjects;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Class Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Class','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Class','sys_error':str(e)}

  @staticmethod
  def deleteClass(id): #Delete Obj
    try:
      d=Class.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Class deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Class!','sys_error':str(e)}


  @staticmethod
  def searchClass(name,room,class_teacher,subjects,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if room is not None: Query['room__contains']=room
      if class_teacher is not None: Query['class_teacher']=class_teacher
      if subjects is not None: Query['subjects']=subjects #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Class.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'Class search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Class!','sys_error':str(e)}

  

  @staticmethod
  def getClass_Employee(id):
    try:
       res=ClassManager.getClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.class_teacher.all() ]
       return {'res':res,'status':'info','msg':'all class_teacher for the Class returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get class_teacher ','sys_error':str(e)}

  @staticmethod
  def addClass_Employee(id,class_teacher):
    assert (isinstance(class_teacher,list)),"class_teacher must be a list type."
    try:
       res=ClassManager.getClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
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
       return {'res':None,'status':'error','msg':'Not able to get class_teacher ','sys_error':str(e)}

  @staticmethod
  def removeClass_Employee(id,class_teacher):
    assert (isinstance(class_teacher,list)),"class_teacher must be a list type."
    try:
       res=ClassManager.getClassObj(id)
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
       return {'res':None,'status':'error','msg':'Some class_teacher not able to removed! ','sys_error':str(e)}



  @staticmethod
  def getClass_Subject(id):
    try:
       res=ClassManager.getClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       res= [  model_to_dict(i) for i in t.subjects.all() ]
       return {'res':res,'status':'info','msg':'all subjects for the Class returned.'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to get subjects ','sys_error':str(e)}

  @staticmethod
  def addClass_Subject(id,subjects):
    assert (isinstance(subjects,list)),"subjects must be a list type."
    try:
       res=ClassManager.getClassObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
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
       return {'res':None,'status':'error','msg':'Not able to get subjects ','sys_error':str(e)}

  @staticmethod
  def removeClass_Subject(id,subjects):
    assert (isinstance(subjects,list)),"subjects must be a list type."
    try:
       res=ClassManager.getClassObj(id)
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
       return {'res':None,'status':'error','msg':'Some subjects not able to removed! ','sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def minViewClass(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Class.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Class Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Class!','sys_error':str(e)}


from .models import Subject
class SubjectManager:
  @staticmethod
  def createSubject(name,uid,syllabus,accid,teacher,categorise,group,): #Crete an Obj
    try:
      
      
      t = Subject(name=name,uid=uid,syllabus=syllabus,accid=accid,teacher=teacher,categorise=categorise,group=group,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Subject got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Subject','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Subject','sys_error':str(e)}

  @staticmethod
  def getSubject(id): # get Json
    try:
      t=Subject.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Subject returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Subject having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Subject','sys_error':str(e)}

  @staticmethod
  def getSubjectObj(id): #get Obj
    try:
      t=Subject.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Subject Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Subject having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Subject','sys_error':str(e)}

  @staticmethod
  def updateSubject(id,name,uid,syllabus,accid,teacher,categorise,group, ): #Update Obj
    try:
      res=SubjectManager.getSubjectObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.uid = uid if uid is not None else t.uid;t.syllabus = syllabus if syllabus is not None else t.syllabus;t.accid = accid if accid is not None else t.accid;t.teacher = teacher if teacher is not None else t.teacher;t.categorise = categorise if categorise is not None else t.categorise;t.group = group if group is not None else t.group;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Subject Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Subject','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Subject','sys_error':str(e)}

  @staticmethod
  def deleteSubject(id): #Delete Obj
    try:
      d=Subject.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Subject deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Subject!','sys_error':str(e)}


  @staticmethod
  def searchSubject(name,uid,syllabus,accid,teacher,categorise,group,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if uid is not None: Query['uid__contains']=uid
      if syllabus is not None: Query['syllabus__contains']=syllabus
      if accid is not None: Query['accid']=accid
      if teacher is not None: Query['teacher']=teacher
      if categorise is not None: Query['categorise']=categorise
      if group is not None: Query['group']=group #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Subject!','sys_error':str(e)}

  

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
      return {'res':None,'status':'error','msg':'Not able to get teacher ','sys_error':str(e)}

  @staticmethod
  def addSubject_Employee(id,teacher):
    assert (isinstance(teacher,list)),"teacher must be a list type."
    try:
       res=SubjectManager.getSubjectObj(id)
       if res['res'] is None: return res
       t=res['res']
       loc_msg =''
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
       return {'res':None,'status':'error','msg':'Not able to get teacher ','sys_error':str(e)}

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
       return {'res':None,'status':'error','msg':'Some teacher not able to removed! ','sys_error':str(e)}



  #Advance search is Implemented here..
  @staticmethod
  def minViewSubject(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Subject Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Subject!','sys_error':str(e)}


from .models import Mark
class MarkManager:
  @staticmethod
  def createMark(name,accid,): #Crete an Obj
    try:
      
      
      t = Mark(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Mark got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Mark','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Mark','sys_error':str(e)}

  @staticmethod
  def getMark(id): # get Json
    try:
      t=Mark.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Mark returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Mark having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Mark','sys_error':str(e)}

  @staticmethod
  def getMarkObj(id): #get Obj
    try:
      t=Mark.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Mark Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Mark having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Mark','sys_error':str(e)}

  @staticmethod
  def updateMark(id,name,accid, ): #Update Obj
    try:
      res=MarkManager.getMarkObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Mark Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Mark','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Mark','sys_error':str(e)}

  @staticmethod
  def deleteMark(id): #Delete Obj
    try:
      d=Mark.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Mark deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Mark!','sys_error':str(e)}


  @staticmethod
  def searchMark(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Mark!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewMark(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Mark Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Mark!','sys_error':str(e)}


from .models import Result
class ResultManager:
  @staticmethod
  def createResult(name,accid,): #Crete an Obj
    try:
      
      
      t = Result(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Result got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Result','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Result','sys_error':str(e)}

  @staticmethod
  def getResult(id): # get Json
    try:
      t=Result.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Result returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Result having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Result','sys_error':str(e)}

  @staticmethod
  def getResultObj(id): #get Obj
    try:
      t=Result.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Result Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Result having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Result','sys_error':str(e)}

  @staticmethod
  def updateResult(id,name,accid, ): #Update Obj
    try:
      res=ResultManager.getResultObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Result Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Result','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Result','sys_error':str(e)}

  @staticmethod
  def deleteResult(id): #Delete Obj
    try:
      d=Result.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Result deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Result!','sys_error':str(e)}


  @staticmethod
  def searchResult(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Result!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewResult(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Result Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Result!','sys_error':str(e)}


from .models import Exam
class ExamManager:
  @staticmethod
  def createExam(name,accid,): #Crete an Obj
    try:
      
      
      t = Exam(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Exam got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Exam','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Exam','sys_error':str(e)}

  @staticmethod
  def getExam(id): # get Json
    try:
      t=Exam.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Exam returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Exam having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Exam','sys_error':str(e)}

  @staticmethod
  def getExamObj(id): #get Obj
    try:
      t=Exam.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Exam Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Exam having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Exam','sys_error':str(e)}

  @staticmethod
  def updateExam(id,name,accid, ): #Update Obj
    try:
      res=ExamManager.getExamObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Exam Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Exam','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Exam','sys_error':str(e)}

  @staticmethod
  def deleteExam(id): #Delete Obj
    try:
      d=Exam.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Exam deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Exam!','sys_error':str(e)}


  @staticmethod
  def searchExam(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
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
      
      return {'res':res,'status':'info','msg':'Exam Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Exam!','sys_error':str(e)}


from .models import Attendance
class AttendanceManager:
  @staticmethod
  def createAttendance(name,accid,): #Crete an Obj
    try:
      
      
      t = Attendance(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Attendance got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Attendance','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Attendance','sys_error':str(e)}

  @staticmethod
  def getAttendance(id): # get Json
    try:
      t=Attendance.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Attendance returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Attendance having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Attendance','sys_error':str(e)}

  @staticmethod
  def getAttendanceObj(id): #get Obj
    try:
      t=Attendance.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Attendance Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Attendance having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Attendance','sys_error':str(e)}

  @staticmethod
  def updateAttendance(id,name,accid, ): #Update Obj
    try:
      res=AttendanceManager.getAttendanceObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Attendance Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Attendance','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Attendance','sys_error':str(e)}

  @staticmethod
  def deleteAttendance(id): #Delete Obj
    try:
      d=Attendance.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Attendance deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Attendance!','sys_error':str(e)}


  @staticmethod
  def searchAttendance(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Attendance!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewAttendance(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Attendance Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Attendance!','sys_error':str(e)}


from .models import Fees
class FeesManager:
  @staticmethod
  def createFees(name,accid,): #Crete an Obj
    try:
      
      
      t = Fees(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Fees got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fees','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fees','sys_error':str(e)}

  @staticmethod
  def getFees(id): # get Json
    try:
      t=Fees.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Fees returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Fees having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Fees','sys_error':str(e)}

  @staticmethod
  def getFeesObj(id): #get Obj
    try:
      t=Fees.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Fees Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Fees having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Fees','sys_error':str(e)}

  @staticmethod
  def updateFees(id,name,accid, ): #Update Obj
    try:
      res=FeesManager.getFeesObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Fees Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fees','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Fees','sys_error':str(e)}

  @staticmethod
  def deleteFees(id): #Delete Obj
    try:
      d=Fees.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Fees deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Fees!','sys_error':str(e)}


  @staticmethod
  def searchFees(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
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
      
      return {'res':res,'status':'info','msg':'Fees Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fees!','sys_error':str(e)}


from .models import Fund
class FundManager:
  @staticmethod
  def createFund(name,accid,): #Crete an Obj
    try:
      
      
      t = Fund(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Fund got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fund','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fund','sys_error':str(e)}

  @staticmethod
  def getFund(id): # get Json
    try:
      t=Fund.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Fund returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Fund having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Fund','sys_error':str(e)}

  @staticmethod
  def getFundObj(id): #get Obj
    try:
      t=Fund.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Fund Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Fund having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Fund','sys_error':str(e)}

  @staticmethod
  def updateFund(id,name,accid, ): #Update Obj
    try:
      res=FundManager.getFundObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Fund Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Fund','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Fund','sys_error':str(e)}

  @staticmethod
  def deleteFund(id): #Delete Obj
    try:
      d=Fund.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Fund deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Fund!','sys_error':str(e)}


  @staticmethod
  def searchFund(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
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
      
      return {'res':res,'status':'info','msg':'Fund Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Fund!','sys_error':str(e)}


from .models import LibBook
class LibBookManager:
  @staticmethod
  def createLibBook(name,accid,): #Crete an Obj
    try:
      
      
      t = LibBook(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New LibBook got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create LibBook','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create LibBook','sys_error':str(e)}

  @staticmethod
  def getLibBook(id): # get Json
    try:
      t=LibBook.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'LibBook returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The LibBook having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive LibBook','sys_error':str(e)}

  @staticmethod
  def getLibBookObj(id): #get Obj
    try:
      t=LibBook.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'LibBook Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The LibBook having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object LibBook','sys_error':str(e)}

  @staticmethod
  def updateLibBook(id,name,accid, ): #Update Obj
    try:
      res=LibBookManager.getLibBookObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'LibBook Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create LibBook','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update LibBook','sys_error':str(e)}

  @staticmethod
  def deleteLibBook(id): #Delete Obj
    try:
      d=LibBook.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one LibBook deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete LibBook!','sys_error':str(e)}


  @staticmethod
  def searchLibBook(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=LibBook.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'LibBook search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search LibBook!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewLibBook(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=LibBook.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'LibBook Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search LibBook!','sys_error':str(e)}


from .models import Leaves
class LeavesManager:
  @staticmethod
  def createLeaves(name,accid,): #Crete an Obj
    try:
      
      
      t = Leaves(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Leaves got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Leaves','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Leaves','sys_error':str(e)}

  @staticmethod
  def getLeaves(id): # get Json
    try:
      t=Leaves.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Leaves returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Leaves having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Leaves','sys_error':str(e)}

  @staticmethod
  def getLeavesObj(id): #get Obj
    try:
      t=Leaves.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Leaves Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Leaves having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Leaves','sys_error':str(e)}

  @staticmethod
  def updateLeaves(id,name,accid, ): #Update Obj
    try:
      res=LeavesManager.getLeavesObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Leaves Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Leaves','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Leaves','sys_error':str(e)}

  @staticmethod
  def deleteLeaves(id): #Delete Obj
    try:
      d=Leaves.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Leaves deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Leaves!','sys_error':str(e)}


  @staticmethod
  def searchLeaves(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=Leaves.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'Leaves search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Leaves!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewLeaves(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=Leaves.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'Leaves Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Leaves!','sys_error':str(e)}


from .models import PayRoll
class PayRollManager:
  @staticmethod
  def createPayRoll(name,accid,): #Crete an Obj
    try:
      
      
      t = PayRoll(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New PayRoll got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create PayRoll','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create PayRoll','sys_error':str(e)}

  @staticmethod
  def getPayRoll(id): # get Json
    try:
      t=PayRoll.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'PayRoll returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The PayRoll having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive PayRoll','sys_error':str(e)}

  @staticmethod
  def getPayRollObj(id): #get Obj
    try:
      t=PayRoll.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'PayRoll Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The PayRoll having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object PayRoll','sys_error':str(e)}

  @staticmethod
  def updatePayRoll(id,name,accid, ): #Update Obj
    try:
      res=PayRollManager.getPayRollObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'PayRoll Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create PayRoll','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update PayRoll','sys_error':str(e)}

  @staticmethod
  def deletePayRoll(id): #Delete Obj
    try:
      d=PayRoll.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one PayRoll deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete PayRoll!','sys_error':str(e)}


  @staticmethod
  def searchPayRoll(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
      dd=PayRoll.objects.filter(**Query).values(*include)
      
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
    
      return {'res':res,'status':'info','msg':'PayRoll search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search PayRoll!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewPayRoll(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
      dd=PayRoll.objects.values(*include)
      
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
      
      return {'res':res,'status':'info','msg':'PayRoll Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search PayRoll!','sys_error':str(e)}


from .models import Sport
class SportManager:
  @staticmethod
  def createSport(name,): #Crete an Obj
    try:
      
      
      t = Sport(name=name,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Sport got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Sport','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Sport','sys_error':str(e)}

  @staticmethod
  def getSport(id): # get Json
    try:
      t=Sport.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Sport returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Sport having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Sport','sys_error':str(e)}

  @staticmethod
  def getSportObj(id): #get Obj
    try:
      t=Sport.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Sport Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Sport having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Sport','sys_error':str(e)}

  @staticmethod
  def updateSport(id,name, ): #Update Obj
    try:
      res=SportManager.getSportObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Sport Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Sport','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Sport','sys_error':str(e)}

  @staticmethod
  def deleteSport(id): #Delete Obj
    try:
      d=Sport.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Sport deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Sport!','sys_error':str(e)}


  @staticmethod
  def searchSport(name,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Sport!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewSport(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Sport Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Sport!','sys_error':str(e)}


from .models import Event
class EventManager:
  @staticmethod
  def createEvent(name,accid,): #Crete an Obj
    try:
      
      
      t = Event(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Event got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Event','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Event','sys_error':str(e)}

  @staticmethod
  def getEvent(id): # get Json
    try:
      t=Event.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Event returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Event having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Event','sys_error':str(e)}

  @staticmethod
  def getEventObj(id): #get Obj
    try:
      t=Event.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Event Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Event having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Event','sys_error':str(e)}

  @staticmethod
  def updateEvent(id,name,accid, ): #Update Obj
    try:
      res=EventManager.getEventObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Event Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Event','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Event','sys_error':str(e)}

  @staticmethod
  def deleteEvent(id): #Delete Obj
    try:
      d=Event.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Event deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Event!','sys_error':str(e)}


  @staticmethod
  def searchEvent(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Event!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewEvent(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Event Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Event!','sys_error':str(e)}


from .models import Discipline
class DisciplineManager:
  @staticmethod
  def createDiscipline(name,accid,): #Crete an Obj
    try:
      
      
      t = Discipline(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Discipline got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Discipline','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Discipline','sys_error':str(e)}

  @staticmethod
  def getDiscipline(id): # get Json
    try:
      t=Discipline.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Discipline returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Discipline having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Discipline','sys_error':str(e)}

  @staticmethod
  def getDisciplineObj(id): #get Obj
    try:
      t=Discipline.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Discipline Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Discipline having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Discipline','sys_error':str(e)}

  @staticmethod
  def updateDiscipline(id,name,accid, ): #Update Obj
    try:
      res=DisciplineManager.getDisciplineObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Discipline Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Discipline','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Discipline','sys_error':str(e)}

  @staticmethod
  def deleteDiscipline(id): #Delete Obj
    try:
      d=Discipline.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Discipline deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Discipline!','sys_error':str(e)}


  @staticmethod
  def searchDiscipline(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Discipline!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewDiscipline(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Discipline Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Discipline!','sys_error':str(e)}


from .models import Notice
class NoticeManager:
  @staticmethod
  def createNotice(name,accid,): #Crete an Obj
    try:
      
      
      t = Notice(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Notice got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Notice','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Notice','sys_error':str(e)}

  @staticmethod
  def getNotice(id): # get Json
    try:
      t=Notice.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Notice returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Notice having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Notice','sys_error':str(e)}

  @staticmethod
  def getNoticeObj(id): #get Obj
    try:
      t=Notice.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Notice Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Notice having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Notice','sys_error':str(e)}

  @staticmethod
  def updateNotice(id,name,accid, ): #Update Obj
    try:
      res=NoticeManager.getNoticeObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Notice Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Notice','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Notice','sys_error':str(e)}

  @staticmethod
  def deleteNotice(id): #Delete Obj
    try:
      d=Notice.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Notice deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Notice!','sys_error':str(e)}


  @staticmethod
  def searchNotice(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Notice!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewNotice(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Notice Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Notice!','sys_error':str(e)}


from .models import Account
class AccountManager:
  @staticmethod
  def createAccount(name,accid,): #Crete an Obj
    try:
      
      
      t = Account(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Account got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Account','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Account','sys_error':str(e)}

  @staticmethod
  def getAccount(id): # get Json
    try:
      t=Account.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Account returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Account having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Account','sys_error':str(e)}

  @staticmethod
  def getAccountObj(id): #get Obj
    try:
      t=Account.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Account Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Account having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Account','sys_error':str(e)}

  @staticmethod
  def updateAccount(id,name,accid, ): #Update Obj
    try:
      res=AccountManager.getAccountObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Account Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Account','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Account','sys_error':str(e)}

  @staticmethod
  def deleteAccount(id): #Delete Obj
    try:
      d=Account.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Account deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Account!','sys_error':str(e)}


  @staticmethod
  def searchAccount(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
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
      
      return {'res':res,'status':'info','msg':'Account Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Account!','sys_error':str(e)}


from .models import Instrument
class InstrumentManager:
  @staticmethod
  def createInstrument(name,accid,): #Crete an Obj
    try:
      
      
      t = Instrument(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Instrument got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Instrument','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Instrument','sys_error':str(e)}

  @staticmethod
  def getInstrument(id): # get Json
    try:
      t=Instrument.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Instrument returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Instrument having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Instrument','sys_error':str(e)}

  @staticmethod
  def getInstrumentObj(id): #get Obj
    try:
      t=Instrument.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Instrument Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Instrument having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Instrument','sys_error':str(e)}

  @staticmethod
  def updateInstrument(id,name,accid, ): #Update Obj
    try:
      res=InstrumentManager.getInstrumentObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Instrument Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Instrument','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Instrument','sys_error':str(e)}

  @staticmethod
  def deleteInstrument(id): #Delete Obj
    try:
      d=Instrument.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Instrument deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Instrument!','sys_error':str(e)}


  @staticmethod
  def searchInstrument(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Instrument!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewInstrument(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Instrument Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Instrument!','sys_error':str(e)}


from .models import Setting
class SettingManager:
  @staticmethod
  def createSetting(name,accid,): #Crete an Obj
    try:
      
      
      t = Setting(name=name,accid=accid,)
      
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'New Setting got created.'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Setting','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Setting','sys_error':str(e)}

  @staticmethod
  def getSetting(id): # get Json
    try:
      t=Setting.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      return {'res':res,'status':'info','msg':'Setting returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Setting having id <'+str(id)+'> Does not exist!','sys_error':''}      
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive Setting','sys_error':str(e)}

  @staticmethod
  def getSettingObj(id): #get Obj
    try:
      t=Setting.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Setting Object returned'}
    except ObjectDoesNotExist : 
      D_LOG()
      return {'res':None,'status':'error','msg':'The Setting having id <'+str(id)+'> Does not exist!','sys_error':''}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrive object Setting','sys_error':str(e)}

  @staticmethod
  def updateSetting(id,name,accid, ): #Update Obj
    try:
      res=SettingManager.getSettingObj(id)
      if res['res'] is None: return res
      t=res['res']
      
        
      
      t.name = name if name is not None else t.name;t.accid = accid if accid is not None else t.accid;             
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Setting Updated'}
    except IntegrityError as e:
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create Setting','sys_error':str(e),'help':'You are trying to violate Database Integrity like Forain key or One2One key.'}  
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update Setting','sys_error':str(e)}

  @staticmethod
  def deleteSetting(id): #Delete Obj
    try:
      d=Setting.objects.get(pk=id)
      d.delete()
      return {'res':None,'status':'info','msg':'one Setting deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete Setting!','sys_error':str(e)}


  @staticmethod
  def searchSetting(name,accid,page=None,limit=None,id=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if name is not None: Query['name__contains']=name
      if accid is not None: Query['accid']=accid #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      include =[u'name', 'id']
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
      return {'res':None,'status':'error','msg':'Not able to search Setting!','sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def minViewSetting(page=None,limit=None):
    try:
      res =None
      include =[u'name', 'id']
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
      
      return {'res':res,'status':'info','msg':'Setting Mini View returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search Setting!','sys_error':str(e)}

