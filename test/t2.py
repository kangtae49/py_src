'''
class A(object):
	l = []

	def show(self):
		print self.l

	def add(self, x):
		self.l.append(x)
'''

'''
class A(object):
	def __init__(self):
		self.l = []

	def show(self):
		print self.l

	def add(self, x):
		self.l.append(x)
'''
class A(object):

	def __init__(self):
		self.l = []

	def show(self):
		print self.l

	def add(self, x):
		self.l.append(x)

a = A()
a.add('a')
a.show()

b = A()
b.add('b')
b.show()

a.show()

