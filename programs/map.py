'''
map() is a function that takes in two arguments: a function and a sequence iterable. In the form: map(function, sequence)
map() applies the function to all the elements of the sequence
It returns a new list with the elements changed by function.
map() can be applied to more than one iterable. The iterables have to have the same length.
'''
#ex1
def fahrenheit(T):
	return (9.0/5)*T+32

def celsius(T):
	return (5.0/9)*(T-32)

temp=[0, 22.5, 40, 100]

F_temps=list(map(fahrenheit, temp))
print(F_temps)

C_temps=list(map(celsius, F_temps))
print(C_temps)

a=map(lambda x: (5.0/9)*(x-32), F_temps )
print(list(a))

a1=[1,2,3,4]
a2=[5,6,7,8]
a3=[9,10,11,12]
a4=map(lambda x,y,z:x+y+z, a1,a2,a3)
print(list(a4))

a5=map(chr, [66,53,0,94])     #trying to map a list into hex
print(list(a5))