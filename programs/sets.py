'''
set:unordered collection of distinct(unique) elements
unordered so u can't indexing or slicing .
mutable:set
immutable:frozen set
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

'''
#create and add elements to sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
x=set()
x.add(1)
x.add(2)
print(x)   #o/p:{1,2}  like dictionary with only keys
print(type(x))  #<class 'set'>
#we can't add sets with same elements
x.add(1)
print(x)     #o/p:{1,2}  

#sets advantage:remove duplicate elements
l = [1,1,2,2,3,4,5,6,1,1]
s=set(l)
print(s)     #o/p:{1, 2, 3, 4, 5, 6}

a = set('abracadabra')
b = set('alacazam')
print(a-b)                #{'r', 'd', 'b'} :letters in a but not in b
print(a | b)             #{'b', 'r', 'm', 'l', 'd', 'z', 'a', 'c'}:letters in either a or b
print(a & b)              #{'c', 'a'}:letters in both a and b
print(a ^ b)          #{'b', 'r', 'm', 'l', 'd', 'z'}:letters in a or b but not both

#methods
#1.clear()
cities = {"Stuttgart", "Konstanz", "Freiburg"}
cities.clear()
print(cities)        #set()
#2.copy()
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
print(cities_backup)               #{'St. Gallen', 'Winterthur', 'Schaffhausen'}



#list comprehensiom
a={y for y in 'abracadabra' if y not in 'abc'}
print(a)                #{'r', 'd'}

#ex1
print(set("my name is Eric and Eric is my name".split()))   #o/p: {'and', 'is', 'name', 'Eric', 'my'}       

