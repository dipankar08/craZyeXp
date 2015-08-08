#!/usr/bin/env python

import os
import uuid
import json
import tornado.ioloop
import tornado.web
from tornado import websocket


class RoomHandler(object):
    """Store data about connections, rooms, which users are in which rooms, etc."""
    def __init__(self):
        self.client_info = {}  # for each client id we'll store  {'wsconn': wsconn, 'room':room, 'nick':nick}
        self.room_info = {}  # dict  to store a list of  {'cid':cid, 'nick':nick , 'wsconn': wsconn} for each room
        self.roomates = {}  # store a set for each room, each contains the connections of the clients in the room.

    def add_roomnick(self, room, nick):
        """Add nick to room. Return generated clientID"""
        # meant to be called from the main handler (page where somebody indicates a nickname and a room to join)
        cid = uuid.uuid4().hex  # generate a client id.
        if not room in self.room_info:  # it's a new room
            self.room_info[room] = []
        c = 1
        nn = nick
        nir = self.nicks_in_room(room)
        while True:
            if nn in nir:
                nn = nick + str(c)
            else:
                break
            c += 1

        self.client_info[cid] = {'room': room, 'nick': nn}  # we still don't know the WS connection for this client
        self.room_info[room].append({'cid': cid, 'nick': nn})
        return cid

    def add_client_wsconn(self, client_id, conn):
        """Store the websocket connection corresponding to an existing client."""
        self.client_info[client_id]['wsconn'] = conn
        cid_room = self.client_info[client_id]['room']

        if cid_room in self.roomates:
            self.roomates[cid_room].add(conn)
        else:
            self.roomates[cid_room] = {conn}

        for user in self.room_info[cid_room]:
            if user['cid'] == client_id:
                user['wsconn'] = conn
                break
        # send "join" and and "nick_list" messages
        self.send_join_msg(client_id)
        nick_list = self.nicks_in_room(cid_room)
        cwsconns = self.roomate_cwsconns(client_id)
        self.send_nicks_msg(cwsconns, nick_list)

    def remove_client(self, client_id):
        """Remove all client information from the room handler."""
        cid_room = self.client_info[client_id]['room']
        nick = self.client_info[client_id]['nick']
         # first, remove the client connection from the corresponding room in self.roomates
        client_conn = self.client_info[client_id]['wsconn']
        if client_conn in self.roomates[cid_room]:
            self.roomates[cid_room].remove(client_conn)
            if len(self.roomates[cid_room]) == 0:
                del(self.roomates[cid_room])
        r_cwsconns = self.roomate_cwsconns(client_id)
        # filter out the list of connections r_cwsconns to remove clientID
        r_cwsconns = [conn for conn in r_cwsconns if conn != self.client_info[client_id]['wsconn']]
        self.client_info[client_id] = None
        for user in self.room_info[cid_room]:
            if user['cid'] == client_id:
                self.room_info[cid_room].remove(user)
                break
        self.send_leave_msg(nick, r_cwsconns)
        nick_list = self.nicks_in_room(cid_room)
        self.send_nicks_msg(r_cwsconns, nick_list)
        if len(self.room_info[cid_room]) == 0:  # if room is empty, remove.
            del(self.room_info[cid_room])
            print "Removed empty room %s" % cid_room

    def nicks_in_room(self, rn):
        """Return a list with the nicknames of the users currently connected to the specified room."""
        nir = []  # nicks in room
        for user in self.room_info[rn]:
            nir.append(user['nick'])
        return nir

    def roomate_cwsconns(self, cid):
        """Return a list with the connections of the users currently connected to the room where
        the specified client (cid) is connected."""
        cid_room = self.client_info[cid]['room']
        r = []
        if cid_room in self.roomates:
            r = self.roomates[cid_room]
        return r


    def send_join_msg(self, client_id):
        """Send a message of type 'join' to all users connected to the room where client_id is connected."""
        nick = self.client_info[client_id]['nick']
        r_cwsconns = self.roomate_cwsconns(client_id)
        msg = {"msgtype": "join", "username": nick, "payload": " joined the chat room."}
        pmessage = json.dumps(msg)
        for conn in r_cwsconns:
            conn.write_message(pmessage)

    @staticmethod
    def send_nicks_msg(conns, nick_list):
        """Send a message of type 'nick_list' (contains a list of nicknames) to all the specified connections."""
        msg = {"msgtype": "nick_list", "payload": nick_list}
        pmessage = json.dumps(msg)
        for c in conns:
            c.write_message(pmessage)

    @staticmethod
    def send_leave_msg(nick, rconns):
        """Send a message of type 'leave', specifying the nickname that is leaving, to all the specified connections."""
        msg = {"msgtype": "leave", "username": nick, "payload": " left the chat room."}
        pmessage = json.dumps(msg)
        for conn in rconns:
            conn.write_message(pmessage)


class MainHandler(tornado.web.RequestHandler):

    def initialize(self, room_handler):
        """Store a reference to the "external" RoomHandler instance"""
        self.__rh = room_handler

    def get(self):
        """Render chat.html if required arguments are present, render main.html otherwise."""
        try:
            room = self.get_argument("room")
            nick = self.get_argument("nick")
            cid = self.__rh.add_roomnick(room, nick)
            self.render("templates/chat.html", clientid=cid)
        except tornado.web.MissingArgumentError:
            self.render("templates/main.html")

class ClientWSConnection(websocket.WebSocketHandler):

    def initialize(self, room_handler):
        """Store a reference to the "external" RoomHandler instance"""
        self.__rh = room_handler
    def check_origin(self, origin):
        return True
    def open(self, client_id):
        self.__clientID = client_id
        self.__rh.add_client_wsconn(client_id, self)
        print "WebSocket opened. ClientID = %s" % self.__clientID

    def on_message(self, message):
        msg = json.loads(message)
        msg['username'] = self.__rh.client_info[self.__clientID]['nick']
        pmessage = json.dumps(msg)
        rconns = self.__rh.roomate_cwsconns(self.__clientID)
        for conn in rconns:
            conn.write_message(pmessage)

    def on_close(self):
        print "WebSocket closed"
        self.__rh.remove_client(self.__clientID)

if __name__ == "__main__":
    rh = RoomHandler()
    app = tornado.web.Application([
        (r"/", MainHandler, {'room_handler': rh}),
        (r"/ws/(.*)", ClientWSConnection, {'room_handler': rh})],
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
    app.listen(8888)
    print 'Simple Chat Server started.'
    print 'listening on 8888 ...'
    tornado.ioloop.IOLoop.instance().start()

