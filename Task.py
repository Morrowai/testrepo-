#! /usr/bin/python3
# need first : pip install mysql-connector-python
x=input("Enter mysql password ")
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                             database='co',
                                             user='root',
                                             password=x)
cursor=connection.cursor()
cursor.execute("SELECT * FROM employees")
for employees_column in cursor:
        print(employees_column)