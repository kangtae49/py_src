import os
import sys
import zlib

BUF_SIZE = 1024

def gen_dec():
	fd = open('./apache-tomcat-8.0.23.tar.gz', 'rb')
	dec = zlib.decompressobj(16+zlib.MAX_WBITS)
	while True:
		bytes = fd.read(BUF_SIZE)
		if bytes:
			rv = dec.decompress(bytes)
			if rv:
				yield rv
		else:
			break
	fd.close()
			
def main():
	fd_w = open('./apache-tomcat-8.0.23.tar', 'wb')
	for bytes in gen_dec():
		fd_w.write(bytes)
	fd_w.close()
		
	print("main")

if __name__ == '__main__':
	main()
