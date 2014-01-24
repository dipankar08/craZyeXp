import sleekxmpp
from ConfigParser import ConfigParser
import pdb
################################ Perser from Raw XML #######
import xml.etree.ElementTree as ET

########### Helper Function############
def breakFrom(fullid):
  data={}
  if '@' in fullid:
     data['jid']= fullid[:fullid.index('@')]
     if '/' in fullid:
       data['domain'] = fullid[fullid.index('@')+1:fullid.index('/')]
       data['resource'] = fullid[fullid.index('/')+1:]
     else:
       data['domain'] = ''
       data['resource'] = ''    
  else:
    data['jid']  = fullid
    data['domain'] = ''
    data['resource'] = ''
  return data
  
def ParseMsg(xml):
  #pdb.set_trace()
  #pdb.set_trace()
  root = ET.fromstring(str(xml))
  data ={}
  data['from'] = root.attrib.get('from')
  if  data['from'] : data.update(breakFrom(data['from'] ))
  data['type'] = root.attrib.get('type')
  data['body'] = root.findtext('body')
  return data
  
def parseRoster(xml):
  #pdb.set_trace()
  root = ET.fromstring(str(xml))
  ilist =[]
  root = root.find('{jabber:iq:roster}query').findall('{jabber:iq:roster}item')
  for i in root:
    data = i.attrib
    data['from'] = data['jid']
    if data['from'] : data.update(breakFrom(data['from'] ))
    data['group']= i.findtext('group')
    ilist.append(data)
  return ilist

  
def parsePresence(xml):
  #pdb.set_trace()
  root = ET.fromstring(str(xml))
  data ={}
  data['from'] = root.attrib.get('from')
  if data['from'] : data.update(breakFrom(data['from'] ))
  data['priority'] = root.findtext('priority')
  data['show'] = root.findtext('show')
  data['photo'] = root.find('{vcard-temp:x:update}x').findtext('{vcard-temp:x:update}photo')
  return data



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
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0199')
if xmpp.connect():
    xmpp.process(threaded=False)