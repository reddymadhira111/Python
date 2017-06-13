'''
#volume of a sphere=4/3 pi r3
class Mathb(object):
    def __init__(self,r):
        self.r=r
    def vol():
        r=int(input('enter radius:'))
        v=(4/3)*(3.14)*(r**3)
        return v
m=Mathb.vol()
print(m)
'''
'''
#no is in the range or no
num=int(input('enter the no:'))
low=int(input('enter the no:'))
high=int(input('enter the no:'))
def ran_check(num,low,high):
	if (num >= low and num <= high):
		print('in the range')
	else:
		print('not in range')
	
ran_check(num,low,high)
'''
'''
i=input('enter a string:')
def check():
    count=0
    c=0
    for item in i:
        if ord(item)>=65 and ord(item)<=90:
            count+=1
        elif ord(item)>= 97 and ord(item)<=122:
        	c+=1
    print('no of upper',count)
    print('no of lower',c)
print(check())
'''
'''
def unique():
    l=[1,2.3,35,43,1,12,2]
    for item in l:
        if l.count(item)>1:
            l.remove(item)
    print('unique list:',l)

m=unique()
print(m)
'''
'''
def multiply():
	l=[1,2,4,5]
	s=1
	for i in l:
		s=s*i
	return s
m=multiply()
print(m)
'''
'''
def palindrome():
	s=input('enter a string:')
	if s==s[::-1]:
		print('palindrome',s)
	else:
		print('not palindrome')
m=palindrome()
print(m)
'''
'''
import string
def ispangram():
    str1=input('enter a string:')
    str1.lower()
    str2='abcdefghijklmnopqrstuvwxyz'
    a={}
    for s in str2:
        a[s]=0 
    for i in str1.lower():
    	if i in str2:
    		a[i]+=1
    v=a.values()
    for v1 in v:
        if v1<1:
    	    return False
    return True
m=ispangram()
print(m)
'''