'''
initial integer number in the first line;
one or more lines describing operations, in form sign value where sign is either + or * and value is an integer;
last line in the same form, but with sign % instead and number by which the result should be divided to get the remainder.
Answer should give remainder of the result of all operations applied sequentially (starting with initial number) divided by the last number.


'''
#i did not get the proper ans to the question
#http://www.codeabbey.com/index/task_view/modular-calculator
s='''87
+ 246
* 7
+ 18
* 61
+ 684
+ 4827
* 8492
+ 10
* 4430
+ 725
* 4060
* 68
* 115
* 9
* 491
+ 27
* 15
* 339
+ 28
+ 985
+ 778
+ 962
+ 6840
+ 86
* 3910
* 8525
* 16
+ 7530
* 13
* 9
+ 452
+ 207
+ 17
+ 5
+ 265
+ 151
+ 7
+ 577
+ 91
+ 54
* 760
* 43
* 73
+ 8
* 404
* 133
+ 22
+ 8
* 1966
+ 719
* 34
+ 84
% 3536'''
l1=[]
l2=[]
l3=[]
l4=[]
l=s.split('\n')
for i in l:
	m=i.split(' ')
	l1.append(m)
#print(l1)
for j in l1:
	for k in j:
		l2.append(k)
print(l2)
sum=0
c=0
for x in range(1,len(l2)):
	l2.insert(x*3,sum)
print(l2)

for x in range(0,len(l2),3):
	if l2[x+1]=='*':
		sum=(int(l2[x]) * int(l2[x+2]))
		l2[x+3]=sum
		l3.append(sum)
	elif l2[x+1]=='+':
		sum=(int(l2[x]) + int(l2[x+2]))
		l2[x+3]=sum
		l3.append(sum)
	elif l2[x+1]=='%':
		sum=(sum % int(l2[x+2]))
		l3.append(sum)
		break

#print(l3)
print(l3[-1])


