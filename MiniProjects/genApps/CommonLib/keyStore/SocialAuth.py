###########################################################
#       This file provide the registaration and authenticaltion by Socail login 
############################################################
from genApps.settings import KEYSTORE
from CommonLib.utils import getRandom
table = 'user'
import pdb
def getReqInfo(request):
    if not request:
       return {}
    return { 'REMOTE_ADDR': request.META.get('REMOTE_ADDR'), 'HTTP_USER_AGENT': request.META.get('HTTP_USER_AGENT'),'SERVER_NAME': request.META.get('SERVER_NAME'),'HTTP_HOST': request.META.get('HTTP_HOST'),'REMOTE_ADDR': request.META.get('REMOTE_ADDR'), }
    
def update_history(id,msg,request):
    KEYSTORE.creteOrUpdate({'table':table, 'id': id, 'attr':'history' },{'msg':msg,'info':getReqInfo(request)})
    
    
class SocialAuth:
    @staticmethod
    def createOrAuthUserBySocial( data,request):
        #pdb.set_trace()
        email = data.get('email')
        a = KEYSTORE._getIdByEntry(table,{'email':email})
        path ={'table':table, 'id': a['res'], 'attr':None}
        entry={'email':email,'data':data}
        res = KEYSTORE.creteOrUpdate(path,entry)
        id = res['res']['_id']
        #pdb.set_trace()
        if res['status'] == 'success':
            if not a['res']: #Register
                update_history(id,'New user joined',request)
                #Send Mail
            else: # old user
                update_history(id,'user logged in happens',request)
            if res['res'].get('history'): del res['res']["history"]
            return res;
        else:
            return {"status": "error", "msg": "not able to sign up"};
           

    @staticmethod
    def createOrAuthUserByPassword(self, email,data,request):
        pass
    #################################  USER ACTIVATION #############################################
    "Send mail and create a passkey in backend"
    @staticmethod
    def sendMailToActivateUser(data,request):
        a = KEYSTORE.getOrSearch({'table':table, 'id':None, 'attr':None},{'email':data.get('email') })
        if not a['res'] : return {"status": "error", "msg": "email not registered!"};
        id = a['res']['_id']
        
        pass_key = getRandom(10)
        
        res = KEYSTORE.creteOrUpdate({'table':table, 'id': id, 'attr':None},{'pass_key':pass_key})
        if res['status'] == 'error':return {"status": "error", "msg": "pass_key not generted"};
        update_history(id,'send activation link',request)
        return res
        # Send Mail with pass key

    "GET THE PASS KEY AND set the activation "
    @staticmethod
    def activateUser(data,request):
        a = KEYSTORE.getOrSearch({'table':table, 'id':None, 'attr':None},{'email':data.get('email'),'pass_key':data.get('pass_key') })
        if not a['res'] : return {"status": "error", "msg": "pass Key Not valid."};
        id = a['res']['_id']
        
        res = KEYSTORE.creteOrUpdate({'table':table, 'id': id, 'attr':None},{'active':True})
        return {"status": "success", "msg": 'We have activate the user'};
        
    "GET THE PASS KEY AND set the activation "
    @staticmethod
    def isActive(data,request):
        a = KEYSTORE.getOrSearch({'table':table, 'id':None, 'attr':None},{'email':data.get('email') })
        if not a['res'] : return {"status": "error", "msg": "Email Not valid"};
        if a['res'].get('active'):
            return {"status": "success", "msg": 'active'};
        else:
            return {"status": "error", "msg": 'Not active'};
        
    #############################   CHANGE PASS WORD #################################################
    "Send mail and create a passkey in backend"
    @staticmethod
    def sendMailToChangePassword(self,email,data,request):
        pass

    "GET THE PASS KEY AND set the activation "
    @staticmethod
    def changePassWord(self,email,data,request):
        pass
        
    "Get Login History"
    @staticmethod
    def getAuthHistory(self,email,data,request):
        pass
        