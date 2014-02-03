#########################
## Name : FaceBook Module Integration
##
#########################
import sleekxmpp
import logging
logging.basicConfig(level=logging.DEBUG)

##### Handaler ############



########## End of Handaler#################


def read_message(msg):
    if msg['type'] in ('chat','normal'):
        print msg
        print('msg received')
        print(msg['body'])
        msg.reply('Thanks').send()

######### Main API Class  #################

class Facebook(sleekxmpp.ClientXMPP):
    def __init__(self,uid,pwd):
        jid = uid+'@chat.facebook.com'
        server = ('chat.facebook.com', 5222)
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler('session_start', self.session_start)
        self.add_event_handler('message', read_message)
        self.auto_reconnect = True
        #self.connect(server)
        #self.conn = chatbot
        #self.process(block=True)
    def session_start(self,event):
        self.send_presence()
        print('Session started')        
        self.roster = self.get_roster()
        print self.roster
        print self.roster.get_items()
        print self.conn.client_roster.keys()
        
    def getContactList(self):
        return self.roster.get_items()
    def send_msg(self,to,msg):
        self.send_message(mto=to,mbody=msg,mtype='chat')
    def change_status(self,status):
        pass
    def logout(self):
        # Using wait=True ensures that the send queue will be
        # emptied before ending the session.
        self.disconnect(wait=True)



##################  Main Program #########
uid = 'HIDDEN'
password = 'HIDDEN'
f = Facebook(uid,password)
print f.getContactList()

