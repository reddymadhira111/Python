'''
tuple=()
tuples are immutable



'''
#1. creating a tuple
t=(1,2,3.5,[1,2],'tmobile')
print(t)
print(type(t))
print(len(t))

#tuple() takes atmost one argument
print(tuple('bar'))

#tuple slicing
print(t[:3])
print(t[3][1])

#tuple operations
t1=t[0],t[2],t[3]
print(t1)
t3=(22,54,54,447)
print(max(t3))
print(min(t3))
print(t3.index(54))    #index()
print(t3.count(54))    #count()

a=1
b=3
a,b=b,a  #swapping with tuple in one step
print(a,b)

for pair in enumerate(t3):    #enumerate() :gives the pair of index and values
	print(pair)
#1.concatination
t2=t+t1
print(t2)

#2.deleting 
del t2

#3.cmp() method,python3 does not compare method
#operators:compares the first element in the tuple only
print((2,3)>(3,2))
print((3,4)>(2,99))
print((2,3)<=(3,4))
print((2,3)==(2,3))

#if tuple objects contain some mutable objects like list.we can change the mutable objects inside the tuple
t[3][1]=[3,4]
print(t)

#default collection type is tuple
x,y,z=1,2,3
print(x,y,z)
print(2,3<4,3)

#single element in a tuple
d=(1)
print(d,type(d))  #o/p: 1,int
d1=(1,)
print(d1,type(d1))  #o/p: 1,tuple

#example programs

#Write a Python program to create a tuple.
t=(1,2,3)
t1=tuple('123')
print(t,t1)

#Write a Python program to create a tuple with different data types
t=(1,1.2,[1,2],'str')
print(t)

#Write a Python program to count the elements in a list until an element is a tuple
l=[1,3,4,5,(6,),57]
c=0

for i in range(len(l)):
	if type(l[i])==tuple:
		print('touple found')
		break
	else:
	    c+=1	
print(c)

#Write a Python program to sort a tuple by its float element.
t= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
for i in range(len(t)):
	if float(t[0][1])<float(t[1][1]):
		t[0],t[1]=t[1],t[0]
	elif float(t[0][1])<float(t[2][1]):
		t[0],t[2]=t[2],t[0]
	elif float(t[1][1])<float(t[2][1]):
		t[1],t[2]=t[2],t[1]
	



print(t)


