import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
mycursor.execute("create database if not exists test5")
mycursor.execute("create table if not exists test5.Student(roll int,name varchar(20) , Address varchar(20))")
mycursor.execute("insert into test5.Student values(1,'Nikhil','Taloja')")
mydb.commit()
mycursor.execute("select * from test5.Student")
for i in mycursor:
    print(i)

mydb.close()