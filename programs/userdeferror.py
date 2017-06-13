'''
Programs may name their own exceptions by creating a new exception class
Exception classes can be defined which do anything any other class can do, but are usually kept simple, 
often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.
When creating a module that can raise several distinct errors,
 a common practice is to create a base class for exceptions defined by that module,
 and subclass that to create specific exception classes for different error conditions:

'''





'''class Error(Exception):
	pass
class InputError(Error):

	def __init__(self,expression,message):
		self.expression=expression
		self.message=message
class TransitionError(Error):
	def __init__(self,previous,next,message):
		self.previous=previous
		self.next=next
		self.message=message
try:
	raise KeyboardInterrupt
finally:
	print('good bye')
'''
def divide(x,y):
	try:
		result=x/y
	except ZeroDivisionError:
		print('division by zero')
	else:
		print('result is',result)
	finally:
		print('executed finally')
divide(2,1)
divide(2,0)
divide('2','1')