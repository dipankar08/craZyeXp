############################
# Core Chat Server uisng socketio purely.
#
############################


import os
import logging
import pdb
#from gevent import monkey; monkey.patch_all()

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin

class gdbServer(BaseNamespace):
    def __init__(self, *args, **kwargs):
        super(gdbServer, self).__init__(*args, **kwargs)
        if 'rooms' not in self.session:
            self.session['rooms'] = set()  # a set of simple strings
    def _build_pkt(self,d,en="recv_data"):
      return  dict(type="event",
                   name=en,
                   args=({'status':'success','res':d},),
                   endpoint=self.ns_name)
                   
                   

    def on_attach_gdb(self,data):
        #pdb.set_trace()
        from gdb import pyGdb
        g = pyGdb('./sum.exe')
        self.session['pygdb'] =g 
        self.socket.send_packet(self._build_pkt(d="gdb Attached Successfully..")); 
    def on_run_cmd(self,data):
        #pdb.set_trace()
        if not self.session['pygdb']:
          self.socket.send_packet(self._build_pkt(d="Session broken."));
          return
        gg = self.session['pygdb']
        res = gg.issueCmd(data)
        self.socket.send_packet(self._build_pkt(d=res));

    def on_start_gdb(self,data):
        #pdb.set_trace()
        if not self.session['pygdb']:
          self.socket.send_packet(self._build_pkt(d="Session broken."));
          return
        gg = self.session['pygdb']
        res = gg.start()
        self.socket.send_packet(self._build_pkt(d=res));
        
    def on_stopGdb(self,data):
        pdb.set_trace()
        self.socket.send_packet(self._build_pkt(d="gdb Attached Successfully..")); 
        

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
            socketio_manage(environ, {'': gdbServer}, self.request)
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
