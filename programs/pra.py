'''p=(3*24*3600)+(7*3600)+(20*60)+25
print(p)
p1=p/(24*3600)
p2=(p%(24*3600))/3600
p3=((p%(24*3600))%3600)/60
p4=((p%(24*3600))%3600)%60

print(int(p1),p2,p3,p4)
'''
'''
print ("%s and number %d!"%("python", 1))
string= "myworld"
print(string)
'''
def digit_sum(n):
	sum=0
	l=list(n)
	print(l)
	if len(l)>1:
		for x in range(len(l)):
			sum=sum+((x+1)*int(l[x]))
		return print(sum)
	else:
		return print(n)


digit_sum('61743')
