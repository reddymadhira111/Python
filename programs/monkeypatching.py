'''
Monkey patching is reopening the existing classes or methods in class at runtime and changing the behavior,
which should be used cautiously, or you should use it only when you really need to.
As Python is a dynamic programming language, Classes are mutable so you can reopen them and modify or even replace them.

'''
#monkey patching is dynamic modification of a class or a module at runtime
#ex1:
def safe_sqrt(num):
	#does not show error when num is negative
	if num < 0:
		return math.nan
	return math.original(num)

import math
math.original=math.sqrt()
math.sqrt=safe_sqrt