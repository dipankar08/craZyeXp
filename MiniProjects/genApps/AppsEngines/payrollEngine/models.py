from datetime import datetime
from django.db import models
from .config import TT_SEV,TT_STATE,TT_TYPE
from CommonLib.customFields import ListField,DictField,SetField

class FYReport(models.Model):
    #List of MonthReport[] =...
    fy = models.CharField(max_length=100,null=False)#'xx-yy'
    net_debited = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    all_80cs = DictField(default={'HRA':0,'80C':0,'80CC':0},null=True,blank=True);
    net_pf_saved = models.IntegerField(default=None,null=True,blank=True) #sum of all PF
    #tax related stuff
    total_income = models.IntegerField(default=None,null=True,blank=True) #sum of 
    total_hrent_examed = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    total_gross = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    total_examed = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    total_taxable_pay =models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    calculated_tax = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    net_tax_payed = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    tax_due = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    
    #Investment Summary
    total_fixed_depot = DictField(default={'ALAHABAD':0,'HDFC':0,'ICICI':0},null=True,blank=True);
    total_inc_payed = DictField(default={'Life':0,'HDFC':0,'BAZAJ':0},null=True,blank=True);
    total_investment_nonRefund= DictField(default={'HomeCons':0,'a':0,'b':0},null=True,blank=True);
    total_investment_nointerest = DictField(default={'MIS':0},null=True,blank=True);
    
class MonthReport(models.Model):
    net_pay = models.IntegerField(default=None,null=True,blank=True)#Sum of all Inclome
    net_debit = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    net_tax = models.IntegerField(default=None,null=True,blank=True) #sum of all tax
    net_pf = models.IntegerField(default=None,null=True,blank=True) #sum of all PF
    other_exp = DictField(default={'house_rent':0,'food':0,'traval':0},null=True,blank=True);
    # Auto data
    # listOrgPay[] = [..]    

class Org(models.Model):
    name = models.CharField(max_length=100,null=False)
    summary = models.CharField(max_length=100,null=False)
    eid = models.IntegerField(default=None,null=True,blank=True)#EMP ID
    post = models.CharField(max_length=100,null=False)
    ctc = models.IntegerField(default=None,null=True,blank=True)
    ctc_break = DictField(default={},null=True,blank=True);
    
    joining_date = models.DateTimeField(auto_now=True)
    leaving_date = models.DateTimeField(default=datetime.now())
    
    #Access list of pay
    def __unicode__(self):
        return u"TT:%s : %s" % (self.id,self.name)
    
class OrgPay(models.Model):
    credit_break = DictField(default={},null=True,blank=True);
    debit_break = DictField(default={},null=True,blank=True);
    others_break = DictField(default={},null=True,blank=True);
    net_pay = models.IntegerField(default=None,null=True,blank=True)
    
    # Ref.
    org = models.ForeignKey(Org)
    month=models.ForeignKey(MonthReport)


    
