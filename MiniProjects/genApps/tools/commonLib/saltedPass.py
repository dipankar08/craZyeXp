##############################################
# Salted password.
# Autor: dipankar
##############################################
import os
import hashlib
import binascii
class SaltedPass:

  @staticmethod
  def getSaltPasswd(passwd):
    salt = os.urandom(24)
    salt = binascii.hexlify(salt)
    passwd = str(salt)+str(passwd)
    passwd = hashlib.sha224(passwd).hexdigest()
    return (passwd,salt)


  @staticmethod
  def checkPasswd(i_pass, s_pass,salt):
    return hashlib.sha224(salt+i_pass).hexdigest() == s_pass 



#sample test
(p,s) = SaltedPass.getSaltPasswd('dipankar123')
print (p,s)
print SaltedPass.checkPasswd('dipankar123',p,s)
print SaltedPass.checkPasswd('dipankar123',p,'wrong')
print SaltedPass.checkPasswd('wrrong',p,s)
