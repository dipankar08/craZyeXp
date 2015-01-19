############################
# Core Chat Server uisng socketio purely.
#
############################


import os
import logging
import pdb
from gevent import monkey; monkey.patch_all()

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin

class LonelyRoomMixin(object):
    def __init__(self, *args, **kwargs):
        super(LonelyRoomMixin, self).__init__(*args, **kwargs)
        if 'rooms' not in self.session:
            self.session['rooms'] = set()  # a set of simple strings

    def join(self, room):
        """Lets a user join a room on a specific Namespace."""
        self.session['rooms'].add(self._get_room_name(room))

    def leave(self, room):
        """Lets a user leave a room on a specific Namespace."""
        self.session['rooms'].remove(self._get_room_name(room))

    def _get_room_name(self, room):
        return self.ns_name + '_' + room

    def emit_to_room(self, room, event, *args):
        """This is sent to all in the room (in this particular Namespace)"""
        pkt = dict(type="event",
                   name=event,
                   args=args,
                   endpoint=self.ns_name)
        room_name = self._get_room_name(room)
        for sessid, socket in self.socket.server.sockets.iteritems():
            if 'rooms' not in socket.session:
                continue
            #if room_name in socket.session['rooms'] and self.socket != socket:
            if room_name in socket.session['rooms']:
                socket.send_packet(pkt)

class ChatNamespace(BaseNamespace):
    def initialize(self):
        self.logger = logging.getLogger("socketio.chat")
        self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))

    def on_hello(self,data):
        """
        Only recv bo Emit..
        """
        print 'on_use_gdb:',data
        pass    
    def on_hello_reply(self,data):
        """
        This is sent the same info to itself.
        """
        pkt = dict(type="event",
                   name='recv_data',
                   args=(data,),
                   endpoint=self.ns_name)

        self.socket.send_packet(pkt)   
        
    def on_hello_reply_all(self,data):
        """
        This is sent to all in the sockets in this particular Namespace,
        """
        pkt = dict(type="event",
                   name='recv_data',
                   args=(data,),
                   endpoint=self.ns_name)

        for sessid, socket in self.socket.server.sockets.iteritems():
          socket.send_packet(pkt)

    def on_hello_reply_all_not_me(self, data):
        """
        This is sent to all in the sockets in this particular Namespace,
        except itself.
        """
        #pdb.set_trace()
        pkt = dict(type="event",
                   name="recv_data",
                   args=(data,),
                   endpoint=self.ns_name)

        for sessid, socket in self.socket.server.sockets.iteritems():
            if socket is not self.socket:
                socket.send_packet(pkt)
        
class Application(object):
    def __init__(self):
        self.buffer = []
        # Dummy request object to maintain state between Namespace
        # initialization.
        self.request = {
            'nicknames': [],
        }

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/')

        if not path:
            try:
                data = open('chat.html').read()
            except Exception:
                return not_found(start_response)

            start_response('200 OK', [('Content-Type', 'text/html')])
            return [data]


        if path.startswith('static/'):
            try:
                data = open(path).read()
            except Exception:
                return not_found(start_response)

            if path.endswith(".js"):
                content_type = "text/javascript"
            elif path.endswith(".css"):
                content_type = "text/css"
            else:
                content_type = "text/html"

            start_response('200 OK', [('Content-Type', content_type)])
            return [data]

        if path.startswith("socket.io"):
            #pdb.set_trace()
            socketio_manage(environ, {'': ChatNamespace}, self.request)
        else:
            return not_found(start_response)


def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print 'Listening on port {}'.format(port)
    SocketIOServer(('0.0.0.0', port), Application(),
        resource="socket.io").serve_forever()
