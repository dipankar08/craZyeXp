###########################################
## Author : Dipankar Dutta
## Title :
## Description:
## Function: Contains API and Backend call to do the task. The Brain of this Engine
###########################################
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

from .models import Tickets
class TTManager:
    @staticmethod
    def createTicket(summary,description,author_name,author_email,uid=None,):
        try:
            t=Tickets(uid=uid,summary=summary,description=description,author_name=author_name,author_email=author_email)
            t.comments=[{'author':'admin','timestamp':str(datetime.now()),'msg':'Thanks for your TT. We will get back to you soon'}]
            t.history = [{'author':'admin','timestamp':str(datetime.now()),'what':'created this issue'}]
            t.save()
            return {'res':model_to_dict(t),'status':'info','msg':'Thank you for leting us this problem'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def getTickets(tid):
        try:
            t=Tickets.objects.get(pk=tid)
            return {'res':model_to_dict(t),'status':'info','msg':'TT returned'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def getTicketsObj(tid):
        try:
            t=Tickets.objects.get(pk=tid)
            return {'res':t,'status':'info','msg':'TT returned'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def updateTicket(tid,state=None,type=None,sav=None,tag_list=[],assigned=None ):
        try:
            res=TTManager.getTicketsObj(tid)
            if res['res'] is None: return res
            t=res['res']
            modified_date=datetime.now()
            changes=''
            if state is not None:t.state= state;changes+='new State:%s,'%state
            if type is not None:t.type= type;changes +='new type:%s,'%type
            if sav is not None:t.sav= sav;changes +='new sav:%s,'%sav
            if assigned is not None:t.assigned= assigned;changes +='new assigned:%s,'%assigned
            if tag_list is not None:t.tags+= tag_list;changes +='Added tag_list:%s,'%tag_list

            t.history.append({'author':'admin','timestamp':str(datetime.now()),'what':'Update this TT by %s'%changes})
            t.save()
            return {'res':model_to_dict(t),'status':'info','msg':'TT Updated'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def changeStateTicket(tid,state=None):
        try:
            res=TTManager.getTicketsObj(tid)
            if res['res'] is None: return res
            t=res['res']
            if state is not None:t.state= state
            t.history.append({'author':'admin','timestamp':str(datetime.now()),'what':'ticket state change to %s' %state})
            t.save()
            return {'res':model_to_dict(t),'status':'info','msg':'State Changed Successfully!'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def addCommentOnTickets(tid,author,msg):
        try:
            res=TTManager.getTicketsObj(tid)
            if res['res'] is None: return res
            t=res['res']
            t.comments.append({'author':author,'timestamp':str(datetime.now()),'msg':msg})
            t.history.append({'author':'admin','timestamp':str(datetime.now()),'what':'Comment Added At %s' %datetime.now()})
            t.save()
            return {'res':model_to_dict(t),'status':'info','msg':'New comment got added!'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def getAllTicketsWithFilter(uid=None,state=None,type=None,sav=None,tag=None,assigned=None,page=None,limit=None):
        try:
            Query={}
            if uid is not None: Query['uid']=uid
            if state is not None: Query['state']=state
            if type is not None:  Query['type']=type
            if sav is not None: Query['sav']=sav
            if assigned is not None: Query['assigned']=assigned
            if tag is not None: Query['tags__contains']=tag
            d=Tickets.objects.filter(**Query)
            if page is not None: # doing pagination if enable.
                if limit is None: limit =10
                paginator = Paginator(d, limit)
                d= paginator.page(page)
            res=[model_to_dict(u,exclude=['history']) for u in d]
            return {'res':res,'status':'info','msg':'All TT returned'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}
    @staticmethod
    def getHistoryOfTicket(tid):
        try:
            res=TTManager.getTicketsObj(tid)
            if res['res'] is None: return res
            t=res['res']
            return {'res':t.history,'status':'info','msg':'History Returned!'}
        except Exception,e :
            return {'res':None,'status':'error','msg':'Opps!! there are some Error','sys_error':str(e)}