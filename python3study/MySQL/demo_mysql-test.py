#!/bin/python
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abc@123"
)
print(mydb)

