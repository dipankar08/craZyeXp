############################################
#
# A Proxy to access Github v3 API.
# @author: Dipankar Dutta
# @Date: 10/28/2015
############################################
import requests
import base64
import pdb
import json

import hashlib

class GitHub:
    def __init__(self,repo="dipankar08/craZyeXp",uname=None,passwd=None):
        self._repo = repo ; # it shpuld be looks like "dipankar08/craZyeXp
        self._base_url = "https://api.github.com/repos/"+self._repo+"/contents"
        self._auth = (uname, passwd)


    def listFiles(self):
        pass
        
    def getFile(self,path="/README.md"):
        """ You sould give the path as /abc/pqr.txt """
        pdb.set_trace()
        res={'status':"error",'res':'file data','msg':'file contined returned'}
        try:
            r = requests.get(self._base_url+path)
            data = r.json()
            if isinstance(data, dict) and data["type"] == "file":
                data  = base64.b64decode(data['content'])
                res['res'] = data
                res['status'] = 'success'
            else:
                res['msg'] = 'The path is not a file'
        except Exception, e:
            res['msg'] = 'Some error occures: '+ str(e)
        return res
        
    def saveFile(self,path="/test.txt",data="",cname="PeerReviewBot",cemail="p@p.com",cmsg="Auto commit message"):
        """ You sould give the path as /abc/pqr.txt """
        pdb.set_trace()
        res= {'status':"error",'res':'file data','msg':'some error occures'}
        try:
            url = self._base_url+path
            data = base64.b64encode(data)
            payload = {"path": path, "message": cmsg, "committer": {"name": cname, "email": cemail}, "content": data, "branch": "master"}
            # See if esit or not!
            r1 = requests.get(url)
            if r1.status_code == 200: #already exist
                payload['sha'] = r1.json()['sha']
            else:
                print ' We are creating new file..'
            r = requests.put(url, data= json.dumps(payload),auth=self._auth)
            if r.status_code == 201 :
                res['msg'] = 'Code Succufully commited!(Created)'
                res['status'] = 'success'
                return res
            elif r.status_code == 200 :
                res['msg'] = 'Code Succufully commited!(Updated)'
                res['status'] = 'success'
                return res
            else:
                res['msg'] = 'Not able to sumit your code'
                res['status'] = 'error'
                res['res'] = r.json()
        except Exception, e:
            res['msg'] = 'Some error occures: '+ str(e)
        return res
    def listFiles(self):
        pass

def UnitTest():
    g = GitHub(uname="dipankar08",passwd="DD08@iitr")
    #print g.getFile('/')
    print g.saveFile(data="I love dipankar")
    
    
UnitTest()