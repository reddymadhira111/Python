s="ababbcdeab"
l=[]
l1=[]
for i in s:
	
	l.append(i)

print(l)
for i in l:
	j=l.count(i)
	l1.append(j)

print(l1)
d=dict(zip(l,l1))
print(l2)