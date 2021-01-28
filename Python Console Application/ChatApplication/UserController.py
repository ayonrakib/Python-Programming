from User import User
import mysql.connector as mysql
import json

# class
class UserController():
    def __init__(self, connection):
        self.connection = connection
        pass


    def __str__(self):
        pass

    # convert user object into list
    # input: resultSet
    # return: list
    # method:
    #   if type(resultSet) != list:
    #       raise exception
    #   if resultSet != []:
    #       for row in resultSet:
    #           user = User(row[0], row[1])
    #           userObjectList.append(user)
    #       return userObjectList
    #   return None
    def convertResultSetIntoList(self, resultSet):
        if str(type(resultSet)) != "<class 'list'>":
            raise Exception("Resut set has to be a list.")
        userObjectList = []
        if resultSet != []:
            for row in resultSet:
                user = User(row[0], row[1])
                userObjectList.append(user)
            return userObjectList
        return None

    # find user by id
    # input: id
    # return: object
    # method:
    #   create cursor
    #   select * from user where id = id
    #   if resultSet != []:
    #       name = resultSet[1]
    #       user = User(id, name)   
    #       return user
    #   return None
    def findById(self, id):
        if not isinstance(id, int):
            raise Exception("Id has to be integer.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM User where id = %s;",(id,))
        resultSet = self.myCursor.fetchone()
        if resultSet != []:
            name = resultSet[1]
            user = User(id, name)
            return user
        return None


    # find user name by id
    # input: id
    # return: name string if found, none if not
    # method:
    #   select * from user where id = id
    #   if resultset is not []:
    #       user = User(resultset[0], resultset[1])
    #       return user.getName()
    #   return None
    def findUserNameById(self, id):
        if not isinstance(id, int):
            raise Exception("User id has to be integer.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROm User WHERE id = %s;",(id,))
        resultset = self.myCursor.fetchone()
        if resultset != []:
            user = User(resultset[0], resultset[1])
            return user.getName()
        return None


    # add user
    # input: name
    # return: user object
    # method:
    #   create cursor
    #   insert into user where name = name
    #   commit
    #   resultSet = lastrowid
    #   if resultSet is not None:
    #       user = User(resultset[0], resultset[1])
    #       return user
    #   return None
    def addUser(self, name):
        if not isinstance(name, str):
            raise Exception("User name should be string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("INSERT INTO User (name) VALUES(%s);",(name,))
        self.connection.commit()
        id = self.myCursor.lastrowid
        self.myCursor.close()
        userName = self.findUserNameById(id)
        user = User(id, userName)
        return user


    # find all users with name
    # input: name
    # return: list of object if found, else none
    # method:
    #   create cursor
    #   select name from user where name = name
    #   resultSet = fetchall
    #   if resultSet != []:
    #       return resultSet
    #   return None
    def findAllUsersWithName(self, name):
        userObjectList = []
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM User WHERE name = %s;",(name,))
        resultSet = self.myCursor.fetchall()
        if resultSet != []:
            userObjectList = self.convertResultSetIntoList(resultSet)
            return userObjectList
        return None


    # def find all users where name starts with ayon
    # input: name
    # return: list of object if found, else none
    # method:
    #   create cursor
    #   select name from user where name like name%
    #   resultSet = fetchall
    #   if resultSet != []:
    #       return resultSet
    #   return None
    def findAllUsersWhoseNameStartsWithName(self, name):
        userObjectList = []
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM User WHERE name LIKE %s %s;",(name,"%"))
        resultSet = self.myCursor.fetchall()
        if resultSet != []:
            userObjectList = self.convertResultSetIntoList(resultSet)
            return userObjectList
        return None


    # def find all users where name ends with ayon
    # input: name
    # return: list of object if found, else none
    # method:
    #   create cursor
    #   select name from user where name like %name
    #   resultSet = fetchall
    #   if resultSet != []:
    #       return resultSet
    #   return None
    def findAllUsersWhoseNameEndsWithName(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM User WHERE name LIKE %s %s;",("%", name))
        resultSet = self.myCursor.fetchall()
        if resultSet != []:
            userObjectList = self.convertResultSetIntoList(resultSet)
            return userObjectList
        return None


    # find all users whose name contains ayon
    # input: name
    # return: list of object if found, else none
    # method:
    #   create cursor
    #   select name from user where name like %name
    #   resultSet = fetchall
    #   if resultSet != []:
    #       return resultSet
    #   return None
    def findAllUsersWhoseContainsName(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT * FROM User WHERE name LIKE %s %s %s;",("%", name, "%"))
        resultSet = self.myCursor.fetchall()
        if resultSet != []:
            userObjectList = self.convertResultSetIntoList(resultSet)
            return userObjectList
        return None


    # update user
    # input: name
    # return: object of modified user
    # method:
    #   create cursor
    #   modify user
    #   commit
    #   cursor close
    #   find by id
    #   return object user if found
    #   return None if not
    def updateUser(self, id, name):
        if not isinstance(name, str):
            raise Exception("The users new name has to be a string.")
        if not isinstance(id, int):
            raise Exception("The users id has to be an integer.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("UPDATE User SET name = %s WHERE id = %s;",(name, id))
        self.connection.commit()
        foundUser = self.findById(id)
        self.myCursor.close()
        return foundUser