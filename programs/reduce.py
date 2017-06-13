'''
The function reduce(function, sequence) continually applies the function to the sequence. It then returns a single value.
steps:At first the first two elements of seq will be applied to function, i.e. func(s1,s2)
The list on which reduce() works looks now like this: [ function(s1, s2), s3, ... , sn ]
In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
The list looks like this now: [ function(function(s1, s2),s3), ... , sn ]
It continues like this until just one element is left and return this element as the result of reduce()


'''
#ex1
import functools
x=functools.reduce(lambda x1,x2:x1+x2,[1,2,3,4])
print(x)
#it is limited to associative values.so this is not present in python3
max=lambda a,b:a if (a>b) else b
y=functools.reduce(max,[1,2,34,7])
print(y)