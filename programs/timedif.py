s='''3 11 41 42 21 6 28 3
18 22 53 35 26 23 56 40
14 21 27 53 17 13 28 3
17 3 45 46 26 16 5 28
4 21 15 41 18 10 39 39
1 16 40 54 21 14 16 30
13 1 20 29 24 21 50 30
19 3 4 45 20 14 56 42
3 11 17 44 6 23 39 32
4 18 48 1 15 11 39 13
7 1 2 42 22 19 22 55
3 5 17 23 8 5 34 29
8 9 19 14 28 12 19 12
0 7 34 46 4 4 58 24
14 8 44 59 14 15 15 13'''
import math
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

def daytosec(a,b,c,d):
	a1=a*24*3600
	b1=b*3600
	c1=c*60
	d1=d
	s1=a1+b1+c1+d1
	return s1

def sectoday(x):
	x1=x/(24*3600)
	x2=(x%(24*3600))/3600
	x3=((x%(24*3600))%3600)/60
	x4=((x%(24*3600))%3600)%60
	return print('(%d %d %d %d)'%(int(x1),int(x2),int(x3),int(round(x4))))

for e in range(0,120,8):
	f=daytosec(l2[e+4],l2[e+5],l2[e+6],l2[e+7])-daytosec(l2[e],l2[e+1],l2[e+2],l2[e+3])
	l4.append(sectoday(f))




