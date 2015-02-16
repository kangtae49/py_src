# -*- coding: utf-8 -*-
import tornado
import signal
from tornado.tcpserver import TCPServer
from tornado.httpserver import HTTPServer
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop, PeriodicCallback, PollIOLoop
from tornado.netutil import bind_sockets


class WSHandler(WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

def main():
	application = tornado.web.Application([
		(r'/ws', WSHandler),
	])
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)

	IOLoop.instance().start()


if __name__ == '__main__':
    main()


