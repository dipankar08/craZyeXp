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
from CommonLib.utils import getRandom
from CommonLib.Logs import Log
#################################################
# C O M M O  N  H E L P E R   F U N C T I O N
#################################################
def getAutoRandom10():
    return getRandom(10)# ^ digit random number

            




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
  Log(e)
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
       # Step 2: Apply Constrictions
       #pdb.set_trace()
       for table_name, fig in CONFIG.items():
           table = self.db[table_name]
           #check contrains
           if fig.has_key('contrains'):
               contrains = fig['contrains']
               for x,y in contrains:
                  if y == 'unique':
                      print '>>> Applying contstins to table....'
                      table.ensure_index((x),unique=True,sparse=True)
                  else:
                      print '>>> Invalid Contratins :',y                    
       
    except Exception ,e:
       return BuildError('not able connect database',e)
    
  def _getById(self, coll,id): # Only used in update
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
    try:
        collection = self.db[coll]
        res ={}
        if id:
          res = collection.find_one({'_id': ObjectId(id)})
          if res: #asking for spacific entry
             #This ans might to be explored for inner table ref.
             res  = self._BuildEntryForOutput(coll,_norm(res))
             return BuildSuccess('return data',res)
          else:
             return BuildSuccess('No entry found :(',res)
        else: # search by some entry..
            r = [x for x in collection.find(entry)] # iterator to list
            if r:
                if ( len(r) > 1) : 
                    res = {'data':r,'count':len(r)}
                else:
                    res = r[0]
                return BuildSuccess('returning serach data by: '+str(entry),_norm(res))
            else:
                return BuildInfo('No Item found',res)
    except Exception,e:
           return BuildError('not able to retrive data',e)

  def _VerifyEntryFailed(self, coll,entry): # Verify an Entry for null check and return true if failed.
        if not CONFIG.has_key(coll): return None
        conf = CONFIG[coll]
        #pdb.set_trace()
        if conf.get('notnull'):
            for x in conf.get('notnull'):
                if (not entry.has_key(x) or not entry.get(x)):
                    return x +' field should not have null value'
        return None; # return None as no Error
        
  # Build an entry for adding into storage as some data might be generated.
  def _BuildEntryForInput(self, coll,entry):
        conf = CONFIG[coll]
        if conf.get('getAutoRandom6'):
            for x in conf.get('getAutoRandom6'):
                entry[x] = getAutoRandom10();
        return entry;
        
  # Build an entry for returning as some internal table might need to explore.
  def _BuildEntryForOutput(self, coll,entry):
        conf = CONFIG[coll]
        if conf.get('explore'):
            for ref in conf.get('explore'):
                ref_act = ref.replace('table_','')
                if isinstance(entry[ref],list):                    
                    entry[ref_act]=[]
                    for id in entry[ref]:#['512d5793abb900bf3e20d012', '512d5793abb900bf3e20d011'];
                        res = self._getById(ref_act,id)
                        if res['status'] == 'success':
                            entry[ref_act].append(_norm(res['res']))
                        else:
                            print '>>>ERROR: Not able to constarct inner table< %s of id %s>. ' %(ref_act,id)
                elif isinstance(entry[ref],basestring):
                    id = entry[ref]
                    res = self._getById(ref_act,id)
                    if res['status'] == 'success':
                        entry[ref_act]=(_norm(res['res']))
                    else:
                        print '>>>ERROR: Not able to constarct inner table < %s of id %s >' %(ref_act,id)                    
        return entry; 
        
  def _add(self, coll,entry):
    #pdb.set_trace()    
    try:
        res = self._VerifyEntryFailed(coll,entry);
        if res:
            return BuildError(res,None)
        entry = self._BuildEntryForInput(coll,entry);
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
    

    print '\n>>> testing Constains ...'; print '-'*50
    k.db.test.remove({'name':'dipankar'})  # Cleanup for test
    x =  k._add('test',{'name':'dipankar','email':'dutta.dipankar08@gmail.com'});print x; x = x['res']['_id']  
    print k._add('test',{'name':'dipankar','email':'dutta.dipankar08@gmail.com'})
    print k._update('test','55f705181a757e11127da3d4',{'name':'dipankar'}) # updating other data to same name
    print k._delete('test',x)
    print k._add('test',{'name':'dipankar','email':'dutta.dipankar08@gmail.com'})
    print '-'*50
    #pdb.set_trace()
    print k._add('test1',{'name':'dipankar','table_test':'55f705181a757e11127da3d4'})
    print k._get('test1','563baaa01a757e135a219d63')
    
  
  
#test()
       
       