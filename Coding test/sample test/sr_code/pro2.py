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
n = -9999

for year in range(1985,2015):	
	for file in files:
		data = open(file, 'r').readlines()
		for i in data:
			j=i.split()
			k = (j[0])
			y = int(k[:4])

			if year == y:
				for x in range(1,4):
					if n == j[x]:
						j[x] = 0
				max_temp.append(int(j[1]))
				min_temp.append(int(j[2]))
				precp.append(int(j[-1]))
			
		avg_max_temp = (sum(max_temp)/len(max_temp))*10
		avg_min_temp = (sum(min_temp)/len(min_temp))*10
		total_precp = (sum(precp))/100
		
		lamax.append(round(avg_max_temp, 2))
		lamin.append(round(avg_min_temp,2))
		lt.append(round(total_precp,2))
		l2.append(y)
		l1.append(file.split('/')[-1].split('.')[0])

l3=list(zip(l1,l2, lamax, lamin, lt))
l3 = list(set(l3))
l3.sort()
print(l3, len(l3))



problem2_output = 'C:/Users/reddy/Desktop/python/Coding test/sample test/answer/YearlyAverages.out'


sys.stdout = open(problem2_output, 'w')
print(l3)
sys.stdout.close()

	






