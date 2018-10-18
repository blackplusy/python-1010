'''def test1():
	a=10
	print('修改前a的值是',a)
	a=20
	print('修改后a的值是',a)

def test():
	a=40
	print('我是test2中的a',a)

test1()
test() '''
'''

a=100
print('a的值是',a)

def test01():
	a=20
	print('test01中a的值是',a)

def test02():
	print('test02中a的值是',a)

test01()
test02()

'''
a=100
print('a的值是',a)

def test1():
	global a
	a=200
	print('test1中修改全局变量a',a)

def test2():
	print('test2中使用全局变量a',a)

test1()
test2()







