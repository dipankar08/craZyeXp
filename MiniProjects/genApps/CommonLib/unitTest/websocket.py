import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import define, options, parse_command_line
import pdb

define("port", default=9999, help="run on the given port", type=int)
# we gonna store clients in dictionary..
clients = dict()
# Dipankar: We are not using this, as we are using django..
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        pdb.set_trace()
        self.write("This is your response")
        self.finish()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        pdb.set_trace()
        self.id = self.get_argument("Id")
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}
        print '>>> adding client',clients[self.id]
    def check_origin(self, origin):
        return True
    def on_message(self, message):        
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        pdb.set_trace()
        print "Client %s received a message : %s" % (self.id, message)
        
    def on_close(self):
        pdb.set_trace()
        if self.id in clients:
            del clients[self.id]

app = tornado.web.Application([
    #(r'/', IndexHandler),
    (r'/', WebSocketHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port,address="0.0.0.0")
    print '>>> Starting application on ',options.port
    print 'Ex: http://192.168.56.111:9999/'
    tornado.ioloop.IOLoop.instance().start()