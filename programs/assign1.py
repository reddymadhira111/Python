'''
value = input('enter a value:')
value=int(value)
print(value)
d = (100 - value)
d=int(d)
print(d)
m=100%value
m=int(m)
print(m)
'''
'''
v1=input('enter v1:')
v1=int(v1)
v2=input('enter v2:')
v2=int(v2)
sum=v1+v2
print(sum)
dif=v1-v2
print(dif)
'''

name=input('enter name:')
print(name)
print(len(name))
title=input('enter title:')
print(title)
print(len(title))
dl=int(len(name)-len(title))
print(dl)
if dl==2:
	print("congrats the difference is 2")