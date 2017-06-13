import csv

#%precision 2

with open('mpg.csv') as csvfile:
	mpg = list(csvfile)

print(mpg[:3])
'''
csv.Dictreader has read in each row of our csv file as a dictionary. 



'''