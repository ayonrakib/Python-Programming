import mysql.connector as mysql
import json
import Item
class ItemController():
    def __init__(self, connection):
        self.connection = connection
    def __str__(self):
        pass

    # print item table
    # input: nothing
    # return: nothing, only print item table
    # method:
    #   cursor execute of select * from iem table
    def printItemTable(self):
        self.myCursor = self.connection.cursor(buffered=True)
        self.myCursor.execute("SELECT * FROM Item;")
        self.connection.commit()
        resultTable = self.myCursor.fetchall()
        print("The item table is: ")
        for row in resultTable:
            print(row)
        self.myCursor.close()

    # delete item
    # input: name
    # return: nothing
    # method:
    #   cursor
    #   execute delete query
    #   cursoe close
    def deleteItem(self, name):
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("DELETE FROM Item where name = %s;",(name,))
        self.connection.commit()
        self.myCursor.close()

    # check if record exist in item table
    # input: record
    # return: boolean
    # method:
    #   result table fetch all
    #   if exist, return true
    #   else, return False
    def checkIfRecordExistsInItemTable(self,record):
        self.myCursor = self.connection.cursor(buffered=True)
        self.myCursor.execute("SELECT * FROM item;")
        self.connection.commit()
        resultTable = self.myCursor.fetchall()
        for row in resultTable:
            if record in row:
                return True
        return False

    def addItem(self, itemName):
        if not isinstance(itemName, str):
            raise Exception("item Name has to be a string.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("INSERT INTO Item(name) VALUES (%s)", (itemName,))
        print(self.myCursor.rowcount, " row was inserted.")
        self.connection.commit()
        id = self.myCursor.lastrowid
        foundItem = self.findItembyId(id)
        self.myCursor.close()
        return foundItem

    # find item by id
    def findItembyId(self, id):
        if not isinstance(id, int):
            raise Exception("Id must be an integer.")
        self.myCursor = self.connection.cursor(buffered=True)
        self.myCursor.execute("SELECT * FROM Item WHERE id = %s;",(id,))
        resultSet = self.myCursor.fetchone()
        # print(resultSet[0], resultSet[1])
        id = resultSet[0]
        name = resultSet[1]
        foundItem = Item.Item(name, id)
        return foundItem
    # update item
    # input: self
    # return: nothing, jump to another method which modifies userName/userId accordig to input
    # method:
    #   print: what do you want to update?
    #       1. userName in String
    #       2. userId in int
    #   select any option as input and then ask for necessary input
    #   jump to other method

    def updateItem(self):
        # update name of existing Item
        # input: self, existing Item, new Item
        # method:
        #   if existing Item type not string: exception
        #   if new Item not string: exception
        #   cursor
        #   modify query
        #   commit
        #   cursor close
        def updateNameOfItemByComparingName(self, nameOfExistingItem, nameOfNewItem):
            self.myCursor = self.connection.cursor()
            self.myCursor.execute("update Item set name = %s where name = %s;",(nameOfNewItem, nameOfExistingItem))
            self.connection.commit()
            self.myCursor.close()

        def updateNameOfItemByComparingId(self, idOfExistingItem, nameOfNewItem):
            self.myCursor = self.connection.cursor()
            self.myCursor.execute("update Item set name = %s where id = %s;",(nameOfNewItem, idOfExistingItem))
            self.connection.commit()
            self.myCursor.close()

    # jotokkhon na porjonto 1/2 input, loop
    # erpore option select korle kar sathe compare korbo sheitao select kore oi method e jaite hobe.
        while(True):
            nameOfNewItem = input("Please write the new name of the Item that you want to update into: ")
            while(True):
                selectOption = input("""Please select how you want to check the item name to modify:
1. Find with Item name
2. Find with Item id \n""")
                if selectOption == '1':
                    nameOfExistingItem = input("Please write the existing name of the Item that you want to update from: ")
                    if not self.checkIfRecordExistsInItemTable(nameOfExistingItem):
                        raise Exception("Existing Item name does not exist in the Item table.")
                    updateNameOfItemByComparingName(self, nameOfExistingItem, nameOfNewItem)
                    break
                elif selectOption == '2':
                    idOfExistingItem = int(input("Please write the existing id of the Item that you want to update from: "))
                    if not self.checkIfRecordExistsInItemTable(idOfExistingItem):
                        raise Exception("Existing Item id does not exist in the Item table.")
                    updateNameOfItemByComparingId(self, idOfExistingItem, nameOfNewItem)
                    break
                else:
                    print("Wrong input!")
            break

    # update item
    # input: self
    # return: nothing, jump to another method which modifies userName/userId accordig to input
    # method:
    #   print: what do you want to update?
    #       1. userName in String
    #       2. userId in int
    #   select any option as input and then ask for necessary input
    #   jump to other method
