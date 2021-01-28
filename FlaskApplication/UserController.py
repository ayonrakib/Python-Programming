from User import User
import mysql.connector as mysql
import json, hashlib, binascii

# class
class UserController():
    def __init__(self, connection):
        self.connection = connection
        pass


    def __str__(self):
        pass


    # find user by id
    # input: id
    # return: user object
    # method:
    #   create cursor
    #   find user by id
    #   save result in resultSet
    #   if resultSet != []:
    #       name = resultSet[1]
    #       user = User(id, name)   
    #       return user
    #   return None
    def findUserById(self, id):
        if not isinstance(id, int):
            raise Exception("id has to be integer.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM userdetails WHERE id = %s;",(id,))
        resultSet = self.myCursor.fetchone()
        if resultSet != []:
            firstName = resultSet[1]
            lastName = resultSet[2]
            email = resultSet[3]
            password = resultSet[4]
            user = User(firstName, lastName, email, password)
            return user
        return None


    # add user
    # input: firstname, lastname, email, password
    # return: created user object
    # method:
    #   create cursor
    #   add user into table
    #   commit
    #   fetch last row id into result set
    #   if resultSet is not None:
    #       newUser = User(resultSet[1],resultSet[2],resultSet[3],resultSet[4])
    #       return newUser
    #   return None
    def addUser(self, firstName, lastName, email, password):
        password = self.hashPassword(password)
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("INSERT INTO userdetails(firstName, lastName, email, password) VALUES(%s, %s, %s, %s);",(firstName, lastName, email, password))
        self.connection.commit()
        id = self.myCursor.lastrowid
        user = self.findUserById(id)
        return user


    # getAllUserId
    # input: None
    # return: All user id in string format
    # method:
    #   create cursor
    #   execute search for all user id in resultset
    #   string to add all user id
    #   1. email : user id
    #   return string
    def getAllUserId(self):
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT email, Id FROM userdetails;")
        resultSet = self.myCursor.fetchall()
        return resultSet


    # hash password method
    # input: password
    # return: hashed password
    # method:
    #   if password is not string, raise exception
    #   take the password and use hashlib library and encode.
    #   then use hexdigest method.
    def hashPassword(self, password):
        if not isinstance(password, str):
            raise Exception("Password should be a string.")
        encodedPassword = hashlib.sha512(password.encode('utf-16',errors='strict'))
        hashedPassword = encodedPassword.hexdigest()
        return hashedPassword


    # find user by email and password
    # input: email, password
    # method:
    #   check if email and password is string
    #   create cursor
    #   select user with email and password
    #   save result set 
    #   count result set rows
    #   if count == 1:
    #       return True
    #   return False
    def authenticateUser(self, email, password):
        if not isinstance(email, str):
            raise Exception("email has to be a string.")
        if not isinstance(password, str):
            raise Exception("Password has to be a string.")
        hashedPassword = self.hashPassword(password)
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM USERDETAILS WHERE EMAIL = %s AND PASSWORD = %s;",(email, hashedPassword))
        resultSet = self.myCursor.fetchall()
        count=0
        for row in resultSet:
            count += 1
        if count == 1:
            return True
        return False


    # get all user data from email
    # input: email
    # return: string
    # method:
    #   create cursor
    #   select * from table where email = email
    #   save in resultset
    #   return resultSet
    def getAllUserData(self, email):
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM USERDETAILS WHERE email = %s;",(email,))
        resultSet = self.myCursor.fetchone()
        return resultSet


    # change full name
    # input: string
    # return: nothing
    # method:
    #   create cursor
    #   if both names are empty, modify nothing
    #   if first name is empty: modify last name
    #   if last name is empty, modify first name
    def changeUserName(self, firstName, lastName, email):
        self.myCursor = self.connection.cursor()
        print(firstName, lastName, email)
        if firstName == "" and lastName == "":
            pass
        elif firstName == "" and lastName != "":
            self.myCursor.execute("UPDATE userdetails SET lastName = %s WHERE email = %s;",(lastName, email))
        elif firstName != "" and lastName == "":
            self.myCursor.execute("UPDATE userdetails SET firstName = %s WHERE email = %s;",(firstName, email))
        elif firstName != "" and lastName != "":
            self.myCursor.execute("UPDATE userdetails SET firstName = %s, lastName = %s WHERE email = %s;",(firstName,lastName, email))
        self.connection.commit()


    # get description
    # input: email
    # return: string
    # method:
    #   create cursor
    #   select description from email
    #   return resultset 0th index as string
    def getDescription(self, email):
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT description FROM userdetails WHERE email = %s;",(email,))
        resultSet = self.myCursor.fetchone()
        return resultSet[0]

# connection = mysql.connect(
#     host="localhost",
#     user="root",
#     passwd="Hahaha01670",
#     auth_plugin='mysql_native_password',
#     database = "userregistration"
# )

# userController = UserController(connection)
# print(userController.getDescription('ayon@gmail.com'))