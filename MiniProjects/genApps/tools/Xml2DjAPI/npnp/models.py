import pdb
from common import D_LOG
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField

#*************Defining model for Parent ***************
class Parent(models.Model):
  name = models.CharField(max_length=100,null=False)
  email = models.CharField(max_length=100,null=True)
  phone = models.CharField(max_length=100,null=True)
  occupation = models.CharField(max_length=100,null=True)
  address = models.CharField(max_length=100,null=True)
  income = models.CharField(max_length=100,null=True)
  relationship = models.CharField(default=None,null=True,blank=True)
  secondary_contact = models.CharField(max_length=100,null=True)

#*************End Defining model for Parent ************


#*************Defining model for Student ***************
class Student(models.Model):
  uid = models.CharField(max_length=100,null=True)
  name = models.CharField(max_length=100,null=True)
  email = models.CharField(max_length=100,null=True)
  phone = models.CharField(max_length=100,null=True)
  address = models.CharField(max_length=500,null=True)
  dob = models.CharField(max_length=100,null=True)
  doj = models.DateTimeField(max_length=100,null=True)
  gender = models.CharField(max_length=100,null=True)
  parent = models.ForeignKey(to=Parent)
  myclass = models.ManyToManyField(to=MyClass)
  roll = models.CharField(max_length=100,null=True)
  section = ListField(default=[1,2,3],null=True,blank=True)

#*************End Defining model for Student ************


#*************Defining model for Employee ***************
class Employee(models.Model):
  name = models.CharField(max_length=100,null=False)
  uid = models.CharField(max_length=100,null=False)
  address = models.CharField(default=None,null=True,blank=True)
  age = models.IntegerField(default=None,null=True,blank=True)
  designation = models.CharField(default=None,null=True,blank=True)
  rank = models.CharField(default=None,null=True,blank=True)
  max_qualification = models.CharField(default=None,null=True,blank=True)
  meretarial_status = models.CharField(default=None,null=True,blank=True)
  gender = models.CharField(default=None,null=True,blank=True)
  dob = models.CharField(max_length=100,null=True)
  doj = models.DateTimeField(max_length=100,null=True)
  categories = ListField(default=[1,2,3],null=True,blank=True)

#*************End Defining model for Employee ************


#*************Defining model for MyClass ***************
class MyClass(models.Model):
  name = models.CharField(max_length=100,null=False)
  room = models.CharField(max_length=100,null=True)
  class_teacher = models.ManyToManyField(to=Employee)
  subjects = models.ManyToManyField(to=Subject)

#*************End Defining model for MyClass ************


#*************Defining model for Subject ***************
class Subject(models.Model):
  name = models.CharField(max_length=100,null=False)
  uid = models.CharField(max_length=100,null=True)
  syllabus = models.CharField(max_length=1000,null=True)
  ref_book = models.CharField(max_length=1000,null=True)
  teacher = models.ManyToManyField(to=Employee)
  categorise = ListField(null=True,blank=True)
  group = ListField(null=True,blank=True)
  mark_division = DictField(null=True,blank=True)

#*************End Defining model for Subject ************


#*************Defining model for Exam ***************
class Exam(models.Model):
  name = ListField(null=True,blank=True)
  subject = models.ForeignKey(to=Subject)
  date = models.DateTimeField(auto_now=True,default=datetime.now())
  classRoom = models.CharField(max_length=1000,null=True)
  time = models.CharField(max_length=1000,null=True)
  teacher = models.ManyToManyField(to=Employee)

#*************End Defining model for Exam ************


#*************Defining model for Mark ***************
class Mark(models.Model):
  student = models.ForeignKey(to=Student)
  subject = models.ForeignKey(to=Subject)
  exam = models.ForeignKey(to=Exam)
  written = models.IntegerField(null=True,blank=True)
  written = models.IntegerField(null=True,blank=True)
  written = models.IntegerField(null=True,blank=True)
  total = models.IntegerField(null=True,blank=True)
  comment = models.CharField(max_length=1000,null=True)

#*************End Defining model for Mark ************


#*************Defining model for Result ***************
class Result(models.Model):
  exam = models.ForeignKey(to=Exam)
  Student = models.ManyToManyField(to=Student)
  division = models.CharField(max_length=100,null=False)
  total = models.IntegerField(default=None,null=True,blank=True)
  percentage = models.IntegerField(default=None,null=True,blank=True)
  division = ListField(null=True,blank=True)
  comment = models.CharField(max_length=1000,null=True)

#*************End Defining model for Result ************


#*************Defining model for Attendance ***************
class Attendance(models.Model):
  student = models.ForeignKey(to=Student)
  myclass = models.ForeignKey(to=MyClass)
  total = models.IntegerField(default=None,null=True,blank=True)
  percentage = models.IntegerField(default=None,null=True,blank=True)
  comment = models.CharField(max_length=100,null=False)

#*************End Defining model for Attendance ************


#*************Defining model for Sport ***************
class Sport(models.Model):
  name = models.CharField(max_length=100,null=False)
  position = DictField(null=True,blank=True)
  student = models.ManyToManyField(to=Student)
  categories = ListField(null=True,blank=True)

#*************End Defining model for Sport ************


#*************Defining model for Event ***************
class Event(models.Model):
  name = models.CharField(max_length=100,null=False)
  details = models.CharField(max_length=100,null=False)
  categories = ListField(null=True,blank=True)
  date = models.DateTimeField(auto_now=True,default=datetime.now())

#*************End Defining model for Event ************


#*************Defining model for Discipline ***************
class Discipline(models.Model):
  name = models.CharField(max_length=100,null=False)
  details = models.CharField(max_length=100,null=False)
  categories = ListField(null=True,blank=True)

#*************End Defining model for Discipline ************


#*************Defining model for Notice ***************
class Notice(models.Model):
  title = models.CharField(max_length=100,null=False)
  details = models.CharField(max_length=100,null=False)
  categories = ListField(null=True,blank=True)
  date = models.DateTimeField(auto_now=True,default=datetime.now())

#*************End Defining model for Notice ************


#*************Defining model for Instrument ***************
class Instrument(models.Model):
  name = models.CharField(max_length=100,null=False)
  details = models.CharField(max_length=100,null=False)
  categories = ListField(null=True,blank=True)
  purchage_date = models.DateTimeField(auto_now=True,default=datetime.now())
  count = models.IntegerField(null=True,blank=True)

#*************End Defining model for Instrument ************


#*************Defining model for Account ***************
class Account(models.Model):
  name = models.CharField(max_length=100,null=False)
  email = models.CharField(default=None,null=True,blank=True)
  password_hash = models.CharField(default=None,null=True,blank=True)
  salt_hash = models.CharField(default=None,null=True,blank=True)
  active = models.CharField(default=None,null=True,blank=True)
  clue = models.CharField(default=None,null=True,blank=True)

#*************End Defining model for Account ************


#*************Defining model for Setting ***************
class Setting(models.Model):
  name = models.CharField(max_length=100,null=False)
  account = models.ManyToManyField(to=Account)
  theme = ListField(null=True,blank=True)

#*************End Defining model for Setting ************

