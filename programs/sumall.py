s='''37 280 163
59 251 174
81 118 59
352 236 169
138 212 155
141 178 167
164 178 20
281 124 158
36 103 167
154 297 99'''

l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
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

for x in range(0,30,3):
	y=l2[x]*l2[x+1]+l2[x+2]
	l4.append(y)
print(l4)
def digit_sum(n):
	sum=0
	l5=list(str(n))
	print(l5)
	for i in l5:
		sum=sum+int(i)
	return sum
for z in l4:
	o=digit_sum(z)
	l6.append(o)
print(l6)
for a in l6:
	print(a,' ')
