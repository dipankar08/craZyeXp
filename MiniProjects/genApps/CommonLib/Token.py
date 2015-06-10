#################################################
#        T O K E N 
#################################################
MIXTURE = "DIPANKAR"
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
  val =''
  flag = 0
  val += MIXTURE
  val += VERSION
  
  if ip:
   flag = flag + (1 << FLAG_IP )
   val += str(ip)
  if dataId:
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
def verifyToken(token,ip=None,dataId=None,license=None):
  pdb.set_trace()
  res = decode(KEY,token)
  flag = res[:res.find('###')]
  res = res.replace(flag+'###','')
  flag = int(flag)

  if not res.startswith(MIXTURE):
    return (False,'TOKEN ERROR: MIXTURE MISMATCH')
  res = res.replace(MIXTURE,'')

  if not res.startswith(VERSION):
    return (False,'TOKEN ERROR: VESRION MISMATCH')
  res = res.replace(VERSION,'')
  
  if get_bit(flag,FLAG_IP):
    if not res.startswith(ip):
      return (False,'TOKEN ERROR: IP MISMATCH')
    res = res.replace(ip,'')

  if get_bit(flag,FLAG_ID): 
    if not res.startswith(dataId):
      return (False,'TOKEN ERROR: ID MISMATCH')
    res = res.replace(dataId,'')

  if get_bit(flag,FLAG_DATE):
    date = datetime.strptime(res[:10], '%m/%d/%Y')
    if date.date() > datetime.today().date():
      return (False,'TOKEN ERROR: DATE MISMATCH') 
    res = res.replace(date,'')

  if get_bit(flag,FLAG_TIME):
    time =''
    if not res.startswith(time):
      return (False,'TOKEN ERROR: TIME MISMATCH')
    res = res.replace(time,'')

  if get_bit(flag,FLAG_LIC):
    if not res.startswith(license):
      return (False,'TOKEN ERROR: LIC MISMATCH')
    res = res.replace(license,'')

  if res == '':
    return (True,'Success!')
  return (False,'TOKEN ERROR: Unknown/ InvalidToken')

  



