import pdb
from common import *
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField

#*************Defining model for User ***************
class User(models.Model):
  uname = models.CharField(max_length=100,null=False)
  fname = models.CharField(max_length=100,null=True)
  lname = models.CharField(max_length=100,null=True)
  passwd = models.CharField(max_length=100,null=False)
  email = models.CharField(max_length=400,null=False)
  dob = models.DateTimeField(auto_now=True,default=datetime.now())
  desc = models.CharField(max_length=400,null=True)
  pic_url = models.CharField(max_length=400,null=True)
  address = models.CharField(max_length=700,null=True)
  social_id = DictField(null=True,blank=True)
  payload = DictField(null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

#*************End Defining model for User ************

