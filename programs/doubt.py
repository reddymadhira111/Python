#doubt with the  outputs
names = "{1}, {2} and {0}".format('John', 'Bill', 'Sean')
print(names)

m='{1},{2} and {0}'.format('c','d','a')
print(m)

#doubt with the line 21,24 

 def StringContainer():
     # define a class
...     class String:
...         def __init__(self):
...             self.content_string = ""
...         def len(self):
...             return len(self.content_string)
...     # return the class definition
...     return String
...
>>> # create the class definition
... container_class = StringContainer()
>>>
>>> # create an instance of the class
... wrapped_string = container_class()
>>>
>>> # take it for a test drive
... wrapped_string.content_string = 'emu emissary'
>>> wrapped_string.len()
12

#doubt with the format

%precision 2
