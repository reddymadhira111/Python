'''range(0,10)
for i in range(0,10):
	print(i)

l=[1,2,3,4,5]
for i in l:
	print(i)

data='word'
print(data[:])
print(data[:-1])
print(data[::-1])
print(data[-1::-4])
print(data[-1:-2])

l=[1,2,3,4,5]
for i in l:
	if i%2==0:
		print(i)
	else:
	    print("odd no")

l=[1,2,3,4,5]
s=0
for i in l:
	s+=i
print(s)

for i in 'this is a string':
	print(i)
    
t=(1,2,3,4,5)
for i in t:
	print(i)


l=[(1,2), (3,4),(5,6)]
for t in l:
	print(t)
for (t1,t2) in l:
	print(t1)
	'''
d={'d1':1, 'd2':2, 'd3':3}
for (i,v) in d:
	print(v)