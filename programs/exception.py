'''
Errors detected during excution are called exceptions.
Exceptions should be class objects. The exceptions are defined in the module exceptions.
The basic terminology and syntax used to handle errors in Python is the try and except statements.
The code which can cause an exception to occue is put in the try block and the handling of the exception is the implemented in the except block.
ex:
try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 



'''

#ex1:
try:
	f=open('text.txt','r')
	f.write('write this text')
except IOError:
	print('Error:could not find file or read data')
else:
	print('content written successfully')
	f.close()

#The finally: block of code will always be run regardless if there was an exception in the try code block.
'''
try:
   Code block here
   ...
   Due to any exception, this code may be skipped!
finally:
   This code block would always be executed.
'''

try:
	f=open('text.txt','w')
	f.write('this code is in write mode')
finally:
	print('always executed')
	f.close()
#ex2:
def askint():
	while True:
		try:
			ip=int(input('enter an integer:'))
		except:
			print('enter correct input')
			continue
		else:
			print('entered correct input')
			break
		finally:
			print('finally i executed')
		print(ip)
askint()

print('ex3')
#ex3
import sys

try:
	f=open('text.txt')
	s=f.readline()
	i=int(s.strip())
except OSError as err:
	print('os error: {0}'.format(err))
except ValueError:
	print('does not convert to int')
except :
	print('error:',sys.exc_info()[0])
	raise

#ex4
print('ex4')

for arg in sys.argv[1:]:
	try:
		f=open(arg, 'r')
	except OSError:
		print('cannot open',arg)
	else:
		print(arg, 'has', len(f.readlines()),'lines')
		f.close()
#ex5
print('ex5')

try:
	raise Exception('spam','eggs')
except Exception as ins:
	print(type(ins))   #the exception instance
	print(ins.args)    #arguments stored in .args
	print(ins)         #__str__ allows args to be printed directly

	x,y=ins.args
	print('x=',x)
	print('y=',y)

#user defined exceptions
'''
Exception classes can be defined which do anything any other class can do, 
but are usually kept simple, often only offering a number of attributes 
that allow information about the error to be extracted by handlers for the exception.
 When creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions 
defined by that module, and subclass that to create specific exception classes for different error conditions:
ex:
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

