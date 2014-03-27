import sleekxmpp
from ConfigParser import ConfigParser
import pdb
################################ Perser from Raw XML #######
import xml.etree.ElementTree as ET
import logging

from sleekxmpp.xmlstream import ET, ElementBase, register_stanza_plugin
from sleekxmpp.plugins.xep_0054.stanza import *

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
########### Helper Function############
FILE_TYPES = {
    'image/png': 'png',
    'image/gif': 'gif',
    'image/jpeg': 'jpg'
}

def breakFrom(fullid):
  data={}
  if '@' in fullid:
     data['jid']= fullid[:fullid.index('@')]
     if '/' in fullid:
       data['domain'] = fullid[fullid.index('@')+1:fullid.index('/')]
       data['resource'] = fullid[fullid.index('/')+1:]
     else:
       data['domain'] = fullid[fullid.index('@')+1:]
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
  if root.find('{vcard-temp:x:update}x'): data['photo'] = root.find('{vcard-temp:x:update}x').findtext('{vcard-temp:x:update}photo')
  return data



################ Main Class are here ###############
class StatusWatcher(sleekxmpp.ClientXMPP):
    def __init__(self,type):
        self.hashes = []
        config = ConfigParser()
        config.read("config.ini")
        if type == 'google':
          jid = config.get("gmail", "jid")
          resource = config.get("gmail", "resource")
          password = config.get("gmail", "password")
          print jid,password
        if type =='facebook':
          jid = config.get("facebook", "jid")
          resource = config.get("facebook", "resource")
          password = config.get("facebook", "password")
        sleekxmpp.ClientXMPP.__init__(self, jid + "/" + resource, password)
        self.auto_reconnect = True

        self.add_event_handler("session_start", self.handle_XMPP_connected)
        self.add_event_handler("changed_status", self.handle_changed_status)

        self.add_event_handler('message', self.recv_message)
        
        self.add_event_handler('gmail_notify', self.xmpp_gmail_notify)
        
        
        #Vcard
        self.add_event_handler('vcard_avatar_update', self.on_vcard_avatar)
        self.add_event_handler('avatar_metadata_publish', self.on_avatar)

    def xmpp_gmail_notify(self, event):
        """
        Connection Handaler
        """
        pdb.set_trace()
        print '!!!! Gmail Message come'
        print event
        
        
    def handle_XMPP_connected(self, event):
        """
        Connection Handaler
        """
        print '!!!! Connected'
        self.sendPresence(pstatus="I'm just a Bot.")
        roster = self.get_roster()
        roster = parseRoster(roster)
        #print roster


    def handle_changed_status(self, pres):
        """
        Status Change Handaler
        """
        pdb.set_trace()
        print '!!!! Status Changes'
        photo_hash = pres['vcard_temp_update']['photo']
        pres = parsePresence(str(pres))
        
        if not photo_hash in self.hashes:
            self.hashes.append(photo_hash) 
            iq = self.Iq()
            iq['vcard_temp']['want-extval'] = True
            iq.send(block=False, callback=self.request_vcard)
        #print pres 
    def request_vcard(self, stanza):
        pdb.set_trace()
        vcard_temp = stanza.get('vcard_temp')
        photo = vcard_temp['PHOTO']
 
        if not photo:
            return
        binval = photo.get('BINVAL', None)
        if binval:
            print 'BINVAL:', len(binval), 'bytes'        
            
    def recv_message(self, msg):
        """
        Message Received handaler
        """
        print '!!!! Message Received'        
        msg  = ParseMsg(msg)
        #print msg
        # You'll probably want to ignore error and headline messages.
        # If you want to handle group chat messages, add 'groupchat' to the list.
        if msg['type'] in ('chat', 'normal'):
            print "%s says: %s" % (msg['from'], msg['body'])
            msg.reply('Thanks').send()
    
    def on_vcard_avatar(self, pres):
        """
        Getting Profile Picture: Working
        """
        pdb.set_trace()
        print("Received vCard avatar update from %s" % pres['from'].bare)
        try:
            result = self['xep_0054'].get_vcard(pres['from'], cached=True)
        except XMPPError:
            print("Error retrieving avatar for %s" % pres['from'])
            return
        avatar = result['vcard_temp']['PHOTO']

        filetype = FILE_TYPES.get(avatar['TYPE'], 'png')
        filename = 'vcard_avatar_%s_%s.%s' % (
                pres['from'].bare,
                pres['vcard_temp_update']['photo'],
                filetype)
        with open(filename, 'w+') as img:
            img.write(avatar['BINVAL'])

    def on_avatar(self, msg):
        """
        Getting Profile Picture using url: Working
        """
        pdb.set_trace()
        print("Received avatar update from %s" % msg['from'])
        metadata = msg['pubsub_event']['items']['item']['avatar_metadata']
        for info in metadata['items']:
            if not info['url']:
                try:
                    result = self['xep_0084'].retrieve_avatar(msg['from'], info['id'])
                except XMPPError:
                    print("Error retrieving avatar for %s" % msg['from'])
                    return

                avatar = result['pubsub']['items']['item']['avatar_data']

                filetype = FILE_TYPES.get(metadata['type'], 'png')
                filename = 'avatar_%s_%s.%s' % (msg['from'].bare, info['id'], filetype)
                with open(filename, 'w+') as img:
                    img.write(avatar['value'])
            else:
                # We could retrieve the avatar via HTTP, etc here instead.
                pass

xmpp = StatusWatcher('facebook') # The account to monitor
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0199')


# vcard
xmpp.register_plugin('xep_0054')
xmpp.register_plugin('xep_0153')
xmpp.register_plugin('xep_0084')
    
if xmpp.connect():
    xmpp.process(threaded=False)
