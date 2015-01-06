###########################################
## Author : Dipankar Dutta
## Title :
## Description:
## Function: Contains API and Backend call to do the task. The Brain of this Engine
###########################################
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict


from .models import Feedback
class FeedbackManager:
    @staticmethod
    def isIpInFeedback(ipaddress ):
        """ return True if IP address is already in use """
        try:
            t=Feedback.objects.filter(ipaddress = ipaddress )
            if t:
              return {'res':True,'status':'info','msg':'You have already submited a feedback( IP already exit in our database)'}
            else: 
              return {'res':False,'status':'info','msg':'You IP is not yet registered ! '}

        except Exception,e :
            return {'res':False,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def createFeedback(name,email,mobile,feedback,ipaddress ):
        try:
            res = FeedbackManager.isIpInFeedback(ipaddress)
            if res['res'] is True:
               return res
            t=Feedback(name=name,email=email,mobile=mobile,feedback=feedback,ipaddress = ipaddress )
            t.save()
            return {'res':model_to_dict(t),'status':'info','msg':'Thank you for your feedback'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def getAllFeedbackWithFilter(name=None,email=None,mobile=None, page=None,limit=None):
        try:
            Query={}
            if name is not None: Query['name']=name
            if email is not None: Query['email']=email
            if mobile is not None:  Query['mobile']=mobile

            d=Feedback.objects.filter(**Query)
            if page is not None: # doing pagination if enable.
                if limit is None: limit =10
                paginator = Paginator(d, limit)
                d= paginator.page(page)
            res=[model_to_dict(u,exclude=['history']) for u in d]
            return {'res':res,'status':'info','msg':'Here is all your feedback'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error, Cannot retrive feedback','sys_error':str(e)}
