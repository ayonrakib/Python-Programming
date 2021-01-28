import UserController
import mysql.connector as mysql
import json
import User

connect = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hahaha01670",
    auth_plugin='mysql_native_password',
    database = "inventorymanagement"
)
testUserController = UserController.UserController(connect)

print(testUserController.printUserTable())