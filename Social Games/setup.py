from library.DatabaseConnection import DatabaseConnection
from model.User import User
from controller.UserController import UserController
from model.Friends import Friends
import os


databaseConnection = DatabaseConnection.getConnection()
userController = UserController()

# jokhon table banabo, create_tables function er input hobe list of Class objects
# databaseConnection.create_tables([User, Friends])
# salt = str(os.urandom(20))
# currentSession = str(os.urandom(20))

# user1 = User.create(email = 'ayon@gmail.com',salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user1.save()

# user2 = User.create(email = 'eva@gmail.com',salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user2.save()

# user3 = User.create(email = 'golam@gmail.com',salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user3.save()

# user4 = User.create(email = 'saad@gmail.com',salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user4.save()