###########################################################
#  This is Stubs : App dev shroud fill it with logic      #
#                                                         #
###########################################################
import pdb
from bson import json_util
from django.http import HttpResponse

from CommonLib.Token import verifyToken
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def authenticate(func):
  " This is a decorator to do the authetication logic "
  def inner(*args, **kwargs): 
    #print "Arguments were: %s, %s" % (args, kwargs)   
    #pdb.set_trace()   
    ###############################################
    request = args[0]
    if request.GET.get('nokey') == None:
      token =  request.GET.get('token') if request.GET.get('token') else request.POST.get('token') # GET Enjoy More Precidency
      license =  request.GET.get('license') if request.GET.get('license') else request.POST.get('license')
      dataId =  request.GET.get('id') if request.GET.get('id') else request.POST.get('id')
      ip = get_client_ip(request)
      lres= verifyToken(str(token),ip=str(ip),dataId=str(dataId),license=str(license))
      if lres[0] == False:
        #Lincese fail 
        res = {'res':None,'status':'error','msg':'Invalid License or Expaired!','short_desc' :str(lres[1])}  
        return HttpResponse(json_util.json.dumps(res,default=json_util.default),content_type = 'application/json')        
    ###############################################
    return func(*args, **kwargs) 
  return inner
