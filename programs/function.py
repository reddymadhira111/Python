'''
functions allow us to not have to repeatedly write the same code again and again
functions are independent
function annotations:
Function annotations are completely optional metadata information about the types used by user-defined functions
Annotations are stored in the __annotations__ attribute of the function as a dictionary and
have no effect on any other part of the function.

'''

#create a function
def name_of_fn(arg1,arg2):
    return arg1+arg2
#ex1
def say_hello():
	print('hello')
say_hello()

#ex2
def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print ('not prime')
            break
    else: # If never mod zero, then prime
        print ('prime')
is_prime(2)

#ex on fn annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
f('spam')
#o/p:Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
#Arguments: spam eggs
