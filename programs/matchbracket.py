s='''(a+[b*c]-{d/3})
(a + [b * c) - 17]
(((a * x) + [b] * y) + c
auf(zlo)men [gy<psy>] four{s}'''

l=s.split('\n')
print(l)
l1=[]
for i in l:
	c=0
	for j in i:
		if j=='(' or j=='[' or j=='{' or j=='<':
			for k in i:
				if k==')':
					i=i[i.index(j):i.index(k)]
					break
					
				elif k==']':
					i=i[i.index(j):i.index(k)]
					break
				elif k=='}':
					i=i[i.index(j):i.index(k)]
					break
				elif k=='<':
					i=i[i.index(j):i.index(k)]
					break
			c+=1
		else:
			continue
		
	
	if c>0:
		l1.append(1)
	else:
		l1.append(0)
print(l1)











'''
	try:
		j=int(i)
		l1.append(1)
	except SyntaxError:
		l1.append(0)
print(l1)
	
'''




