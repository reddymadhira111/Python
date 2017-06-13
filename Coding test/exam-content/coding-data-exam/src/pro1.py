import glob
import sys

wx_data = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/wx_data/*.txt'
yld_data = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/yld_data/*.txt'

files = glob.glob(wx_data)
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
print(len(l))
print(len(l2))

l3=list(zip(l1,l2))
print(l3, len(l3))



problem1_output = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers/MissingPrcpData.out'


sys.stdout = open(problem1_output, 'w')
print(l3)
sys.stdout.close()


		
	







