import pdb
from common import D_LOG
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField
class Student(models.Model):
  uid = models.CharField(max_length=100,null=True)
  name = models.CharField(max_length=100,null=True)
  email = models.CharField(max_length=100,null=True)
  phone = models.CharField(max_length=100,null=True)
  address = models.CharField(max_length=500,null=True)
  dob = models.CharField(max_length=100,null=True)
  doj = models.DateTimeField(max_length=100,null=True)
  gender = models.CharField(max_length=100,null=True)
  Parent = models.ForeignKey(to=Parent)
  class = models.ManyToManyField(to=Class)
  roll = models.CharField(max_length=100,null=True)
  section = ListField(default=[1,2,3],null=True,blank=True)



class Employee(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Parent(models.Model):
  name = models.CharField(max_length=100,null=False)
  email = models.CharField(max_length=100,null=True)
  phone = models.CharField(max_length=100,null=True)
  occupation = models.CharField(max_length=100,null=True)
  address = models.CharField(max_length=100,null=True)
  income = models.CharField(max_length=100,null=True)
  relationship = models.CharField(default=None,null=True,blank=True)
  secondary_contact = models.CharField(max_length=100,null=True)



class Class(models.Model):
  name = models.CharField(max_length=100,null=False)
  room = models.CharField(max_length=100,null=True)
  class_teacher = models.ManyToManyField(to=Employee)
  subjects = models.ManyToManyField(to=Subject)



class Subject(models.Model):
  name = models.CharField(max_length=100,null=False)
  uid = models.CharField(max_length=100,null=True)
  syllabus = models.CharField(max_length=100,null=True)
  accid = models.IntegerField(default=None,null=True,blank=True)
  teacher = models.ManyToManyField(to=Employee)
  categorise = ListField(default=['practical'],null=True,blank=True)
  group = ListField(default=['sience'],null=True,blank=True)



class Mark(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Result(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Exam(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Attendance(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Fees(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Fund(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class LibBook(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Leaves(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class PayRoll(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Sport(models.Model):
  name = models.CharField(max_length=100,null=False)



class Event(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Discipline(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Notice(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Account(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Instrument(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



class Setting(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)



