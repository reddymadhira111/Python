'''
python2:xrange() was a generator.
Generator functions allow us to write a function that can send back a value and then later 
resume to pick up where it left off.
the generator functions will automatically suspend and resume their execution and 
state around the last point of value generation
Generators are best for calculating large sets of results (particularly in calculations that 
involve loops themselves) 
in cases where we don’t want to allocate the memory for all of the results at the same time.
the yield keyword at a function will cause the function to become a generator.
'''
def gencubes(n):
	for num in range(n):
		yield num**3
for x in gencubes(9):
	print(x)

def genfebon(n):
	a=1
	b=1
	for x in range(n):
		yield a
		a,b=b,a+b
for num in genfebon(9):
	print(num)

#The next function allows us to access the next element in a sequence
def simple_gen():
	for x in range(3):
		yield x
g=simple_gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))
#After yielding all the values next() caused a StopIteration error. 

s='hello'
for l in s:
	print(l)
#print(next(s))     this does not allow 
#The iter() function allows us to do iteration over the string
s_iter=iter(s)
print(next(s_iter))

def reverse(d):
	for i in range(len(d)-1,-1,-1):
		yield d[i]
for j in reverse('reddy'):
	print(j)

#generator expressions
#syntax similar to list comprehensions but with parentheses instead of brackets.
#These expressions are designed for situations where the generator is used right away by an enclosing function.
s=sum(i*i for i in range(10))
print(s)

s='santhu'
sr=list(s[i] for i in range(len(s)-1, -1,-1))
print(sr)

u='i am what i am'
uw=set(word for word in u.split(' '))
print(uw)