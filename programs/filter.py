'''
The function filter(function, list) offers a convenient way
to filter out all the elements of an iterable, for which the function returns True.


'''
def even(n):
	if n %2 == 0:
		return True

x=filter(even, range(10))
print(list(x))

x=filter(lambda n:n%2==0, range(10,20))
print(list(x))