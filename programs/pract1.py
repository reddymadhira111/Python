'''
class Circle(object):
    pi=3.14
    def _init_(self,radius):
        self.radius=radius
    def area(self):
	    return self.radius*self.radius*Circle.pi
    def setRadius(self,radius):
	    self.radius=radius
    def getRadius(self):
	    return self.radius
c=Circle()

c.setRadius(2)
print('Radius is:',c.getRadius())
print('Area is:',c.area())
'''
'''
class Animal(object):
    def __init__(self):
        print('Animal created')
    def whoAmI(self):
        print('Animal')
    def eat(self):
        print('eating')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')
    def whoAmI(self):
        print('Dog')
    def bark(self):
        print('bow bow')

d= Dog()

d.whoAmI()
d.eat()
d.bark()
'''
class Book(object):
    def __init__(self,title,author,pages):
        print('A book is created')
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return 'title:%s,author:%s,pages:%s' %(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print('book is destroyed')
book= Book('python', 'jose',200)
print(book)
print(len(book))
del book