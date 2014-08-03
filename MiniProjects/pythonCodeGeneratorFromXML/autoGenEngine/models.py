from datetime import datetime
from django.db import models
from CommonLib.customFields import ListField,DictField,SetField
class Student(models.Model):
  name = models.CharField(max_length=100,null=False)
  roll = models.IntegerField(default=None,null=True,blank=True)
  date = models.DateTimeField(auto_now=True,default=datetime.now())

  def __unicode__(self):
    return u"Student : %s",  (self.id)
