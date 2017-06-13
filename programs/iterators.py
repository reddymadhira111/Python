'''
Behind the scenes, the for statement calls iter() on the container object. 
The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time.
When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. 

'''

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("text.txt"):
    print(line, end='')

#inner for loop process
s='linga'
it=iter(s)
print('\n',next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))   StopIteration error

#add iterator behavior to your classes.
class Reverse(object):
	def __init__(self,data):
		self.data=data
		self.index=len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index==0:
			raise StopIteration
		self.index=self.index-1
		return self.data[self.index]

rev=Reverse('linga')
k=iter(rev)
for i in k:
	print(i)

