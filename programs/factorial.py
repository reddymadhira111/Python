def factorial(n):
    if n>0:
    	r=1
    	for x in range(n+1):
    		if x==0:
    			pass
    		else:
    		    r=r*x
    	return r
    else:
    	print('0 factorial:',1)
n=int(input('enter n:'))
print(factorial(n))