'''
If an object walks and quaks like a duck then it is a duck.



'''
class Duck(object):

	def quack(self):
		print('quack, quack')

	def fly(self):
		print('flap, flap!')

class Person(object):

	def quack(self):
		print('I am quacking like a duck')

	def fly(self):
		print('i am flaping with my arms')
def quack_and_fly(thing):
	#not duck typing (non-pythonic)
	if isinstance(thing,Duck):
		thing.quack()
		thing.fly()
	else:
		print('this has to be a duck')

	print()

d=Duck()
quack_and_fly(d)

p=Person()
quack_and_fly(p)   #does not meet the instance of duck

'''
o/p:quack, quack
flap, flap!

this has to be a duck
'''