'''
sum=lambda a1,a2:a1+a2
print('相加后的值是',sum(10,20))

stu=[{'name':'tom','age':18},{'name':'jerry','age':20},{'name':'snoopy','age':6}]
stu.sort(key=lambda x:x['age'])
print(stu)
'''
def operation(a,b,opt):
	re=opt(a,b)
	return re

num1=int(input('num1:'))
num2=int(input('num2:'))
res=operation(num1,num2,lambda a,b:a+b)
print(res)
