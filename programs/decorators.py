'''
Decorators can be thought of as functions which modify the functionality of another function
decorator is a function that takes another function and extends the behavior of the
latter function without explicitly modifying it.


'''
def fun():
	return 1
print(fun())

s='Global variable'
def fun():
	print (locals())
print (globals())
print(globals().keys())
print(globals()['s'])
'''
'''
def hello(name='linga'):
	return 'Hello '+ name
print(hello())
greet=hello
print(greet)
print(greet())
'''
'''
def hello(name = 'linga'):
	print('the hello() fn has been executed')
	def greet():
		return '\t this is inside the greet() fn'
	def welcome():
		return '\t this is inside the welcome() fn'
	print(greet())
	print(welcome())
	print('now we are back inside the hello() fn')
print(hello())
#print(welcome())   #NameError: name 'welcome' is not defined

#returning functions from within functions:
def hello(name = 'linga'):
	def greet():
		return '\t this is greet()'
	def welcome():
		return ' this is welcome()'
	if name=='linga':
		return greet
	else:
		return welcome
x=hello()
print(x)
print(x())

def hello():
	return 'linga'
def other(fun):
	print('other code')
	print(fun())
print(other(hello))

def new_decorator(func):
	def wrap_func():
		print('code would be here')
		func()
		print('after func()')
	return wrap_func
def func_needs_decorator():
	print('this func is in need of a decorator')
print(func_needs_decorator())
func_needs_decorator=new_decorator(func_needs_decorator)
print(func_needs_decorator())

#Now lets understand how we can rewrite this code using the @ symbol, which is what Python uses for Decorators:
@new_decorator
def func1():
	print('i am using @new decorator:')

func1()