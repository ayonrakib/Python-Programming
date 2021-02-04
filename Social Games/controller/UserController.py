import mysql.connector as mysql
import json, hashlib, binascii, peewee
from model.User import User
from model.Friend import Friend
from library.DatabaseConnection import DatabaseConnection
import peewee, os
import logging
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

class UserController():
    # def __init__(self):
    #     self.databaseConnection = DatabaseConnection.getConnection()
    def getUserSalt(self, email):
        return User.get(User.email == email).getSalt()


    def hashPassword(self, password, salt):
        if not isinstance(password, str):
            raise Exception("Password should be a string")
        password = salt + password
        encodedPassword = hashlib.sha512(password.encode('utf-16',errors='strict'))
        hashedPassword = encodedPassword.hexdigest()
        return hashedPassword


    def authenticateUser(self, email, password):
        if not isinstance(email, str):
            raise Exception("email has to be string")
        if not isinstance(password, str):
            raise Exception("password has to be str.")
        userSalt = self.getUserSalt(email)
        password = self.hashPassword(password, userSalt)
        try:
            if User.get(User.email == email) and User.get(User.password == password):
                return True
        except:
            return False

# user jei data pathay sob string, so email str kina check dorkar nai.
    def findUserByEmail(self, email):
        # if not isinstance(email, str):
        #     raise Exception("Email is not a string")
# bivinno exception khaite paare: db down, busy, user paay nai, fail korse db te.
# user related kaaj gula show korbo, baki sob log korbo.
        try: 
            if User.get(User.email == email):
                return "User found"
        except peewee.DoesNotExist:
            return "User Not found"


    def createUserFromRegistrationForm(self, email, password, firstName, lastName):
        salt = str(os.urandom(20))
        currentSession = str(os.urandom(20))
        user = User.create(email = email, firstName = firstName, lastName = lastName, password = self.hashPassword(password, salt), salt = salt, currentSession = currentSession)
        return user


    # findUsersWithEmail
    # input: friendName, sessionid
    # return: friends list except logged in user
    # method:
    #   1. userModels hobe User table er sob user jader email e friendName substring thake
    #   2. curentUser hobe jei user er currentSession= sessionId
    #   3. users
    #   4. userNameAndEmail dic with keys name and email
    #   4. userModels er sob user er jonno:
    #       1. jodi user.email and currentUser.email soman na hoy:
    #           1. fullName = user.firstName + " " + user.lastName
    #           2. userNameAndEmail name key er value fullname
    #           3. userNameAndEmail email key er value user.email
    #           4. users e append userNameAndEmail
    #   5. return users
    def findUsersWithEmail(self, friendName, currentSession):
        userModels = User.select().where(User.email.contains(friendName))
        currentUser = User.get(User.currentSession == currentSession)
        users = [currentUser.email]
        for user in userModels:
            if user.email != currentUser.email:
                userNameAndEmail = {"name": "", "email": ""}
                fullName = user.firstName + " " + user.lastName
                userNameAndEmail["name"] = fullName
                userNameAndEmail["email"] = user.email
                users.append(userNameAndEmail)
        return users


    # for user in userModes:
    # 1. user = eva@gmail.com object
    #   1. if user.email != currentUser.email:
    #   2. if 'eva@gmail.com' != currentUser.email:
    #   3. if 'eva@gmail.com' != 'ayon@gmail.com':
    #   4. if true:
    #       1. fullName = user.firstName + " " + user.lastName
    #       2. fullName = "Fahmida" + " " + user.lastName
    #       3. fullName = "Fahmida" + " " + "Mahjabin"
    #       4. fullName = "Fahmida Mahjabin"
    #       5. userNameAndEmail["name"] = fullName
    #       6. userNameAndEmail["name"] = "Fahmida Mahjabin"
    #       7. x12345["name"] = "Fahmida Mahjabin"
    #       8. userNameAndEmail["email"] = email
    #       9. userNameAndEmail["email"] = "eva@gmail.com"
    #       10. x12345["email"] = "eva@gmail.com"
    #       10. userNameAndEmail = {"name": "Fahmida Mahjabin", "email" : "eva@gmail.com"}
    #       11. users.append(userNameAndEmail)
    #       12. users.append(x12345)
    #       12. users = [x12345]
    # 2. user = golam@gmail.com object
    #   1. if user.email != currentUser.email:
    #   2. if 'golam@gmail.com' != currentUser.email:
    #   3. if 'golam@gmail.com' != 'ayon@gmail.com':
    #   4. if true:
    #       1. fullName = user.firstName + " " + user.lastName
    #       2. fullName = "Golam" + " " + user.lastName
    #       3. fullName = "Golam" + " " + "Muktadir"
    #       4. fullName = "Golam Muktadir"
    #       5. userNameAndEmail["name"] = fullName
    #       6. userNameAndEmail["name"] = "Golam Muktadir"
    #       7. x12345["name"] = "Golam Muktadir"
    #       7. userNameAndEmail["email"] = email
    #       8. userNameAndEmail["email"] = "golam@gmail.com"
    #       10. x12345["email"] = "golam@gmail.com"
    #       9. userNameAndEmail = {"name": "Golam Muktadir", "email" : "golam@gmail.com"}
    #       10. users.append(userNameAndEmail)
    #       12. users.append(x12345)
    #       11. users = [x12345, x12345]

    # for user in users:
    #   print(user)

    # loop1:
    #   1. user = x12345
    #   2. print(user)
    #   3. print(x12345)
    #   4. print({"name": "Golam Muktadir", "email" : "golam@gmail.com"})



    # getUser
    # input: sessionid
    # return: found user object
    # method:
    #   return User.get(User.currentSession == currentSession)
    def getUser(self, currentSession):
        return User.get(User.currentSession == currentSession)


    def addFriend(self, currentUserEmail, userToBeAdded):
        currentUser = User.get(User.email == currentUserEmail)
        requestedFriend = User.get(User.email == userToBeAdded)
        friendRequest = Friend.create(user = currentUser.id, friend = requestedFriend.id, status = "requested")
        friendRequest.save()
        return ""


    def getPendingRequests(self, currentSession):
        currentUser = User.get(User.currentSession == currentSession)
        
# userController = UserController()
# print(userController.authenticateUser("rakib@gmail.com","password"))
# databaseConnection.create_tables([User])

# create 2 users
# user1 = User(email = "ayon@gmail.com", password = userController.hashPassword("password"))
# print(user1.save())
# user2 = User(email = "golam@gmail.com", password = userController.hashPassword("password"))
# print(user2.save())

# emails are unique, so this user will throw errors
#   user3 = User(email = "golam@gmail.com", password = user.hashPassword("password"))
#   print(user3.save())

# update user email field
#   user1 = User.get(User.id == 1)
#   user1.email = "ayon@gmail.com"
#   print(user1.save())

# update user password field with hash
#   user1 = User.get(User.id == 1)
#   user1.password = user.hashPassword("password")
#   print(user1.save())

# update current session
#   user1 = User.get(User.id == 1)
#   user1.currentSession = ""
