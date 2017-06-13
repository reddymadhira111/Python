import math
import operator
import json
from pprint import pprint

with open('coordinates.json') as data_file:    
    l = json.load(data_file)

pprint(l)

l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
for i in l:
  j=i['value']
  l1=j.split(',')
  l2.append(int(l1[0]))
  l2.append(int(l1[1]))

for i in l:
  j=i['id']
  l5.append(j)


def distance():
  x=int(input("enetr x: "))
  y=int(input('enter y: '))
  
  d=0
  for i in range(0,52,2):
    d=math.sqrt(((int(l2[i])-x)**2)+ ((int(l2[i+1])-y)**2))
    l3.append(round(d,3))
distance()
#print(l3)
for i in range(26):
  d= dict(zip(l5,l3))

print(d)
d1=sorted(d.items(), key=lambda d: d[1])

print(d1)




