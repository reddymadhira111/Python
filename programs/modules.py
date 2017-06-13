'''
def:A module is a logical way to physically organize and distinguish related pieces of Python code into
individual files. A module can contain executable code, functions, classes, or any and all of the above
Modules are a means to organize
Python code, and packages help you organize modules
namespace is an
individual set of mappings from names to objects.
1.which is a list of modules, sys.modules is a dictionary where the
keys are the module names with their physical location as the values.
file:///D|/
2.import preference
Python Standard Library modules
 Python third party modules
● Application-specific modules

'''
#import a module:import module_name


#to call a module fn or access variable
'''
module.function()
module.variable
'''
#ex1
import sys

sys.stdout.write('hello world\n')
print(sys.platform, sys.version)
#win32 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)]

#set system path to user created module
import sys
import mymodule
'''
Traceback (innermost last):
File "<stdin>", line 1, in ?
ImportError: No module named mymodule
'''
sys.path.append('/home/wesc/py/lib')
sys.path
'''
['', '/usr/local/lib/python2.x/', '/usr/local/lib/
python2.x/plat-sunos5', '/usr/local/lib/python2.x/
lib-tk', '/usr/local/lib/python2.x/lib-dynload', '/usr/
local/lib/python2.x/site-packages','/home/wesc/py/lib']
'''
#import mymodule  :it will show no error
