'''
polymorphism:many forms
similar to method overriding
created two classes son &doughter those inherits the properties of the father class
and overriding those two methods with say_name method

'''
#ex1
class Father:
	def __init__(self,first_name,last_name,age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
	def say_name(self):
		print('Father:',self.first_name,' ',self.last_name)
	def say_age(self):
		print('age:',str(self.age))
class Son(Father):
	def say_name(self):
		print('son:',self.first_name,' ',self.last_name)
class Daughter(Father):
	def say_name(self):
		print('daughter:',self.first_name,' ',self.last_name)

obj1=Father('Rama','madhira',50)
obj2=Son('linga','madhira',25)
obj3=Daughter('ram','madhira',29)
obj1.say_name()            #Father: Rama   madhira
obj2.say_name()            #son: linga   madhira
obj3.say_name()            #daughter: ram   madhira
obj1.say_age()              #age: 50
obj2.say_age()              #age: 25
obj3.say_age()              #age: 29
