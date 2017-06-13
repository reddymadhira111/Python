'''
overriding is the ability of a class to change the implementation of a method provided by its instances

'''
#ex1:method overriding
class Father:
	def print_firstname(self):
		print('Father name')
	def print_lastname(self):
		print('surname')

class Son(Father):
	def print_firstname(self):      #same method as parent but overriding with son name
		print('Son name')

obj_son=Son()
obj_son.print_firstname()      #son name
obj_son.print_lastname()       #surname