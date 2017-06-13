import math
import json
from pprint import pprint

with open('invoice.json') as data_file:    
    l = json.load(data_file)

pprint(l)
l1=[]
for i in l:
	j=i['Amount']
	l1.append(j)
print(l1)
sum=0
for x in l1:
	sum+=x

print(sum)

cb = sum * (0.05)
print('Cash back after 6 months:', cb)
Amount= input('Enter next month Amount:')
Amount = int(Amount) - cb
print('Next month payment is:', float(Amount) )
