'''n=['a','b','c']
nc=n
nc[2]='h'
print(n,nc)
'''
'''
for i in range(3):
	print(i)
else:
	print('done')
'''	'''
n='python'
print(n[-1])
'''
'''
a=30
b=7
c=a/b
d=a//b
e=a%b
print(c,d,e)'''
'''
def wish(m):
	return lambda name: m.upper() + name

greet=wish('hbdy')
print(greet('joy'))
'''
'''
for i in range(1,10,2):
	print(i)
	'''
'''
x=3+2j
y=3-2j
z=x+y
print(z)
'''
'''
d=(x*10 for x in range(3))
for i in d:
	print(i)
for j in d:
	print(j)
'''
'''
l=['d','a','g','e','b']
l.sort()
print(l[:-3],l[:10],l[0:])
'''
'''
def wel(n):
	return 'wel'+n, 'gb'+n
wis=wel('joe')
print(wis)
'''
