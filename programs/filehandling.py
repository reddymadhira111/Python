'''



'''


file_ptr=open('demo.txt','r')
print(file_ptr.readlines())
print(file_ptr.readlines())   #[] becz the file already reads and the cursor is at the end
# Seek to the start of file (index 0)
file_ptr.seek(0)
for data in file_ptr.readlines():
	print(data)
file_ptr.close()

file1=open('demo1.txt')
print(file1)
file1.close()

file_ptr=open('demo.txt')
file_ptr.read()
file_ptr.readlines()
name=input('enter the filename:')
fobj=open(name)
print(fobj.read())
fobj.close()

with open('setup.py') as fobj:
	for line in fobj:
		print(line)
'''
file_ptr=open('demo.txt','a')
file_ptr.write('this is a new demo file')
file_ptr.write('to practice new file handling')
file_ptr.close()
import sys
if len(sys.argv) <3:
	print('wrong parameter')
	print('./copyfile.py file1 file2')
	sys.exit(1)
f1=open(sys.argv[1])
s=f1.read()
f1.close()
f2=open(sys.argv[2],'w')
f2.write(s)
f2.close()
'''