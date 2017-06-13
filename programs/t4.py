a=[0,0,1,2,3,4]
value=0

def counta(a,value):
	c=0
	for i in a:
		if i==value:
			c+=1
		return c
	print(c)
counta(a,0)
