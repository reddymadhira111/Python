def digit_sum():
	n=input('enter the no:')
	sum=0
	l=list(n)
	print(l)
	for i in l:
		sum=sum+int(i)
	return sum
print(digit_sum())

