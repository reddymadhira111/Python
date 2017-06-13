import glob
import sys

w_data = 'C:/Users/reddy/Desktop/python/Coding test/sample test/w_data/*.txt'
y_data = 'C:/Users/reddy/Desktop/python/Coding test/sample test/y_data/*.txt'

files = glob.glob(w_data)
lamax=[]
lamin=[]
lt=[]
l1 = []
l2 = []
max_temp = []
min_temp = []
precp = []


for year in range(1985,2015):	
	for file in files:
		data = open(file, 'r').readlines()
		for i in data:
			j=i.split()
			k = (j[0])
			y = int(k[:4])
			if year == y:
				max_temp.append(int(j[1]))
				min_temp.append(int(j[2]))
				precp.append(int(j[-1]))
			
		#print(max_temp,min_temp,total_precp, type(max_temp) )
		avg_max_temp = (sum(max_temp)/len(max_temp))*10
		avg_min_temp = (sum(min_temp)/len(min_temp))*10
		total_precp = (sum(precp))/10
		
		lamax.append(round(avg_max_temp, 2))
		lamin.append(round(avg_min_temp,2))
		lt.append(round(total_precp,2))
		l2.append(y)
		l1.append(file.split('/')[-1].split('.')[0])


l3=list(zip(l1,l2, lamax, lamin, lt))
l3.sort()
#print(l3, len(l3))

lmax=[]
lmin=[]
lpp=[]
lmaxc=[]
lminc=[]
lppc=[]
lp=[]
ly=[]
lmt=[]
lmit=[]
ltp=[]

for i in l3:
	j = i[2]
	lmax.append(int(j))
	k= i[3]
	lmin.append(int(k))
	m=i[4]
	lpp.append(int(m))

high_max_temp = int((max(lmax)))
high_min_temp = int((max(lmin)))
high_total_precp = int((max(lpp)))

for y in range(1985,2015):
	for y1 in l3:
		if y == y1[1]:
			for j in l3:
				if high_max_temp == (int(j[2])) :
					c=0
					lmaxc.append(c)
			for j in l3:
				if high_min_temp == (int(j[3])):
					d=0
					lminc.append(d)
			for j in l3:
				if high_total_precp == (int(j[4])):
					e=0
					lppc.append(e)

	lmt.append(len(lmaxc))
	lmit.append(len(lminc))
	ltp.append(len(lppc))


for i in range(1985,2015):
	ly.append(i)


p3 = list(zip(ly,lmt,lmit,ltp))	
p3.sort()
print(p3,len(p3))




problem3_output = 'C:/Users/reddy/Desktop/python/Coding test/sample test/answer/YearHistogram.out'


sys.stdout = open(problem3_output, 'w')
print(p3)
sys.stdout.close()

	






