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
from pymongo.errors import DuplicateKeyError
DEFAULT_DB_NAME = 'default_database'
DEFAULT_COLLECTION_NAME = 'default_collection'

from CommonLib.keyStore.config import CONFIG

# getTargetResByAttr
# attr should be loosk like name/1/target/..../
def getTargetResByAttr(res,attr):
    attrs = attr.split('/')
    #pdb.set_trace()
    for a in attrs:
        if isinstance(res,dict):
            if a in res:
                res = res[a]
                continue;
            else:
                return (False, BuildError('No matched attribute found as '+attr))
        elif isinstance(res,list):
            if not a.isdigit():
                return (False, BuildError('We have a list and  '+a+' Must be a integer in the attribure'))
            if len(res)-1 < int(a):
                return (False, BuildError('We have a list and  '+a+' Must be a less the the size of list'))
            res = res[int(a)]
            continue;
        else:
            return (False, BuildError('Looks like the path <'+attr+'> Doent exst in your data source'))
    return (True, res)

def modifyTargetResByAttr(res,attr,newvalue=None,action="ADD"): #Action = ADD | REMOVE 
    if action not in ['ADD','REMOVE']:
        return (False, BuildError('action can be either ADD or REMOVE see your api '))
    if not newvalue and  action is 'ADD':
        return (False, BuildError('action ADD must have nevalue as dict'))
    attrs = attr.split('/')
    #pdb.set_trace()
    root = res
    pres = res;
    for a in attrs:
        if isinstance(res,dict):
            if a in res:
                pres = res; res = res[a]
                continue;
            else:
                #return (False, BuildError('No matched attribute found as '+attr))
                pres[a] = [ newvalue ]
                print '>>> INFO : New List attribute got cretaed. '+attr  
                return (True, root)
        elif isinstance(res,list):
            if not a.isdigit():
                return (False, BuildError('We have a list and  '+a+' Must be a integer in the attribure'))
            if len(res)-1 < int(a):
                return (False, BuildError('We have a list and  '+a+' Must be a less the the size of list'))
            pres=res; res = res[int(a)]
            continue;
        else:
            return (False, BuildError('Looks like the path <'+attr+'> Doent exst in your data source'))
    # Now we the path items
    if action  == 'ADD':
        if isinstance(res,dict):
            res = res.update(newvalue)
        elif isinstance(res,list):
            res.append(newvalue)
    elif action  == 'REMOVE':
        if isinstance(pres,dict):
            del pres[attrs[-1]]
        elif isinstance(pres,list):
            pres[int(attrs[-1])] = None # DONT DLETE LIST ITEMA AS IT PRSERVER INDEX ORDERUING>         
    return (True, root)
     



# Utility
def _norm(res):
    # null res
    if not res: return res
    if not isinstance(res,dict): return res
    #res is a dict
    if res.has_key('_id'):
      res['_id'] = str(res['_id'])

    #res has a list of dict
    if res.has_key('data') and isinstance(res['data'],list):
      for x in range(len(res['data'])):
        if res['data'][x].has_key('_id'):
           res['data'][x]['_id'] = str(res['data'][x]['_id'] )

    return res
# We dont use from utils.
def BuildError(msg,e=None,help="Some unknown error! Please contact the developer to fix it"):
  #Log(e)
  return {'status':'error','msg':msg,'sys_msg':str(e),'help':help,'res':None}
def BuildInfo(msg,res):
  return {'status':'info','msg':msg,'res':_norm(res)}

def BuildSuccess(msg,res):    
  return {'status':'success','msg':msg,'res':_norm(res)}
  
  
