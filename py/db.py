
import mysql.connector as c
 
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "guna",
    database = "mano"
)
cursor = mydb.cursor()
#cursor.execute("create table guna(name varchar(15),roll bigint(10),dept varchar(3),year int(1))")
#cursor.execute("desc guna")
'''q="insert into guna(name,roll,dept,year) values(%s,%s,%s,%s)"
v=[("inba",'14','it','2'),("avi",'18','mech','2')]
cursor.execute(q,v)
print(cursor.rowcount,'row updated')
'''
#cursor.execute("delete from guna where roll = 10")
#cursor.execute("drop table std")
#print("table droped scussfully")
cursor.execute("select * from guna order by roll limit 2")
x=cursor.fetchall()
for i in x:
    print (i)
mydb.commit()
mydb.close()