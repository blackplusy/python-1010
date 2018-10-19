#coding=utf-8

class animal:
	def jiao(self):
		print('ao~~~~~~~~')
class dog(animal):
	def jiao(self):
		print('wang！！！！')
class cat(animal):
	def jiao(self):
		print('miao~~~~~~')

def test(obj):
	obj.jiao()

a=animal()
a.jiao()
b=dog()
c=cat()
test(b)
test(c)



