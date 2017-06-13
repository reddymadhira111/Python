l=[]
for i in range(1,101):
    if (i%3==0 and i%5==0):
        i='FizzBuzz'
        l.append(i)
    elif i%5==0:
    	i='Buzz'
    	l.append(i)
    elif i%3==0:
        i='Fizz'
        l.append(i)
    else:
    	l.append(i)
print(l)