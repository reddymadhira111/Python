import math
f='35 348 217 531 106 575 41 570 578 357 170 167 377 241 524 508 157 152 56 182 189 417 80 51 272 62 340 68 65 391 550 350 138 166 280 212'
f1=list(f.split( ))
f2=[]
for j in f1:
	f2.append(int(j))
print(f2)
c=[]
for i in f2:
    c1=(i-32)*(5/9)
    c.append(round(c1))
for a in c:
    print(a,' ')