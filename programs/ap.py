s='''9 12 58
8 9 69
22 14 48
20 3 12
2 13 52
27 3 22
2 12 20
4 10 99'''

l2=[]
l3=[]
l4=[]
l5=[]
sum=0
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

for x in range(0,24,3):
	n=float(l2[x+2]/2)
	a=n*(2*l2[x]+((l2[x+2]-1)*l2[x+1]))
	l4.append(a)
for y in l4:
	print(int(y),' ')