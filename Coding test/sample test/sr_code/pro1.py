import glob
import sys

w_data = 'C:/Users/reddy/Desktop/python/Coding test/sample test/w_data/*.txt'
y_data = 'C:/Users/reddy/Desktop/python/Coding test/sample test/y_data/*.txt'

files = glob.glob(w_data)
l=[]
l1=[]
l2=[]

for file in files:
	data = open(file, 'r').readlines()
	
	for i in data:
		j=i.split()
		if int(j[1]) != 0 and int(j[2]) != 0 and int(j[3]) == -9999:
			l.append(j)
	l2.append(len(l))
	l.clear()
	
for file in files:
	l1.append(file.split('/')[-1].split('.')[0])
l1.sort()



l3=list(zip(l1,l2))
print(l3, len(l3))



problem1_output = 'C:/Users/reddy/Desktop/python/Coding test/sample test/answer/MissingPrcpData.out'


sys.stdout = open(problem1_output, 'w')
print(l3)
sys.stdout.close()


		
	







