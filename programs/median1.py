from statistics import median

s='''96 955 103
687 696 693
357 354 362
564 5 1511
945 953 1431
303 328 3
995 929 21
9 391 22
17 6 20
76 86 80
758 232 194
71 69 78
61 4 22
11 9 73
1110 245 312
79 85 96
1078 987 39
122 895 126
9 1 870
20 63 55
98 4 165
1410 1390 865
3 16 12
874 29 870'''

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
for a in range(0,72,3):
	c=l2[a:a+3]
	l5.append(median(c))
for d in l5:
	print(d,' ')





	
