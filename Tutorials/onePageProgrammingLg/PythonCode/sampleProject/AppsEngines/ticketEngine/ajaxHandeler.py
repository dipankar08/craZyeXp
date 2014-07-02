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


######################3  Start TT Operation using Ajax #########################
from .api import TTManager
@csrf_exempt
def ajax_TT(request,tid=None):
    res=None

    if request.method == 'GET':
        page=request.GET.get('page',None)
        limit=request.GET.get('limit',None)

        state=request.GET.get('state',None)
        uid=request.GET.get('uid',None)
        type=request.GET.get('type',None)
        sav=request.GET.get('sav',None)
        tag=request.GET.get('tag',None)
        assigned=request.GET.get('assigned',None)
        page=request.GET.get('page',None)
        limit=request.GET.get('limit',None)
        if tid is not None: # Get perticular Info
            res= TTManager.getTickets(tid)
        else:
            # General Serach
            res=TTManager.getAllTicketsWithFilter(uid=uid, state=state,type=type,sav=sav,tag=tag,assigned=assigned,page=page,limit=limit)

    elif request.method == 'POST':

        if tid is not None: #Update
            state=request.POST.get('state',None)
            type=request.POST.get('type',None)
            sav=request.POST.get('sav',None)
            tag_list=request.POST.get('tag_list','').split(',')
            assigned=request.POST.get('assigned',None)
            res=TTManager.updateTicket(tid=tid,state=state,type=type,sav=sav,tag_list=tag_list,assigned=assigned)
        else:
            # Upload new file
            uid=request.POST.get('uid',None)
            summary=request.POST.get('summary',None)
            description=request.POST.get('description',None)
            author_name=request.POST.get('author_name',None)
            author_email=request.POST.get('author_email',None)
            res=TTManager.createTicket(uid=uid,summary=summary,description=description,author_name=author_name,author_email=author_email)

    elif request.method ==  'DELETE':
        #Pass No Delete
        pass
    return HttpResponse(json.dumps(res,default=json_util.default),mimetype = 'application/json')

@csrf_exempt
def ajax_changeState(request,tid):
    return HttpResponse(json.dumps(TTManager.changeStateTicket(tid=tid,state=request.POST.get('state',None)),default=json_util.default),
        mimetype = 'application/json')

@csrf_exempt
def ajax_commentOnTT(request,tid):
    return HttpResponse(json.dumps(TTManager.addCommentOnTickets(tid=tid, author=request.POST.get('author',None),
        msg=request.POST.get('msg',None)),default=json_util.default), mimetype = 'application/json')

@csrf_exempt
def ajax_getTTHistory(request,tid):
    return HttpResponse(json.dumps(TTManager.getHistoryOfTicket(tid=tid)), mimetype = 'application/json')


######################  End Address Operation ############################
