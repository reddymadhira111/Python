'''
1.print 
2.exec being statements,
3.integers using floor division
4."range()" returns a memory efficient iterable, not a list as in 2.x

'''
#1.print statement
#print 'linga'    #python 2 :Missing parentheses in call to 'print'
print('linga')   #python 3

#2.class declaration
class Linga:        #python 2.x:
	pass

class LingaRe(object):   #python 2.x & 3.x:
	pass
x=Linga()
y=LingaRe()
print(type(x))  #python 3.x:<class '__main__.Linga'> :it will print class
print(type(y))   #python 2.x:it will print instance:<type 'instance'>

'''
python3: drawbacks
1.slightly worse library support


python3: includes
1.NumPy, SciPy(for number crunching and scientific computing)
2.Django, Flask, CherryPy and Pyramid (for Web sites)
3.PIL (an image processing module) was superseded by its fork: Pillow, which supports Python 3.
4.cx_Freeze (for packaging applications with their dependencies)
5.py2exe (for packaging your application for Windows users)
6.OpenCV 3, (an open source computer vision and machine learning library) now supports Python 3 in versions 3.0 and later.
7.Requests, (an HTTP library for humans)
8.lxml, (a powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API)
9.BeautifulSoup4, (a screen-scraping library for parsing HTML and XML)
10.The IPython/Jupyter project for interactive computing fully supports Python 3.

only available in 3.x releases and won't be backported to the 2.x series:
1.strings are Unicode by default
2.clean Unicode/bytes separation
3.exception chaining
4.function annotations
5.syntax for keyword-only arguments
6.extended tuple unpacking
7.non-local variable declarations

'''