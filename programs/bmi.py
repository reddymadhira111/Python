s='''53 1.95
67 1.99
107 2.26
46 1.15
68 1.36
80 1.72
56 1.60
53 1.55
115 2.97
79 2.68
112 2.31
102 2.15
68 1.53
105 1.73
84 2.65
45 1.22
56 1.63
116 3.25
103 3.06
116 2.88
41 1.37
100 2.43
110 1.77
93 1.70
42 1.67
107 1.75'''

l1=[]
l2=[]
l3=[]
l4=[]
l=s.split('\n')
for i in l:
	m=i.split(' ')
	l1.append(m)
print(l1)
for j in l1:
	for k in j:
		n=float(k)
		l2.append(n)
print(l2)

for x in range(0,52,2):
	bmi=((l2[x]/l2[x+1]**2))
	if bmi < 18.5:
		l3.append('under')
	elif 18.5 <= bmi < 25.0:
		l3.append('normal')
	elif 25.0 <= bmi < 30.0:
		l3.append('over')
	elif bmi >= 30.0:
		l3.append('obese')

print(l3)
for y in l3:
	print(y,' ')