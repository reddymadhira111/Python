import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='madhira', db='db1')

a = conn.cursor()
sql = 'INSERT INTO empinfo(id,Name,Surname,age) VALUES(7,"raghu","r",23);'
#sql = 'INSERT INTO empinfo(id,Name,Surname,age) values(7,"raghu","r",23);'
a.execute(sql)
countrow = a.execute(sql)
print('No of rows: ', countrow)
data = a.fetchall()
print(data)