class KeyStore:
  def _getDB(name):
    pass
    
  ######### Initilization of Database -- Should called  at setting  this is one time operation####
  def init(self, db_name=None):
    self.client = None;
    self.db =None;
    try:
       # Step 1: init client ...
       from pymongo import MongoClient
       self.client = MongoClient()
       if db_name == None:
           db_name = DEFAULT_DB_NAME
       self.db = self.client[db_name]
       # Step 2: Apply Constractins
       #pdb.set_trace()
       for table_name, fig in CONFIG.items():
           table = self.db[table_name]
           contrains = fig['contrains']
           for x,y in contrains:
              if y == 'unique':
                  print '>>> Applying contstins to table....'
                  table.ensure_index((x),unique=True,sparse=True)
              else:
                  print '>>> Invalid Contratins :',y                    
       
    except Exception ,e:
       return BuildError('not able connect database',e)
    
  def _getById(self, coll,id):
    collection = self.db[coll]
    try:
        res = collection.find_one({'_id': ObjectId(id)})
        if res:
           return BuildSuccess('return data',res)
        else:
           return BuildInfo('No entry found :(',res)
    except Exception,e:
           return BuildError('No entry found with id:'+str(id),e,"Make sure that you have valid id")
  def _getIdByEntry(self, coll,entry):
    collection = self.db[coll]
    try:
        res = collection.find_one(entry)
        if res:
           return BuildSuccess('return data',str(res['_id'])) 
        else:
           return BuildInfo('No entry found :(',res)
    except Exception,e:
           return BuildError('No entry found with id:'+str(entry),e,"Make sure that you have valid id")

  # GET OR SERACH 
  # We only Support string search But we have to do more.. 
  def _get(self,coll,id=None,entry=None, limit=None,page=None): # getting a collection..
    #pdb.set_trace()
    collection = self.db[coll]
    res ={}
    if id:
      res = collection.find_one({'_id': ObjectId(id)})
      if res:
         return BuildSuccess('return data',_norm(res))
      else:
         return BuildSuccess('No entry found :(',res)
    else:
        r = [x for x in collection.find(entry)] # iterator to list
        print r
        if r:
            if ( len(r) > 1) : 
                res = {'data':r,'count':len(r)}
            else:
                res = r[0]
            return BuildSuccess('returning serach data by: '+str(entry),_norm(res))
        else:
            return BuildInfo('No Item found',res)

  

  def _add(self, coll,entry):
    try:
        collection = self.db[coll]
        _id = collection.insert(entry)
        res = collection.find_one({'_id': _id})
        res['_id']= str(_id)#System id
        return BuildSuccess('Item cretated',res)
    except DuplicateKeyError ,e:
        return BuildError('Adding an item failed! ',e,'you are violating some unique constrains')
    except Exception,e:
        return BuildError('Adding an item failed! ',e)
      
      
  def _update(self, coll,id,entry,attr=None,action=None):
    try:
        collection = self.db[coll]
        res = self._getById(coll,id)
        if res['res'] == None:
            return res
        else:
            data = res['res']
            del data['_id'];# This need to be removed
            if attr:# Update inside a path.
                tt = modifyTargetResByAttr(data,attr,entry,action) # This will update "data" as we pass by ref
                if not tt[0]:
                    return tt[1] #fails
                else:
                    collection.update({'_id':ObjectId(id)}, {"$set": data}, upsert=False)
                    return BuildSuccess('updated data on path '+ attr,tt[1])
              
            else: #Norma Update                           
                for k,v in entry.items():
                    data[k] = v 
                collection.update({'_id':ObjectId(id)}, {"$set": data}, upsert=False)
                return BuildSuccess('updated data',collection.find_one({'_id': ObjectId(id)}))
    except DuplicateKeyError ,e:
        return BuildError('update an item failed! ',e,'you are violating some unique constrains')
    except Exception,e:
        return BuildError('update an item failed! ',e)
    
  def _delete(self,coll,id):
    collection = self.db[coll]
    x =  BuildSuccess('Deleted data',collection.find_one({'_id': ObjectId(id)}))
    collection.remove( {'_id': ObjectId(id)})
    return x
    pass
  
  
  #Exposed APIs
  def creteOrUpdate(self,path,entry):
    coll = path['table'];id = path['id'];attr = path['attr']
    #pdb.set_trace()
    if not id:
       return self._add(coll,entry)
    else:
       return self._update(coll,id,entry,attr,'ADD')
       
  def getOrSearch(self,path,entry):
    coll = path['table'];id = path['id'];attr = path['attr']
    #pdb.set_trace() 
    res = self._get(coll,id,entry)
    if attr and res['res']:
      data =  getTargetResByAttr(res['res'],attr)
      if data[0]:
        res['res'] = data[1]
      else:
        return data[1] # This is an Error message
    return res

  def deleteEntryOrTable(self,path,data):
    #pdb.set_trace()
    coll = path['table'];id = path['id'];attr = path['attr']
    if not id:
       return BuildInfo('Table Delete Not supported',None)
    if attr:
       return self._update(coll,id,None,attr,'REMOVE')
    else:
       return self._delete( coll,id)
    
###############################
#
#  
#
###############################
def test():
    print '*'*80;print 'KeyStore Test Cases .......';print '*'*80;
    k = KeyStore()
    k.init()
    #pdb.set_trace()

    print '>>> testing Constains ...'
    print '-'*50
    k.db.test.remove({'name':'dipankar'})  # Cleanup for test
    x =  k._add('test',{'name':'dipankar'});print x; x = x['res']['_id']  
    print k._add('test',{'name':'dipankar'})
    print k._update('test','55f705181a757e11127da3d4',{'name':'dipankar'}) # updating other data to same name
    print k._delete('test',x)
    print k._add('test',{'name':'dipankar'})
    print '-'*50
  
  
test()
       
       