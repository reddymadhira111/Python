'''
lambda expressions allow us to create "anonymous" functions
we can quickly make ad-hoc functions without needing to properly define a function using def.
Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs
Lambda functions can be used wherever function objects are required.
'''
def square(num):
	return num**2
s=square(4)
print(s)          #16
s=lambda no:no**2
print(s(4))       #16
even=lambda n:n%2==0
print('even no:',even(4))   #even no: True
f=lambda s:s[1]
print('1 index:',f('linga'))   #1 index: i
rs=lambda rst:rst[::-1]
print(rs('linga'))      #agnil
an=lambda a:a/7
print(an(s(4)))       #2.2857142857142856
 