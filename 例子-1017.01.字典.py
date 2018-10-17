#coding=utf-8
dic={'name':'gaga','QQ':110}
#dic2={'name':'mayun','QQ':119}
print(dic)
dic['name']='8jie'
print(dic)
dic['QQ']=914338492
print(dic)

print('**************8')
dic={'name':'gaga','QQ':110}
print(dic)
del dic['QQ']
print(dic)
del dic
#print(dic)

print('**************8')
dic={'name':'gaga','QQ':110}
print(dic)
dic.clear()
print(dic)


print('**************|||||||||||')
dic={'name':'gaga','QQ':110}
print(dic.keys())
print(dic.values())
for i in dic.keys():
	print(i)
for j in dic.values():
	print(j)

print('**************8')
dic={'name':'gaga','QQ':110}
for i,j in dic.items():
	print(i,j)



print('**************8')
dic={'name':'gaga','QQ':110}
print(dic['name'])
