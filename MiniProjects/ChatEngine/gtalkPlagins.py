########################################3
# Gtalk Plagins  in pythin
#i#########
import xmpp

# Hanalder function here
def myPresenceHandler(con, event):
  #if event.getType() == 'unavailable':
  print str(event.getFrom().getStripped()) +'is now '+ str(event.getType())

class Gtalk:
  def __init__(self,loginid,passwd,domain = 'gmail.com'):
    self.cnx =None
    cnx = xmpp.Client(domain,debug=[])
    if cnx.connect( server=('talk.google.com',5223) ) =="":
      print 'Not able to connect'
      return None
    if cnx.auth(loginid,passwd, 'botty') ==None:
      print "Auth Failed"
      return None
    cnx.sendInitPresence()
    self.cnx = cnx
    print 'Logied in'
    self.cnx.RegisterHandler('message', self.messageCB)
    self.cnx.RegisterHandler('presence', myPresenceHandler)
    
  def getConn(self):
    return self.cnx
  
  def update_status(self,msg):
    pres = xmpp.Presence(typ='unavailable',show='unavailable',status='unavailable')
    pres.setStatus(msg)
    self.cnx.send(pres)
    
  def send_msg(self,to ="dutta.dipankar08@gmail.com",msg="Hello World form Python"):
    msg = xmpp.Message( to ,msg )
    msg.setAttr('type', 'chat')
    self.cnx.send(msg)
  def log_out(self):
    self.cnx.disconnect()
    print 'logout succ'
    

  def messageCB(self,conn,msg):
    print "Sender: " + str(msg.getFrom())
    print "Content: " + str(msg.getBody())
    print msg
  
####Main function ###

def StepOn(conn):
  try:
    conn.Process(1)
  except KeyboardInterrupt:
    return 0
  return 1
    
def GoOn(conn):
  while StepOn(conn):
    pass
  
loginid = 'pequenas.mail' # @gmail.com
pwd   = 'pequenas123'
clx = Gtalk(loginid,pwd)
clx.send_msg()
clx.update_status('Test')
GoOn(clx.getConn())

#log_out(clx)