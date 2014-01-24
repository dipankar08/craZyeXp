import sleekxmpp
from ConfigParser import ConfigParser
################################ Perser from Raw XML #######
from lxml import etree
def ParseMsg(xml):
  print xml
  treetop = etree.fromstring(anxmlstring)
  return treetop
def parseRoster(xml):
  print xml
  treetop = etree.fromstring(anxmlstring)
  return treetop
def parsePresence(xml):
  print xml
  treetop = etree.fromstring(anxmlstring)
  return treetop



################ Main Class are here ###############
class StatusWatcher(sleekxmpp.ClientXMPP):
    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")
        jid = config.get("gmail", "jid")
        resource = config.get("gmail", "resource")
        password = config.get("gmail", "password")
        sleekxmpp.ClientXMPP.__init__(self, jid + "/" + resource, password)

        self.add_event_handler("session_start", self.handle_XMPP_connected)
        self.add_event_handler("changed_status", self.handle_changed_status)
        self.add_event_handler('message', self.recv_message)

    def handle_XMPP_connected(self, event):
        print '!!!! Connected'
        self.sendPresence(pstatus="I'm just a Bot.")
        roster = self.get_roster()
        roster = parseRoster(roster)
        print roster

    def handle_changed_status(self, pres):
        print '!!!! Status Changes'
        pres = parsePresence(str(pres))
        print pres        
        print pres['status']
            
    def recv_message(self, msg):
        print '!!!! Message Received'        
        msg  = ParseMsg(msg)
        print msg
        # You'll probably want to ignore error and headline messages.
        # If you want to handle group chat messages, add 'groupchat' to the list.
        if msg['type'] in ('chat', 'normal'):
            print "%s says: %s" % (msg['from'], msg['body'])
            msg.reply('Thanks').send()


xmpp = StatusWatcher() # The account to monitor
print xmpp.roster
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0199')
if xmpp.connect():
    xmpp.process(threaded=False)