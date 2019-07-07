import pymysql
conn= pymysql.connect(host='localhost' ,user= 'root' , password='' ,db='testdb')
 
sql='SELECT*from`meter data`;'
a.excecute(sql)

countcoloumn = a.execute(sql)
print("no. of cols ;",countcoloumn)
data = a.fetchone()
print(data)
