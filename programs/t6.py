a=4
b=7
x=lambda : a if 1 else b
lambda x:'big' if x>100 else 'small'
print(x())

#x=2+3.5+2+3i
print(type(x))
import datetime
dt = datetime.datetime.now()
print(dt)

def x():
	print('x')
	return True
def y():
	print('y')
	return False

def z():
	if x() or y():
		print('x or y')

	if x() and y():
		print('x oa y')
	else:
		print('z')

z()
'''
def s():
	pass

try:
	x=1/0
except (ArthimeticError, ZeroDivisionError):
	print('d')
try:
	s()
finally:
	CleanupFunction()

'''
class A:
	def __init__(self, a='A', b='B'):
		self.a= a
		self.b=b
a=A(a=1,b=2)
print(vars(a))