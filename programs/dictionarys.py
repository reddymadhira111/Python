'''
dictionaries are mapping type in python
mapping objetcs have one-many relations between keys and values
mutable objects

'''
#create a dictionary
d={'d1':'linga'}
d1=dict((['x', 1],['y',2]))
d2={}.fromkeys(('x1','y1'),1)
print(d1)
print(d2)
#add elements to dictionary
d['d2']=2

#retrival keys and values.Both returns a list of elements
#items() gives the key-value pair in tuple format
print(d.keys())
print(d.values())
print(d.items())

#key-value retrival using for loop
for key in d1:
	print(key,d1[key])

#check if a key is there in a dictionary
print('d2' in d)   #return true

print('i am %(d1)s and my value is %(d2)d' %d)
#o/p:i am linga and my value is 2

#delete,clear and pop operations
print(d1)
del d1['x']     #remove entry with key:x
print(d1)
d2.clear()      #clear all the key-value pairs
print(d2)
print(d1.pop('y'))   #remove and return the associated value

#updates d with d1 values
print(d)
d1={'a':4}
d.update(d1)
print(d)