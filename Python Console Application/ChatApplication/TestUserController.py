from User import User
from UserController import UserController
import mysql.connector as mysql
import json


connection = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hahaha01670",
    auth_plugin='mysql_native_password',
    database = "Chat"
)

userController = UserController(connection)

# print(userController.findUserNameById(5))

# print(userController.addUser("aminebensabeur"))

# print(userController.findAllUsersWithName("ayon"))

# print(userController.findAllUsersWhoseNameStartsWithName("ayon"))

# print(userController.findAllUsersWhoseNameEndsWithName("ayon"))

# print(userController.findAllUsersWhoseContainsName("ayon"))

print(userController.updateUser(2, "Hasan"))