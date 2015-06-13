#################################################
#        T O K E N 
#################################################
MIXTURE = "DIPANKAR"
INGSTR = "nokey"
VERSION = "1.0"
KEY     = "TTY"
FLAG_IP  = 0
FLAG_ID  = 1
FLAG_SALT = 2
FLAG_DATE = 3
FLAG_TIME = 4
FLAG_LIC  = 5

##########  Helper ####################
def get_bit(byteval,idx):
    return ((byteval&(1<<idx))!=0);
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def genToken_ONETIME():
  pass
def verifyToken_ONETIME():
  pass

def genToken(ip=None,dataId=None,endDate=None,endTime=None,license=None):
  print """
##################### F O R M E T ###############################
  ip='10.10.10.10',dataId=100,endDate="06/11/2015",endTime='16:00',license="dipankar")
#################################################################
  """
  val =''
  flag = 0
  val += MIXTURE
  val += VERSION
  
  if ip:
   flag = flag + (1 << FLAG_IP )
   val += str(ip)
  if dataId:
   dataId = str(dataId)
   flag = flag + (1 << FLAG_ID )
   val += str(dataId)
  if endDate:
   flag = flag + (1 << FLAG_DATE )
   val += str(endDate)
  
  if endTime:
   flag = flag + (1 << FLAG_TIME )
   val += str(endTime)
  if license:
   flag = flag + (1 << FLAG_LIC )
   val += str(license)
  
  res = str(flag)+'###'+val
  return encode(KEY,res)
import pdb
from datetime import datetime
def verifyToken(token,ip=None,dataId=None,license=None):
  try:
    if token == INGSTR:
      return (True, "ignore licence check")
    #pdb.set_trace() 
    res = decode(KEY,token)
    flag = res[:res.find('###')]
    res = res.replace(flag+'###','')
    flag = int(flag)

    if not res.startswith(MIXTURE):
      return (False,'Invalid MIXTURE')
    res = res.replace(MIXTURE,'')

    if not res.startswith(VERSION):
      return (False,'Invalid VESRION')
    res = res.replace(VERSION,'')
    
    if get_bit(flag,FLAG_IP):
      if not res.startswith(ip):
        return (False,'Access restricted to :'+ip)
      res = res.replace(ip,'')

    if get_bit(flag,FLAG_ID): 
      dataId = str(dataId)
      if not res.startswith(dataId):
        return (False,'Acess restricted to :'+dataId)
      res = res.replace(dataId,'')

    if get_bit(flag,FLAG_DATE):
      dstr = res[:10]
      date = datetime.strptime(dstr, '%d/%m/%Y')
      if date.date() < datetime.today().date():
        return (False,'Date Expaired Due Date:'+dstr) 
      res = res.replace(dstr,'')

    if get_bit(flag,FLAG_TIME):
      tstr =res[:5]
      date = datetime.strptime(tstr, '%H:%M')
      if date.time() < datetime.today().time():
        return (False,'Time Expaired! Due Time:'+tstr)
      res = res.replace(tstr,'')

    if get_bit(flag,FLAG_LIC):
      if not res.startswith(license):
        return (False,'Invalid User/Access To : ',license)
      res = res.replace(license,'')

    if res == '':
      return (True,'Success!')
    return (False,'Corrupt Licence!')
  except Exception, e:
    print '+++++++++++++> ERORR',str(e)
    return (False,'Internal Error while processing License!')

  


def test():
  
  ip='10.10.10.10'
  dataId=100
  endDate="06/11/2015"
  endTime='15:11'
  license="dipankar"

  t = genToken(ip=ip,dataId=dataId,endDate=endDate,endTime=endTime,license=license)
  print '\n######################\nLinces:',t,'\n##################################\n'
  print '\n#############################\nCross Check: ', verifyToken(t,ip=ip,dataId=dataId,license=license),'\n##################################\n'



#test()
