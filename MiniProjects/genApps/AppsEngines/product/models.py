from common import D_LOG
from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField
class Book(models.Model):
  name = models.CharField(max_length=100,null=False)
  icbn = models.IntegerField(default=None,null=True,blank=True)
  pub_date = models.DateTimeField(auto_now=True,default=datetime.now())
  toc = DictField(default={'house_rent':0,'food':0,'traval':0},null=True,blank=True)
  author = ListField(default=[1,2,3],null=True,blank=True)
  publication = ListField(default=[1,2,3],null=True,blank=True)
  log_history = ListField(default=[{'type':'Unknown', 'msg':'Gods knows the event','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}],null=True,blank=True);
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



