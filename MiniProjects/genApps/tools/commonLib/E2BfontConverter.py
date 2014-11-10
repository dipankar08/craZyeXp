# -*- coding: utf-8 -*-
#####################################
#  E2B-FontConverter
#
######################################
import requests
import pickle
import pdb


def recur_set(counts=3,lst=['a','b','c']):
  all = lst
  now = all
  for i in range(counts -1):
    so = [ j+k for j in now for k in lst]
    all += so
    now = so
  print all
  print len(all)
  return all
      
  
  
  

def grab_and_build_cache(trie_len=10):
  "Build an Cache and use this service for Offline "
  Map= {}
  COUNT = 3 
  #LIST = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
  LIST = [ 'a','b','c','d','e','f','g' ]
  print '>>> Calculating all keys '  
  AllKey=recur_set(COUNT,LIST)
  print AllKey  
  for key in AllKey:
      r = requests.get("http://www.google.com/inputtools/request?text="+key+"&ime=transliteration_en_bn&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi")
      r = r.text      
      r = r.replace('true','True')
      r = r.replace('false','False')
      print r
      y = eval(r)
      Map[key]= y
  print Map
  pickle.dump( Map, open( "a2z-len5.pkl", "wb" ))
    
  

def load_cache():
  cache = pickle.load ( open( "a2z-len5.pkl", "rb" ))
  return cache

############## We Server #################
import flask
from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def converts():
    if request.method == 'GET':
      #pdb.set_trace()
      q = request.args.get('q', '')
      if not q: return "Use /?q=abc "      
      cache = load_cache()
      ll = cache.get(q)
      f = {'status': ll[0],'input': ll[1][0][0] ,'output': ll[1][0][1]}
      return flask.jsonify(**f)
############ End of server ###########
    
# tesing ..
#grab_and_build_cache()

#server
app.run(host='0.0.0.0')
