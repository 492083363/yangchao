#!/bin/python
# 创建表

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd="abc@123",
    database="my_db"
)
mycursor = mydb.cursor()
#mycursor.execute ("CREATE TABLE sites (name VARCHAR(255),url VARCHAR(255))")
mycursor_tables = mycursor.execute("SHOW TABLES")
for x in mycursor_tables:
    print(x)
