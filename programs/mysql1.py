import pymysql


client = pymysql.connect(host='127.0.0.1', user='root', password='madhira', db='db1')
cursor = client.cursor()
query = 'INSERT INTO empinfo(id,Name,Surname,age) values(6,"phani","k",26);'
cursor.execute(query)
data=cursor.fetchall()
print(data)
client.close()

		
