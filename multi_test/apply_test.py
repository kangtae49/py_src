import os
import sys
import random
import time
from threading import Thread

from multiprocessing import Pool

NUM = 50

def task(p):
	for i in range(1000*1000*10):
		random.random()

def test():
	for i in range(NUM):
		task('id0')

def test_pool():
	pool = Pool(8*2)

	for i in range(NUM):
		pool.apply(task, ('id0',))

	pool.close()
	pool.join()


def main():
	func_list = [test, test_pool]
	for func in func_list:
		t1 = time.time()
		func()
		t2 = time.time()
		print('[%s] time: %s' % (func.func_name, (t2-t1)))

def xx():
	while True:
		random.random()

if __name__ == '__main__':
	th = Thread(target=xx)
	th.start()
	print ('start')
	t1 = time.time()
	main()
	t2 = time.time()
	print('time : %s' % (t2-t1))



