from library.DatabaseConnection import DatabaseConnection
from model.User import User
from controller.UserController import UserController
from model.Friends import Friends
from model.GameTable import GameTable
from model.MatchTable import MatchTable
import os


databaseConnection = DatabaseConnection.getConnection()
userController = UserController()

# jokhon table banabo, create_tables function er input hobe list of Class objects
# databaseConnection.create_tables([User, Friends, GameTable, MatchTable])
# salt = str(os.urandom(20))
# currentSession = str(os.urandom(20))

# user1 = User.create(email = 'ayon@gmail.com', firstName = "Rakib", lastName = "Ayon", salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user1.save()

# user2 = User.create(email = 'eva@gmail.com', firstName = "Fahmida", lastName = "Mahjabin", salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user2.save()

# user3 = User.create(email = 'golam@gmail.com', firstName = "Golam", lastName = "Muktadir",salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user3.save()

# user4 = User.create(email = 'saad@gmail.com', firstName = "Saad", lastName = "Manzur",salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
# user4.save()