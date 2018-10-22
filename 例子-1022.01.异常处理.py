学习目标
掌握异常处理的机制和方法

课程内容
a.异常的概念
b.常见的异常
c.异常的处理方式

a.异常的概念
程序执行过程中发生影响程序正常执行的事件，当python无法正常处理时候就会产生异常
异常是python中的一个对象，表示一个错误
捕获异常：为了防止python程序终止，当脚本发生异常时候需要进行捕获

b.常见的异常
1.NameError
没有定义变量就直接使用
p

2.Syntax Error
语法错误
if a

3.IO Error
FileNotFoundError
文件操作不存在等
p=open('/home/heygor/test456','r')

4.ZeroDvisionError
除数为0

5.ValueError
int('d')

c.异常处理的方式
1.try...except
有可能发成错误的代码放在try和except中间
try:
        j
except NameError as e:
        print('cat error!!!')

2.try...except....else
语法：
try：
	代码
except：
	代码
else：
	代码
	#如果没有报错就可以执行其他操作

3.try...finally...
语法：
try：
	代码
finally
	代码
	#如果没有捕获到异常，代码执行
	#如果捕获到异常，先执行这段代码，然后处理异常，finally后面代码一定会执行
try:
        f=open('test9','r')
        print(f.read())
finally:
        print('im living')

4.try...except..finally
语法：
try:
	代码
except：
	代码
finally：
	代码
	#如果try没有捕获到异常，执行finally语句
	#如果捕获到异常，显示出异常，再执行finally

5.try...except...else...finally






























