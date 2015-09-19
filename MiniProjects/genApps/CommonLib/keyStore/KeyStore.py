#####################################################
# File: KeyStore.py 
# Target: To Provide API to CRUD Operation on NoSQL
# Install:(32 Bit Version ) TODO: 64 Bit MUST as It is very memory complex
# > sudo mongod --config /etc/mongodb.conf
# > pip install pymongo
# Architecture:
# client --> db-->collection->document: collection==table; document == row
######################################################
import pymongo
import pdb
#from CommonLib.Logs import Log
from bson.objectid import ObjectId
DEFAULT_DB_NAME = 'default_database'
DEFAULT_COLLECTION_NAME = 'default_collection'

# Utility
def _norm(res):
    # null res
    if not res: return res
    #res is a dict
    if res.has_key('_id'):
      res['_id'] = str(res['_id'])

    #res has a list of dict
    if res.has_key('data') and isinstance(res['data'],list):
      for x in range(len(res['data'])):
        if res['data'][x].has_key('_id'):
           res['data'][x]['_id'] = str(res['data'][x]['_id'] )


      
    return res
def BuildError(msg,e):
  #Log(e)
  return {'status':'error','msg':msg,'sys_msg':str(e)}
def BuildInfo(msg,res):
  return {'status':'info','msg':msg,'res':_norm(res)}

def BuildSuccess(msg,res):    
  return {'status':'success','msg':msg,'res':_norm(res)}
  
  
class KeyStore:
  def _getDB(name):
    pass
    
  ######### Initilization of Database -- Should called at setting ####
  def init(self, db_name=None):
    self.client = None;
    self.db =None;
    try:
       from pymongo import MongoClient
       self.client = MongoClient()
       if db_name == None:
           db_name = DEFAULT_DB_NAME
       self.db = self.client[db_name]
    except Exception ,e:
       return BuildError('not able connect database',e)
    
  def _getById(self, coll,id):
    collection = self.db[coll]
    res = collection.find_one({'_id': ObjectId(id)})
    if res:
       return BuildSuccess('return data',res)
    else:
       return BuildSuccess('No entry found :(',res)
       

    
    
  def _get(self,coll,id=None,limit=None,page=None): # getting a collection..
    collection = self.db[coll]
    if id:
      res = collection.find_one({'_id': ObjectId(id)})
      if res:
         return BuildSuccess('return data',res)
      else:
         return BuildSuccess('No entry found :(',res)
    else:
        res ={}
        res['data'] =  [x for x in collection.find()]
        res['count']= collection.count()
        return BuildSuccess('return all data',res)
     
     
  def _add(self, coll,entry):
    collection = self.db[coll]
    _id = collection.insert(entry)
    res = collection.find_one({'_id': _id})
    res['_id']= str(_id)#System id
    return BuildSuccess('Item cretated',res)
    pass
      
      
  def _update(self, coll,id,entry):
    collection = self.db[coll]
    res = self._getById(coll,id)
    if res['res'] == None:
      return res
    else:
      data = res
      for k,v in entry.items():
        data[k] = v
      collection.update({'_id':ObjectId(id)}, {"$set": data}, upsert=False)
      return BuildSuccess('updated data',collection.find_one({'_id': ObjectId(id)}))
    pass
    
  def _delete(self, coll,id):
    collection = self.db[coll]
    x =  BuildSuccess('Deleted data',collection.find_one({'_id': ObjectId(id)}))
    collection.remove( {'_id': ObjectId(id)})
    return x
    pass
  
  
  #Exposed API
  def creteOrUpdate(self,coll,id,entry):
    
    if not id:
       return self._add(coll,entry)
    else:
       return self._update(coll,id,entry)
  def getOrSearch(self,coll,id,entry):
    #pdb.set_trace() 
    if not entry: # get one or more
       return  self._get(coll,id)
    else:
       return BuildSuccess('Serach is not yet Implemented data',None)

  def deleteEntryOrTable(self,coll,id,data):
    if not id:
       return BuildInfo('Table Delete Not supported',None)
    else:
       return self._delete( coll,id)
    
###############################
#
#  
#
###############################
def test():
  k = KeyStore()
  k.init()
  #print k._add('student',{'name':'dd'})
  #print k._get('student')  
  #print k._update('student','55f704d21a757e110371ceba',{'roll':'dd'})
  print k._get('student');print ''
  print k._delete('student','55f7050b1a757e110d56fc90');print ''
  print k._get('student','55f7054f1a757e111b098e48');print ''
test()
       
       