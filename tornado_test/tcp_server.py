# -*- coding: utf-8 -*-
import socket
import tornado
import signal
import struct
from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop, PeriodicCallback, PollIOLoop
from tornado.netutil import bind_sockets
import datetime

#socket.setdefaulttimeout(10)

class Server(TCPServer):

	def handle_stream(self, stream, address):
		StreamHandler(stream, address)


class StreamHandler(object):
	def __init__(self, stream, address):
		self.stream = stream


		#stream.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		#stream.socket.setsockopt(socket.IPPROTO_TCP, socket.SO_KEEPALIVE, 1)
		self.stream.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, 1)

		self.address = address
		self.stream.read_until_close(self.read_done, self.read_chunk)

		def on_timeout():
			print 'timeout'
			self.stream.close()
		loop = IOLoop.instance()
		loop.add_timeout(datetime.timedelta(seconds=10), on_timeout)

		#self.stream.read_until_close(self.on_close)

	def read_done(self, data):
		print('[%s]close[%s]%s' % (self, self.address, data))

	def read_chunk(self, data):
		print('[%s]chunk[%s]%s' % (self, self.address, data))
		#pass

is_closing = False

def sig_handler(signum, frame):
	global is_closing

	print (signum, frame)
	is_closing = True
	#print ('sig_handler')


def try_exit():
	global is_closing
	#print ('is_closing: %s' % is_closing)
	if is_closing:
		IOLoop.instance().stop()

def main():
	server = Server()
	server.listen(8888)

	#signal
	signal.signal(signal.SIGINT, sig_handler)
	PeriodicCallback(try_exit, 100).start()

	IOLoop.instance().start()
	#PollIOLoop.instance().start()

if __name__ == '__main__':
	main()


