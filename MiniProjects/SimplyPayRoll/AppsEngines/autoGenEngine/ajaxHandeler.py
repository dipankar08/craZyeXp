import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .api import StudentManager
@csrf_exempt
def ajax_Student(request,id=None):
  res=None
  
  #If the request is coming for get ..
  if request.method == 'GET':
    page=request.GET.get('page',None)
    limit=request.GET.get('limit',None)
    name=request.GET.get('name',None);roll=request.GET.get('roll',None);
    # if Id is null, get the perticular Student or it's a search request
    if id is not None: 
      res= StudentManager.getStudent(id)
    else:
      # General Search request 
      id=request.GET.get('id',None) # We also support search based on ID.
      res= StudentManager.searchStudent(name=name,roll=roll,id=id,page=page,limit=limit,  )
    
  #This is the implementation for POST request.
  elif request.method == 'POST':
    name=request.POST.get('name',None);roll=request.POST.get('roll',None);
    # Update request if id is not null. 
    if id is not None: 
      res=StudentManager.updateStudent(id=id,name=name,roll=roll,)
    else:
      # This is new entry request...
      res=StudentManager.createStudent(name=name,roll=roll,)
    
  # This is a Delete Request..
  elif request.method ==  'DELETE' and id is not None:
    res =StudentManager.deleteStudent(id)
  #Return the result after converting into json 
  return HttpResponse(json.dumps(res,default=json_util.default),mimetype = 'application/json')
