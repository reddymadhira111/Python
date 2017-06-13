'''
method overloading is not possible in python
it takes the updated or latest method in the class for future use
python only understand the latest implementation of method
'''
'''
#ex1:
class Father:
	def add(self,x,y):
		return x+y
	def add(self,x,y,z):
		return x+y+z

obj_1=Father()
print(obj_1.add(1,2,3))   #6
print(obj_1.add(3,4))     #add() missing 1 required positional argument: 'z'
#it takes the latest method with 3 arguments only.p

#ex2
class Father:
	def add(self,x,y,z):
		return x+y+z
	def add(self,x,y):
		return x+y


obj_1=Father()
print(obj_1.add(3,4))      #7
print(obj_1.add(1,2,3))   #add() takes 3 positional arguments but 4 were given
'''
#ex3:to overcome method overloading the follwing ex
class Father:
	def add(self,*args):
		result=0
		for i in args:
			result+=i
		return result
obj_1=Father()
print(obj_1.add(1,3,4))   #8
print(obj_1.add(3,6))     #9

				

    