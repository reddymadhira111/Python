'''
abstraction and encapsulation are same meaning(data hiding)
abstraction is achieved through encapsulation
encapsulation is the mechanism for restricting the access to some of an object's components,
 this means that the internal representation of an object can't be seen from outside of the objects definition. 
Access to this data is typically only achieved through special methods: Getters and Setters.
Instance variable names starting with two underscore characters cannot be accessed from outside of the class. 
At least not directly, but they can be accessed through private name mangling. 
That means, private data __A can be accessed by the following name construct: instance_name._classname__A.
Name  Notation   Behaviour
name	Public   Can be accessed from inside and outside
_name	Protected Like a public member, but they shouldn't be directly accessed from outside.
__name	Private   Can't be seen and accessed from outside

'''

class Encapsulation(object):

	def __init__(self,a,b,c):
		self.public=a
		self._protected=b
		self.__private=c
x = Encapsulation(11,13,17)
print(x.public)
print(x._protected)
print(x.__private)
'''
11
13
Traceback (most recent call last):
  File "abstraction.py", line 26, in <module>
    print(x.__private)
AttributeError: 'Encapsulation' object has no attribute '__private
'''