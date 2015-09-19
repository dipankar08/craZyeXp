#################################
# name : utils.py
# target : store all util functions
#################################
import json
from bson import json_util
import pdb

from CommonLib.Logs import Log
from django.http import HttpResponse
def get_client_ip(request):
    """ return IP address for a request in a string format  """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

##################################
# Convert Unicode from Ascii Encoded to unicode format.
#Example: 
# a = {'code': 'exam', 'list': [{'note': '2', 'right': '2', 'question': 'Tr\xe0n V?n H\xf9ng', 'answers': ['etreetetetetret', 'reteretet', 'tedtetetet', 'etetetet']}], 'id': 1, 'level': 1}
# json.dumps(a, encoding='latin1')
'{"code": "exam", "list": [{"note": "2", "right": "2", "question": "Tr\\u00e0n V?n H\\u00f9ng", "answers": ["etreetetetetret", "reteretet", "tedtetetet", "etetetet"]}], "id": 1, "level": 1}'
##################################
def decodeUnicodeDirectory(res):
   try:
      return json.dumps(res,default=json_util.default)
   except UnicodeDecodeError:
      return json.dumps(res, encoding='latin1')
   except Exception ,e:
      x = Log(e)
      return json.dumps({'status':'error','msg':'Your output contains a non-decodable unicode','callstack':x}, encoding='latin1')
      
def RequestGetToDict(x):
    x = dict(x)
    y={}
    for k,v in x.items():
        y[k]=v[0]
    return y
    
""" Convert String to list """
def str2List(a):
    if isinstance(a,list):
        return a
    elif isinstance(a,str):
        if ',' in a:
            return a.split(',')
        if ' ' in a:
            return a.split(' ')
        if '\n' in a:
            return a.split('\n')
        else:
            return [a]
    else:
        print '>>> ERROR, str2List fails::: ',a

    
def BuildError(msg="Some error msg. I don't know about that.",e=None,help=None):
  #Log(e)
  return {'status':'error','msg':msg,'sys_msg':str(e),'help':help}
def BuildInfo(msg,res):
  return {'status':'info','msg':msg,'res':_norm(res)}

def BuildSuccess(msg,res):    
  return {'status':'success','msg':msg,'res':_norm(res)}
  
def CustomHttpResponse(res,content_type='application/json'):
  return HttpResponse(decodeUnicodeDirectory(res), content_type = content_type)

