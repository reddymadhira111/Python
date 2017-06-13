s='''738365 595092 928544 6312 51 3227 5149279 19 151832 50 1160380 294190 7246541 2334 975686943 500026957 5320889 4 493904 8 4 69 316928686 55572931 5657 2 71'''

l1=[]
l2=[]
l3=[]
l=s.split(' ')
print(l)
for i in l:
	j=int(i)
	l1.append(j)
print(l1)
sum=0
limit=10000007
for x in l1:
	sum=(sum+x)*113
	print(sum)
	if sum > limit:
		sum=sum%limit
		print(sum)
print(sum)

	