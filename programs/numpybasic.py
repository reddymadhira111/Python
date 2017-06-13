import numpy as np
#Create a list and convert it to a numpy array
l=[1,2,3]
x= np.array([1,2,3])
print(x)
#Use the shape method to find the dimensions of the array. (rows, columns)
m=np.array([[7, 8, 9], [10, 11, 12]])
print(m.shape)
#arange returns evenly spaced values within a given interval.
n=np.arrange(0,30,2)
print(n)
#reshape returns an array with the same data with a new shape.
n=n.reshape(3,5)
print(n)
#linspace returns evenly spaced numbers over a specified interval.
o=np.linspace(0,4,9) #return 9 evenly spaced values from 0 to 4
print(o)
#ones returns a new array of given shape and type, filled with ones.
np.ones((3,2))
#zeros returns a new array of given shape and type, filled with zeros.
np.zeros((2,3))

#eye returns a 2-D array with ones on the diagonal and zeros elsewhere
np.eye(3)
#diag extracts a diagonal or constructs a diagonal array.
np.diag(y)

#Repeat elements of an array using repeat.
np.repeat([1,2,3],3)
#Use vstack to stack arrays in sequence vertically (row wise)
np.vstack([p,2*p])
#Use hstack to stack arrays in sequence horizontally (column wise).
np.hstack([p,2*p])
print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]

x.dot(y) # dot product  1*4 + 2*5 + 3*6
#Use .T to get the transpose.
print(z.T)

#Use .dtype to see the data type of the elements in the array.
z.dtype
#Use .astype to cast to a specific type.
z = z.astype('f')
print(z.dtype)

#argmax and argmin return the index of the maximum and minimum values in the array.
a.argmax()
a.argmin()

#indexing/slicing
s = np.arange(13)**2

'''
Copying Data
Be careful with copying and modifying arrays in NumPy!
r2 is a slice of r'''
r2 = r[:3,:3]
print(r2)