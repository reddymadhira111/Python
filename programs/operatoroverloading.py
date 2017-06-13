'''
You can change the meaning of an operator in Python depending upon the operands used. This practice is known as operating overloading.
This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.
Class functions that begins with double underscore __ are called special functions in Python. 

'''

class Point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __str__(self):
		return '({0},{1})'.format(self.x,self.y)

	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		return Point(x,y)

a=Point(1,2)
b=Point(3,4)
print(a+b)     #unsupported operand type(s) for +: 'Point' and 'Point'
               #(4,6):after writing __add__() method
#What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2) which in turn is Point.__add__(p1,p2).
print(a)        #<__main__.Point object at 0x000001D2C494C898>:before  defing __str__() method
                #(1,2):after defining
#That did not print well. But if we define __str__() method in our class, we can control how it gets printed.
'''Operator Overloading Special Functions in Python
Operator	Expression	Internally
Addition	p1 + p2	     p1.__add__(p2)
Subtraction	p1 - p2	     p1.__sub__(p2)
Multiplication	p1 * p2	 p1.__mul__(p2)
Power	p1 ** p2	     p1.__pow__(p2)
Division	p1 / p2	     p1.__truediv__(p2)
Floor Division	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	p1 & p2         	p1.__and__(p2)
Bitwise OR	p1 | p2	            p1.__or__(p2)
Bitwise XOR	p1 ^ p2	            p1.__xor__(p2)
Bitwise NOT	~p1	                p1.__invert__()


Comparision Operator Overloading in Python
Operator	Expression	Internally
Less than	p1 < p2	       p1.__lt__(p2)
Less than or equal to	p1 <= p2	p1.__le__(p2)
Equal to   p1 == p2	                      p1.__eq__(p2)
Not equal to	p1 != p2	      p1.__ne__(p2)
Greater than	p1 > p2         	p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)
'''