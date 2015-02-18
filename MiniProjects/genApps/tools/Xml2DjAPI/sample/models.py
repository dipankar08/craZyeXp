import pdb
from common import *
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField

#*************Defining model for Author ***************
class Author(models.Model):
  name = models.CharField(max_length=100,null=True)
  date = models.DateTimeField(auto_now=True,default=datetime.now())
  life = DictField(null=True,blank=True)
  mych = ListField(null=True,blank=True)
  read_only = models.BooleanField(default=True)

#*************End Defining model for Author ************


#*************Defining model for Publication ***************
class Publication(models.Model):
  name = models.CharField(max_length=100,null=False)
  accid = models.IntegerField(default=None,null=True,blank=True)

#*************End Defining model for Publication ************


#*************Defining model for TOC ***************
class TOC(models.Model):
  name = models.CharField(max_length=100,null=False)

#*************End Defining model for TOC ************


#*************Defining model for Book ***************
class Book(models.Model):
  name = models.CharField(max_length=100,null=False)
  authors = models.ManyToManyField(to=Author)
  reg = models.IntegerField(default=None,null=True,blank=True)
  publication = models.ManyToManyField(to=Publication)
  toc = models.OneToOneField(to=TOC,null=True,blank=True)
  tag1 = ListField(default=[1,2,3],null=True,blank=True)
  tag2 = ListField(default=[1,2,3],null=True,blank=True)
  mych = ListField(default=[1,2,3],null=True,blank=True)
  mych2 = ListField(default=[1,2,3],null=True,blank=True)
  log_history = ListField(default=[{'type':'Unknown', 'msg':'Gods knows the event','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}],null=True,blank=True);
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

#*************End Defining model for Book ************

