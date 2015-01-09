import pdb
from common import *
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField

#*************Defining model for Code ***************
class Code(models.Model):
  name = models.CharField(max_length=50,null=False)
  short_desc = models.CharField(max_length=150,null=False)
  full_desc = models.CharField(max_length=2000,null=True,blank=True)
  main = models.CharField(max_length=5000,null=True,blank=True)
  func = models.CharField(max_length=10000,null=True,blank=True)
  input = models.CharField(max_length=5000,null=True,blank=True)
  solution = models.CharField(max_length=5000,null=True,blank=True)
  level = models.CharField(max_length=5000,null=True,blank=True)
  language = models.CharField(max_length=5000,null=True,blank=True)
  compilation = models.CharField(max_length=5000,null=True,blank=True)
  tag = ListField(null=True,blank=True)
  topic = ListField(null=True,blank=True)
  log_history = ListField(default=[{'type':'Unknown', 'msg':'Gods knows the event','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}],null=True,blank=True);
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

#*************End Defining model for Code ************

