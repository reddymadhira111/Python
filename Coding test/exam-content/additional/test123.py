import glob
import sys

problem2_output = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers/YearlyAverages.out'

file = glob.glob(problem2_output)


data = open(file, 'r').readlines()

lmax=[]
lmin=[]
lpp=[]
lmaxc=[]
lminc=[]
lppc=[]
l=[]

for i in data:
	j = i[2]
	lmax.append(j)
	k= i[3]
	lmin.append(k)
	m=i[4]
	lpp.append(m)

high_max_temp = max(lmax)
high_min_temp = max(lmin)
high_total_precp = max(lpp)

for i in range(1985,2015):
	for j in data:
		if i == j[1]:
			if high_max_temp == j[2] :
				c=0
				lmaxc.append(c)
			elif high_min_temp == j[3]:
				d=0
				lminc.append(d)
			elif high_total_precp == j[4]:
				e=0
				lppc.append(e)

	d['i']=len(lmaxc)
	d['i']=len(lminc)
	d['i']=len(lppc)

print(d)	



