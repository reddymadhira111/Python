class Book(object):
	title= ''
	pages= 0
	def __init__(self,title='',pages=0):
		self.title=title
		self.pages=pages
	def __str__(self):
		return self.title
	def __radd__(self,other):
		return self.pages+other
	def __add__(self,other):
		return self.pages + other
#from books import Book
book1= Book('Linga',300)
book2= Book('Reddy',400)
book1+book2
sum([book1,book2])
print(book1.__add__(book2))
print(book1.__str__())

'''
class Student(object):
	def __init__(self,name,roll_no):
		self.name=name
		self.roll_no=roll_no
	def message(self):
		print(self.name,'is awesome')
	#def __gt__(self,other):
	#	return self.roll_no>other.roll_no
	def __ge__(self,other):
		return self.roll_no>=other.roll_no
obj=Student('Linga',55)
print(obj.message())
obj.message()
'''
'''
print(__file__)
print(__name__)
print(__builtins__)
print(__loader__)
print(__spec__)
print(__package__)'''

'''obj1=Student('Srikar',55)
obj1.message()
print(type(obj),type(obj1))
#print(obj>obj1)
print(obj>=obj1)
print(sum([obj.message(),obj1.message()]))
'''