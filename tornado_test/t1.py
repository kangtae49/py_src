num = 10

def a():
    print num

def b():
    num = 20 # local
    print num

def c():
    global num
    num = 30
    print num

a()
b()
a()

c()
a()