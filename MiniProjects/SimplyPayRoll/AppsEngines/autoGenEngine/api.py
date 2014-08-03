from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from .models import Student
class StudentManager:
  @staticmethod
  def createStudent(name,roll,):
    try:
      new = Student(name=name,roll=roll,)
      new.save()
      return {'res':model_to_dict(new),'status':'info','msg':'New Student got created.'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to create Student','sys_error':str(e)}
  @staticmethod    
  def getStudent(id):
    try:
      t=Student.objects.get(pk=id)
      return {'res':model_to_dict(t),'status':'info','msg':'Student returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not Able to retrive Student','sys_error':str(e)}
  @staticmethod
  def getStudentObj(id):
    try:
      t=Student.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'Student Object returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to retrive object Student','sys_error':str(e)}
  @staticmethod
  def updateStudent(id,name,roll, ):
    try:
      res=StudentManager.getStudentObj(id)
      if res['res'] is None: return res
      t=res['res']
      t.name = name if name is not None else t.name;t.roll = roll if roll is not None else t.roll;
      t.save()
      return {'res':model_to_dict(t),'status':'info','msg':'Student Updated'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to update Student','sys_error':str(e)}
  @staticmethod
  def deleteStudent(id):
    try:
      d=Student.objects.get(pk=id)
      d.delete()
      return {'res':d,'status':'info','msg':'one Student deleted!'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to delete Student!','sys_error':str(e)}
              
                        
  @staticmethod
  def searchStudent(name,roll,page=None,limit=None,id=None):
    try:
      Query={}
      if id is not None: Query['id']=id
      if name is not None: Query['name']=name;
      if roll is not None: Query['roll']=roll; #if state is not None: Query['state_contains']=state
      d=Student.objects.filter(**Query)
      if page is not None: # doing pagination if enable.
        if limit is None: limit =10
        paginator = Paginator(d, limit)
        d= paginator.page(page)
      res=[model_to_dict(u) for u in d]
      return {'res':res,'status':'info','msg':'Student search returned'}
    except Exception,e :
      return {'res':None,'status':'error','msg':'Not able to search Student!','sys_error':str(e)}
     
