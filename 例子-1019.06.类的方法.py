#coding=utf-8

class people:
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country

p=people()
print(p.getcountry()) #通过实例对象调用类的方法
print(people.getcountry())#通过类对象调用类的方法

#类的方法还有一个用途是可以对类的属性进行修改
class people:
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country
	@classmethod
	def setcountry(cls,country):
		cls.country=country

p=people()
print(p.getcountry())
p.setcountry('USA')
print(p.getcountry())









