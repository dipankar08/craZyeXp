from datetime import datetime
from django.db import models
from .config import TT_SEV,TT_STATE,TT_TYPE
from CommonLib.customFields import ListField,DictField,SetField

class Tickets(models.Model):
    uid = models.IntegerField(default=None,null=True,blank=True)
    summary = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=400,default=None,null=True,blank=True)
    author_name = models.CharField(max_length=400,default='guest',null=True,blank=True)
    author_email = models.EmailField(default=None,null=True,blank=True)

    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(default=datetime.now())

    state= models.CharField(max_length=40,choices = TT_STATE,default='ASSIGNED',null=True,blank=True)
    type= models.CharField(max_length=40,choices = TT_TYPE,default='BACKEND',null=True,blank=True)
    sav= models.CharField(max_length=40,choices = TT_SEV,default='AVERAGE',null=True,blank=True)
    tags= ListField(default=[],null=True,blank=True)

    history=ListField(default=[],null=True,blank=True)

    assigned =models.CharField(max_length=40,default=None,null=True,blank=True)

    #comments=ListField(default=[{'author':'admin','timestamp':datetime.now(),'msg':'Thanks for your TT. We will get back to you soon'}],null=True,blank=True)
    comments=ListField(default=[],null=True,blank=True)
    def __unicode__(self):
        return u"TT:%s : %s" % (self.id,self.summary)