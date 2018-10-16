#coding=utf-8
#type  查看变量数据类型
a=(1,)
print(a)
print(type(a))

tup=(1,2,3,4)
for i in tup:
	print(i)

tup=(1,2,3,4)
del tup
#print(tup)

tup=(1,2,3,4,5)
print(tup[0])
print(tup[-2])
print(tup[2:4]) 
print(tup[3:])
print(tup[:3])

a=(1,2,3,1,1,1)
print(a.count(1))






