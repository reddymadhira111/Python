s='''4 61743 46882 36 2 120928859 2276 126406022 223418 272138182 299 28902155 15 333824 13 2 18 376664857 219101 412 6 264 1078903 10866 104705 57062055 2715861 3255575 82747 6140 7124 136 0 169'''

l2=[]
l3=[]

l1=s.split( )
print(l1)

def digit_sum(n):
	sum=0
	l=list(n)
	if len(l)>1:
		for x in range(len(l)):
			sum=sum+((x+1)*int(l[x]))
		l2.append(sum)
	else:
		l2.append(int(n))
for y in l1:
	(digit_sum(y))
print(l2)