#coding=utf-8
#嵌套函数
'''def t1():
	print('im in test 1')

def t2():
	t1()
	print('im in test 2')
def t3():
	t2()
	print('im in test 3')

t3()'''

def func(n):
	print('进入到第%d层梦'%n)
	if n==3:
		print('进入到潜意识区')
	else:
		func(n+1)
	print('从第%d层梦中醒来'%n)

func(1)





