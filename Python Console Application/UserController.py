import mysql.connector as mysql
import json
import User as User

class UserController():
    def __init__(self, connection):
        self.connection = connection
    def __str__(self):
        pass

    # print user table
    # input: nothing
    # return: nothing, only print user table
    # method:
    #   cursor execute of select * from user table
    def printUserTable(self):
        self.myCursor = self.connection.cursor(buffered=True)
        self.myCursor.execute("SELECT * FROM User;")
        self.connection.commit()
        resultTable = self.myCursor.fetchall()
        print("The user table is: ")
        for row in resultTable:
            print(row)
        self.myCursor.close()
    
    # check if record exist in user table
    # input: record
    # return: boolean
    # method:
    #   result table fetch all
    #   if exist, return true
    #   else, return False
    def checkIfRecordExistsInUserTable(self,record):
        self.myCursor = self.connection.cursor(buffered=True)
        self.myCursor.execute("SELECT * FROM user;")
        self.connection.commit()
        resultTable = self.myCursor.fetchall()
        for row in resultTable:
            if record in row:
                return True
        return False
    
        # add user
    # parameter: table columns, so userName, userId
    # return: nothing
    # method:
    #   if userName is not string:
    #       throw exception
    #   if userId is not int:
    #       throw exception
    #   cursor execute for inserting into user column with parameter
    def addUser(self, name):
        if not isinstance(name, str):
            raise Exception("User Name has to be a string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute(f"INSERT INTO User(name) VALUES ('{name}');")
        print(self.myCursor.rowcount, " row was inserted.")
        self.connection.commit()
        id = self.myCursor.lastrowid
        self.myCursor.close()
        createdUser = self.findById(id)
        return createdUser

    # method: find by id
    # kaaj: id dibo, amake userObject return korbe db theke pull kore.
    # parameter: id
    # return: object akare return
    def findById(self, id):
        self.myCursor = self.connection.cursor()
        self.myCursor.execute(f"SELECT * FROM User WHERE id = '{id}';")
        resultSet = self.myCursor.fetchone()
        id = resultSet[0]
        name = resultSet[1]
        foundUser = User.User(name, id)
        return foundUser
    # delete user
    # input: self
    # return: nothing
    # method:
    # 1st e dekhabe kon record er against e delete korbe: name naki id
    # name hoile:
    #   delete user with that name
    # id hoile:
    #   delete user with that id

    def deleteUser(self):
        # check the user with name and delete with cursor commit
        def deleteUserComparingByName(self, nameOfExistingUser):
            self.myCursor = self.connection.cursor()
            self.myCursor.execute("delete from User where name = %s;",(nameOfExistingUser,))
            self.connection.commit()
            self.myCursor.close()
        # check the user with id and delete with cursor commit
        def deleteUserComparingById(self, idOfExistingUser):
            self.myCursor = self.connection.cursor()
            self.myCursor.execute("DELETE FROM User where id = %s;",(idOfExistingUser,))
            self.connection.commit()
            self.myCursor.close()
        while(True):
            select = input("""How do you want to delete the user?
1. With user name
2. With user id\n""")
            if select == '1':
                nameOfExistingUser = input("Please insert the name of the existing user which will be deleted: ")
                if not self.checkIfRecordExistsInUserTable(nameOfExistingUser):
                    raise Exception("Name of this user does not exist.")
                deleteUserComparingByName(self, nameOfExistingUser)
                break
            elif select == '2':
                idOfExistingUser = input("Please insert the id of the existing user which will be deleted: ")
                if not self.checkIfRecordExistsInUserTable(int(idOfExistingUser)):
                    raise Exception("Name of this user does not exist.")
                deleteUserComparingById(self, idOfExistingUser)
                break
            else:
                print("Wrong choice!")

    # update name of existing user
    # input: self, existing user, new user
    # method:
    #   if existing user type not string: exception
    #   if new user not string: exception
    #   cursor
    #   modify query
    #   commit
    #   cursor close
    def updateUserName(self):
        def updateNameOfUserByComparingName(self, nameOfExistingUser, nameOfNewUser):
            self.myCursor = self.connection.cursor()
            self.myCursor.execute("update User set name = %s where name = %s;",(nameOfNewUser, nameOfExistingUser))
            self.connection.commit()
            self.myCursor.close()

        def updateNameOfUserByComparingId(self, idOfExistingUser, nameOfNewUser):
            self.myCursor = self.connection.cursor()
            self.myCursor.execute("update User set name = %s where id = %s;",(nameOfNewUser, idOfExistingUser))
            self.connection.commit()
            self.myCursor.close()

        # jotokkhon na porjonto 1/2 input, loop
        # erpore option select korle kar sathe compare korbo sheitao select kore oi method e jaite hobe.
        while(True):
            nameOfNewUser = input("Please write the new name of the User that you want to update into: ")
            while(True):
                selectOption = input("""Please select how you want to check which User name to modify:
1. Compare with User name
2. Compare with User id \n""")
                if selectOption == '1':
                    nameOfExistingUser = input("Please write the existing name of the User that you want to update from: ")
                    if not self.checkIfRecordExistsInUserTable(nameOfExistingUser):
                        raise Exception("Existing User name does not exist in the User table.")
                    updateNameOfUserByComparingName(self, nameOfExistingUser, nameOfNewUser)
                    break
                elif selectOption == '2':
                    idOfExistingUser = int(input("Please write the existing id of the User that you want to update from: "))
                    if not self.checkIfRecordExistsInUserTable(idOfExistingUser):
                        raise Exception("Existing User id does not exist in the User table.")
                    updateNameOfUserByComparingId(self, idOfExistingUser, nameOfNewUser)
                    break
                else:
                    print("Wrong input!")
            break

    # add item
    # parameter: table columns, so itemName, itemId
    # return: nothing
    # method:
    #   if itemName is not string:
    #       throw exception
    #   if itemId is not int:
    #       throw exception
    #   cursor execute for inserting into user column with parameter