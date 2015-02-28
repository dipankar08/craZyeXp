import pdb
from common import *
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import *
from django.db import *

from .models import PayRoll
class PayRollManager:
  @staticmethod
  def createPayRoll(type=None,month=None,year=None,source=None,category=None,subcategory=None,amount=None,actualamount=None,breakup={'hello':0},comment=None,): #Crete an Obj
    try:
      if type and not set(type).issubset(set([u'SalCredit', u'SalDebit', u'ReturnInvest', u'NoRetInvest'])) : return {'res':None,'status':'error','msg':"type must be either of [u'SalCredit', u'SalDebit', u'ReturnInvest', u'NoRetInvest'] ",'sys_error':''};
      if month and not set(month).issubset(set([u'Jan', u'Feb', u'Mar', u'April', u'May', u'June', u'July', u'Aug', u'Sept', u'Oct', u'Nov', u'Dec'])) : return {'res':None,'status':'error','msg':"month must be either of [u'Jan', u'Feb', u'Mar', u'April', u'May', u'June', u'July', u'Aug', u'Sept', u'Oct', u'Nov', u'Dec'] ",'sys_error':''};
      if year and not set(year).issubset(set([u'2011', u'2012', u'2013', u'2014', u'2015'])) : return {'res':None,'status':'error','msg':"year must be either of [u'2011', u'2012', u'2013', u'2014', u'2015'] ",'sys_error':''};
      if source and not set(source).issubset(set([u'Citrix', u'Amazon', u'IpInfusion', u'Microsoft', u'Other'])) : return {'res':None,'status':'error','msg':"source must be either of [u'Citrix', u'Amazon', u'IpInfusion', u'Microsoft', u'Other'] ",'sys_error':''};
      if category and not set(category).issubset(set([u'Basic', u'HRA', u'ConveyAllow', u'SplAllow', u'Reloc', u'SignIn', u'NoticeBuyOut', u'PF', u'ITax', u'Walfare', u'ProfTax', u'LIC', u'Bajaj', u'PPF', u'HouseCons', u'Rent', u'Other'])) : return {'res':None,'status':'error','msg':"category must be either of [u'Basic', u'HRA', u'ConveyAllow', u'SplAllow', u'Reloc', u'SignIn', u'NoticeBuyOut', u'PF', u'ITax', u'Walfare', u'ProfTax', u'LIC', u'Bajaj', u'PPF', u'HouseCons', u'Rent', u'Other'] ",'sys_error':''};
      
      
      
      t = PayRoll(type=type,month=month,year=year,source=source,category=category,subcategory=subcategory,amount=amount,actualamount=actualamount,breakup=breakup,comment=comment,)
      t.log_history = [{'type':'CREATE','msg':'Created new entry !','ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'New PayRoll got created.'}    
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to create PayRoll:'+getCustomException(e),'sys_error':str(e)}
  # Note taht to access all please call search method.. PayRollManager.searchPayRoll()
  @staticmethod
  def getPayRoll(id,mv=None): # get Json
    try:
      t=PayRoll.objects.get(pk=id)
      res = model_to_dict(t)
      if res is not None:
        pass
        
        
      if mv != None:
        #send Mini view only..
        include =[u'type', u'source', u'category', u'amount', 'id']
        res=dict_reduce(res,include)
      return {'res':res,'status':'info','msg':'PayRoll returned'}
   
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not Able to retrive PayRoll:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def getPayRollObj(id): #get Obj
    try:
      t=PayRoll.objects.get(pk=id)
      return {'res':t,'status':'info','msg':'PayRoll Object returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to retrieve object PayRoll:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def updatePayRoll(id,type=None,month=None,year=None,source=None,category=None,subcategory=None,amount=None,actualamount=None,breakup={'hello':0},comment=None, ): #Update Obj
    try:
      res=PayRollManager.getPayRollObj(id)
      if res['res'] is None: return res
      t=res['res']
      
      if type and not set(type).issubset(set([u'SalCredit', u'SalDebit', u'ReturnInvest', u'NoRetInvest'])) : return {'res':None,'status':'error','msg':"type must be either of [u'SalCredit', u'SalDebit', u'ReturnInvest', u'NoRetInvest'] ",'sys_error':''};
      if month and not set(month).issubset(set([u'Jan', u'Feb', u'Mar', u'April', u'May', u'June', u'July', u'Aug', u'Sept', u'Oct', u'Nov', u'Dec'])) : return {'res':None,'status':'error','msg':"month must be either of [u'Jan', u'Feb', u'Mar', u'April', u'May', u'June', u'July', u'Aug', u'Sept', u'Oct', u'Nov', u'Dec'] ",'sys_error':''};
      if year and not set(year).issubset(set([u'2011', u'2012', u'2013', u'2014', u'2015'])) : return {'res':None,'status':'error','msg':"year must be either of [u'2011', u'2012', u'2013', u'2014', u'2015'] ",'sys_error':''};
      if source and not set(source).issubset(set([u'Citrix', u'Amazon', u'IpInfusion', u'Microsoft', u'Other'])) : return {'res':None,'status':'error','msg':"source must be either of [u'Citrix', u'Amazon', u'IpInfusion', u'Microsoft', u'Other'] ",'sys_error':''};
      if category and not set(category).issubset(set([u'Basic', u'HRA', u'ConveyAllow', u'SplAllow', u'Reloc', u'SignIn', u'NoticeBuyOut', u'PF', u'ITax', u'Walfare', u'ProfTax', u'LIC', u'Bajaj', u'PPF', u'HouseCons', u'Rent', u'Other'])) : return {'res':None,'status':'error','msg':"category must be either of [u'Basic', u'HRA', u'ConveyAllow', u'SplAllow', u'Reloc', u'SignIn', u'NoticeBuyOut', u'PF', u'ITax', u'Walfare', u'ProfTax', u'LIC', u'Bajaj', u'PPF', u'HouseCons', u'Rent', u'Other'] ",'sys_error':''};
      
      changes='';
      changes += '< type:'+ str(t.type) +' -> '+str( type)+' >'  if type is not None  else '' 
      changes += '< month:'+ str(t.month) +' -> '+str( month)+' >'  if month is not None  else '' 
      changes += '< year:'+ str(t.year) +' -> '+str( year)+' >'  if year is not None  else '' 
      changes += '< source:'+ str(t.source) +' -> '+str( source)+' >'  if source is not None  else '' 
      changes += '< category:'+ str(t.category) +' -> '+str( category)+' >'  if category is not None  else '' 
      changes += '< subcategory:'+ str(t.subcategory) +' -> '+str( subcategory)+' >'  if subcategory is not None  else '' 
      changes += '< amount:'+ str(t.amount) +' -> '+str( amount)+' >'  if amount is not None  else '' 
      changes += '< actualamount:'+ str(t.actualamount) +' -> '+str( actualamount)+' >'  if actualamount is not None  else '' 
      changes += '< breakup:'+ str(t.breakup) +' -> '+str( breakup)+' >'  if breakup is not None  else '' 
      changes += '< comment:'+ str(t.comment) +' -> '+str( comment)+' >'  if comment is not None  else '' 
      if changes: t.log_history.append({'type':'UPDATE','msg': changes ,'ts':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        
      
      t.type = type if type is not None else t.type;t.month = month if month is not None else t.month;t.year = year if year is not None else t.year;t.source = source if source is not None else t.source;t.category = category if category is not None else t.category;t.subcategory = subcategory if subcategory is not None else t.subcategory;t.amount = amount if amount is not None else t.amount;t.actualamount = actualamount if actualamount is not None else t.actualamount;t.breakup = breakup if breakup is not None else t.breakup;t.comment = comment if comment is not None else t.comment;             
      t.save()
      
      return {'res':model_to_dict(t),'status':'info','msg':'PayRoll Updated'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to update PayRoll:'+getCustomException(e,id),'sys_error':str(e)}

  @staticmethod
  def deletePayRoll(id): #Delete Obj
    
    return {'res':None,'status':'error','msg':'Entry Deletion is not allowed by configuration! '}
    
    try:
      t=PayRoll.objects.get(pk=id)
      
      t.delete()
      return {'res':None,'status':'info','msg':'one PayRoll deleted!'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to delete PayRoll:'+getCustomException(e,id),'sys_error':str(e)}


  @staticmethod
  def searchPayRoll(type=None,month=None,year=None,source=None,category=None,subcategory=None,amount=None,actualamount=None,breakup={'hello':0},comment=None,page=None,limit=None,id=None,mv=None): # Simple Serach 
    try:
      Query={}
      if id is not None: Query['id']=id
      
      if type is not None: Query['type']=type
      if month is not None: Query['month']=month
      if year is not None: Query['year']=year
      if source is not None: Query['source']=source
      if category is not None: Query['category']=category
      if subcategory is not None: Query['subcategory__contains']=subcategory
      if amount is not None: Query['amount']=amount
      if actualamount is not None: Query['actualamount']=actualamount
      if breakup is not None: Query['breakup']=breakup
      if comment is not None: Query['comment__contains']=comment #if state is not None: Query['state_contains']=state
      
      # We have Some Fuild to Select in Any Ops.
      if mv == None:
        include =[u'type', u'source', u'category', u'amount', 'id']
      else:
        include = mv
      dd=PayRoll.objects.filter(**Query).values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
    
      return {'res':res,'status':'info','msg':'PayRoll search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search PayRoll:'+getCustomException(e),'sys_error':str(e)}

  

  #Advance search is Implemented here..
  @staticmethod
  def advSearchPayRoll(id,query_str, page=None,limit=None,orderBy=None,include=None,exclude=None):
    try:
      Qstr = query_str
      print "    [Query] ADVANCE QUERY EXECUTED AS :", Qstr
      if Qstr:
        try:
          Qstr= eval(Qstr)
        except Exception,e :
          D_LOG()
          return {'res':None,'status':'error','msg':'PayRoll Opps!, The Query is not valid as you made some syntax error ','sys_error':str(e)}
      if Qstr:
        dd=PayRoll.objects.filter(Qstr)
      else:
        dd=PayRoll.objects.filter()
      #Oder_by Here.
      if orderBy:
        dd= dd.order_by(*orderBy)

      #Selecting fields.
      if include:
        pass
      else:
        include =[u'type', u'source', u'category', u'amount', 'id']+['id']
      dd=list(dd.values(*include))              
    
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########

      return {'res':res,'status':'info','msg':'PayRoll search returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search PayRoll!','sys_error':str(e)}
  



  #Advance search is Implemented here..
  @staticmethod
  def minViewPayRoll(page=None,limit=None):
    try:
      res =None
      include =[u'type', u'source', u'category', u'amount', 'id']
      dd=PayRoll.objects.values(*include)
      
      ### pagination ##########
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page) 
      res ={}      
      res['data'] = list(dd.object_list)
      res['current_page'] =  page if res['data'] else 0
      res['max'] = paginator.num_pages if res['data']  else 0 
      ### end of pagination ##########
      
      return {'res':res,'status':'info','msg':'Mini View PayRoll  returned'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search PayRoll!','sys_error':str(e)}


  #Advance search is Implemented here..
  @staticmethod
  def getPayRoll_quick_search(q,page=None,limit=None):
    try:
      res = None
      include =['id','category']
      dd=PayRoll.objects.filter(category__startswith=q).values(*include)
      if page is None: page=1
      if limit is None: limit =10
      paginator = Paginator(dd, limit)
      dd= paginator.page(page)      
      res = list(dd.object_list)
      if not res: return {'res':res,'status':'info','msg':'Nothing match with your query'} 
      return {'res':res,'status':'success','msg':'PayRoll match with your query'}
    except Exception,e :
      D_LOG()
      return {'res':None,'status':'error','msg':'Not able to search PayRoll!','sys_error':str(e)}

