import math
s='''74951 11
181 11
9516 6
11070 2
73 6
969 5
107 4
92 2
42 3
52 13'''

l2=[]
l3=[]
l4=[]
l5=[]
l=s.split('\n')
for k in l:
	m=k.split(' ')
	l3.append(m)
print(l3)
for i in l3:
	for j in i:
		n=int(j)
		l2.append(n)
print(l2)

for x in range(0,20,2):
	r=1
	if l2[x+1] > 0:
		for y in range(l2[x+1]):
			d=(l2[x]/r)
			r=(r+d)/2
		if r==int(r):
			l4.append(int(r))
		else:
			l4.append(r)
	else:
		l4.append(1)

print(l4)
for z in l4:
	print(z,' ')