import pdb
from common import *
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField

#*************Defining model for PayRoll ***************
class PayRoll(models.Model):
  type = ListField(null=True,blank=True)
  month = ListField(null=True,blank=True)
  year = ListField(null=True,blank=True)
  source = ListField(null=True,blank=True)
  category = ListField(null=True,blank=True)
  subcategory = models.CharField(max_length=200,null=False)
  amount = models.IntegerField(default=None,null=True,blank=True)
  actualamount = models.IntegerField(default=None,null=True,blank=True)
  breakup = DictField(null=True,blank=True)
  comment = models.CharField(max_length=100,null=False)
  log_history = ListField(default=[{'type':'Unknown', 'msg':'Gods knows the event','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}],null=True,blank=True);
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

#*************End Defining model for PayRoll ************

