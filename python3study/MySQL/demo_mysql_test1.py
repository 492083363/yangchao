#!/bin/python
#输出所有数据库列表

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    passwd="abc@123"
)
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
    
