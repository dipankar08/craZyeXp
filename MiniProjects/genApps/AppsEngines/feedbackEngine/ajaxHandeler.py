###########################################
## Author : Dipankar Dutta
## Title :
## Description:
## Function: Contains XHR Request handlers- hence it;s a Ajax Request Handlers
###########################################
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CommonLib import utils


######################3  Start Feedback Operation using Ajax #########################
from .api import FeedbackManager
@csrf_exempt
def ajax_feedback(request):
    import pdb
    #pdb.set_trace()
    res=None
    if request.method == 'GET':
        page=request.GET.get('page',None)
        limit=request.GET.get('limit',None)

        name=request.GET.get('name',None)
        email=request.GET.get('email',None)
        mobile=request.GET.get('mobile',None)
        res=FeedbackManager.getAllFeedbackWithFilter(name=name, email=email,mobile=mobile,page=page,limit=limit)

    elif request.method == 'POST':
        name=request.POST.get('name',None)
        email=request.POST.get('email',None)
        mobile=request.POST.get('mobile',None)
        feedback=request.POST.get('feedback',None)
        ipaddress  = utils.get_client_ip(request)
        res=FeedbackManager.createFeedback(name=name,email=email,mobile=mobile,feedback=feedback,ipaddress = ipaddress )
    elif request.method ==  'DELETE':
        #Pass No Delete
        pass
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')

######################  End Address Operation ############################
