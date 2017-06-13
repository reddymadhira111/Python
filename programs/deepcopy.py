
'''color1=['red','blue']
color2=color1
print(id(color1),id(color2))
color2[1]='green'
print(color2,color1)
'''

lst1=[1,2,3,[100,101]]
lst2=lst1
print(id(lst1),id(lst2))
print(lst1,lst2)
lst2.append('linga')
print(lst2,lst1)
lst2[3].append('linga reddy')
print(lst2,lst1)


from copy import deepcopy
lst1=[1,2,3,[100,101]]
lst2=deepcopy(lst1)
print(id(lst1),id(lst2))
print(lst1,lst2)
lst2.append('linga')
print(lst1,lst2)
print(id(lst1),id(lst2))
lst2[3].append('linga reddy')
print(lst1,lst2)
