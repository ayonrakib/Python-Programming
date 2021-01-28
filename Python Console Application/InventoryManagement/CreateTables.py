import mysql.connector as mysql
import json

mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hahaha01670",
    auth_plugin='mysql_native_password',
    database = "inventorymanagement"
)

myCursor = mydb.cursor()
myCursor.execute("SHOW TABLES;")

for table in myCursor:
    print(table)

# assignment: foreign key, priamry key er tutorial
# a python class: for each table. that class will have some methods like add, update, delete.