import requests
import pdb
import json
def processResp(resp):
    res ={}
    pdb.set_trace()
    res['status_code']=resp.status_code
    if resp.status_code == 200:
        res['msg']='Looks good.'
        res['status']='success'
        res['res'] = json.loads(resp.text)
    elif resp.status_code == 400:
        res['msg']='Some error 400'
        res['status']='info'
        res['res'] = json.loads(resp.text)
    else:
        res['msg']='Some Unknown Error'
        res['status']='error'
        res['res'] = json.loads(resp.text)
    return res

class paymentUtils:
    def __init__(self,key,secret):
        self.auth = (key, secret)

    def getAllPayment(self):
        url = 'https://api.razorpay.com/v1/payments?from=1400826740&count=2&skip=1'
        resp = requests.get(url, data={}, auth=self.auth)
        #pdb.set_trace()
        return processResp(resp)
        
    def getPaymentByID(self,id):
        url = 'https://api.razorpay.com/v1/payments/'+str(id)
        resp = requests.get(url, data={}, auth=self.auth)
        return processResp(resp)
        
    def capture(self,id,amount):
        url = 'https://api.razorpay.com/v1/payments/'+str(id)+'/capture'
        resp = requests.post(url, data={'amount':amount}, auth = self.auth)
        return processResp(resp)
        
def test():
    p = paymentUtils('rzp_test_gpro0A29e7QWEo','Kfr8fyd3cA9osWWV0jQHGv0R')
    print p.getAllPayment()
    print p.getPaymentByID('pay_40qrxgYC6Jm4tr')
    print p.capture('pay_40qrxgYC6Jm4tr',100)

test()