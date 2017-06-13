def StringContainer():
	#def class string
	class String:
		def __init__(self):
			self.content_string = ''
		def len(self):
			return len(self.content_string)
	#return class definition
	return String

#create the class definition
container_class=StringContainer()
print(container_class)
#create an instance of class
wrapped_string=container_class()
print(wrapped_string)
wrapped_string.content_string='linga reddy'
print(wrapped_string.len())
