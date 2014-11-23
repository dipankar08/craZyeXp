# -*- coding: utf-8 -*-
#####################################
#  E2B-FontConverter
#  # using generator...
######################################
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from doParallel1 import speedUp
from log import D_LOG
from flask import *
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

##########################################
import requests
import pickle
import pdb


def recur_set1(counts=3,lst='abc'):
  LIST = list(lst)
  all = LIST
  now = LIST
  import pdb
  
  for i in range(2,counts+1):
    print 'Calculating of length',i,'...'
    so = [ j+k for j in now for k in list(lst)]
    all += so
    now = so
    print 'Count of length(%s): %s' %(i,len(so))
  print len(all)
  #pdb.set_trace()
  return all

def recur_set(counts=3,lst='abc'):
  """ This is a Generator : Hence no mem Error 
  print gen.next() ==> {'key': 'aaaaaaaaaa'} and doesnt allow 3 consicutive same chracter ..:)
  """
  # this is a second version which Generate only counts Length String from lst desnt have consicutive 3 same occurances...
  LIST = list(lst)
  code ='('
  code+= '{"key":'
  for i in range(1,counts):
    code+='_x'+str(i)+' + '
  code+='_x'+str(counts)
  code+= '} '
  for i in range(1,counts+1):
    code+=' for ' '_x'+str(i)+' in list("'+lst+'") '
  if counts >=3: #ignore <aaa cases>
    code+= ' if not('
    code+='(_x1 == _x2 == _x3)'
    for i in range(2,counts-1):
      code+='or (_x'+str(i)+' == _x'+str(i+1)+' == _x'+str(i+2)+')'
    code+=')'
  code+=')'
  print 'Run Time Expression is :',code
  alllist = eval(code)
  return alllist
#recur_set(counts=10,lst='abcdefghijklmnopqrstuvwxyz')

######### Generator for length 1 to 10 with no consicutive 3 same letter...#####
def getGen():
  " We have list of generator.. We have meta genaration on top of this..."
  gen_list=[ recur_set(i,'abcdefghijklmnopqrstuvwxyz') for i in range(1,11)]
  for g in gen_list:
    for gg in g:
       yield gg




######### Global cache Setup[radis] setup #####################
def load_cache():
  print 'loading cache...'
  #cache = pickle.load ( open( "a-TO-z-LEN2.pkl", "rb" ))
  cache = redis.StrictRedis(host='localhost', port=6379, db=0)
  return cache

import pickle
import redis
cache = load_cache()
print cache

global session 
import requests
session = requests.Session()
a = requests.adapters.HTTPAdapter(max_retries=3)
b = requests.adapters.HTTPAdapter(max_retries=3)
session.mount('http://', a)
session.mount('https://', b)

################################################################


def doCall(key,tried = 0):
  global cache
  global session
  print "[doCall] for key",key
  try:
    r = session.get("http://www.google.com/inputtools/request?text="+key+"&ime=transliteration_en_bn&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi")
    r = r.text
    r = r.replace('true','True')
    r = r.replace('false','False')
    y = eval(r)
    cache.set(key,y[1][0][1]) #redis call
  except requests.exceptions:
    time.sleep(120)
    if tried < 2: 
       doCall(key,tried+1)
    else:
      print 'IGNORING KEYYYYYYYYYYYY :',key
  return None
  
  
  

def grab_and_build_cache(trie_len=10):
  "Build an Cache and use this service for Offline "
  Map= {}
  COUNT = 5
  #2. Make Generator ..
  #gen = recur_set(COUNT,lst='abcdefghijklmnopqrstuvwxyz')
  gen = getGen()
  #pdb.set_trace()
  #3. Fire Up the Operation.
  speedUp(doCall,gen,15);
  


#############  Web server Operation here #######################
import flask
from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@crossdomain(origin='*') # <<< This for cross domain support 
def converts():
  try:
    if request.method == 'GET':
      #pdb.set_trace()
      q = request.args.get('q', '')
      if not q: return "Use /?q=abc "      
      #cache = load_cache()
      ll = cache.get(q)
      if ll: ll = eval(ll)
      
  except:
      D_LOG()
  f = {'status': 'success','input': q ,'output': ll}
  return flask.jsonify(**f)

@app.route('/<path:filename>')
def send_foo(filename):
    return send_from_directory('.', filename)

############ End of server #######################################
    
# tesing ..
xx = raw_input("Press c for recache?")
if xx == 'c':
  grab_and_build_cache()
else:
  #server
  app.run(host='0.0.0.0')
