# -*- coding: utf-8 -*-
import errno
import functools
import tornado
from tornado.ioloop import IOLoop, PeriodicCallback, PollIOLoop
import socket
def handle_connection(connection, address):
	print connection, address

def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error, e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection, address)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)
sock.bind(('', 8888))
sock.listen(128)


#io_loop = tornado.ioloop.IOLoop.instance()
io_loop = IOLoop.instance()
callback = functools.partial(connection_ready, sock)
io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
io_loop.start()

