import pymysql
conn = pymysql.connect(host='localhost',user='root',password='',db='testdb')

a= conn.cursor()
sql = 'Select * from meter data'
num_of_rows = a.execute(sql)
print('number of rows' +str(num_of_rows))
data=a.fetchone()
print(data)
