#!/bin/python
#连接指定库

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    passwd="abc@123",
    database="my_db"
)
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
    
