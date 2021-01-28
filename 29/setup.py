from library.DatabaseConnection import DatabaseConnection
from model.User import User
from model.GameTable import GameTable
from controller.UserController import UserController
import os

userController = UserController()

# pc er random byte generator
# userSalt = os.urandom(20)

# databaseConnection = DatabaseConnection.getConnection()


# databaseConnection.create_tables([User,GameTable])


# ayon = User.create(email = "ayon@gmail.com",salt = str(userSalt), password = userController.hashPassword(str(userSalt) + "password"), currentSessionCookie = userController.createCurrentUserSessionCookie())
# print(ayon)

# golam = User.create(email = "golam@gmail.com",salt = str(userSalt), password = userController.hashPassword(str(userSalt) + "password"), currentSessionCookie = userController.createCurrentUserSessionCookie())
# print(golam)

# eva = User.create(email = "eva@gmail.com",salt = str(userSalt), password = userController.hashPassword(str(userSalt) + "password"), currentSessionCookie = userController.createCurrentUserSessionCookie())
# print(eva)

# saad = User.create(email = "saad@gmail.com",salt = str(userSalt), password = userController.hashPassword(str(userSalt) + "password"), currentSessionCookie = userController.createCurrentUserSessionCookie())
# print(saad)

# try:
#     print(userController.findUserWithEmail('ayon@gmail.com'))
# except:
#     print("user is unavailable")

# print(userController.getUserSalt('ayon@gmail.com'))

# print(userController.authenticate("ayon@gmail.com", "password"))

# print(userController.getCurrentUserSessionCookie('ayon@gmail.com'))

print(userController.deleteCurrentUserSessionCookie("saad@gmail.com"))