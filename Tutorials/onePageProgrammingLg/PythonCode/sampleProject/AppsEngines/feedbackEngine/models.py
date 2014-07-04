from datetime import datetime
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100,null=False)
    email = models.EmailField(default=None,null=False,blank=False)
    mobile = models.CharField(max_length=100,default=None,null=True,blank=True)
    feedback = models.CharField(max_length=1000,default='guest',null=False,blank=False)
    ipaddress = models.CharField(max_length=20,null=True,blank=True)
    created_date = models.DateTimeField(auto_now=True)
   
    def __unicode__(self):
        return u"TT:%s : %s" % (self.id,self.name)
