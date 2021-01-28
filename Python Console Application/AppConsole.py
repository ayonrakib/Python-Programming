import mysql.connector as mysql
import json
import UserController as User
import Item as Item
# inventory management
# use case: 
# 1. see product list
# 2. see product details after selecting that product
# 3. increase product number
# 4. decrease product number
# 5. insert new product into the existing list
# 6. remove product from existing list
# 7. modify product description
# 8. see which warehouse the product is held at
# 9. see the supplier of the product
# 10. product supplier contact
# 11. 

# class AppConsole():
# # constructor: connect to db and point to the db. create cursor also.
#     def __init__(self):
#         self.connection = mysql.connect(
#             host="localhost",
#             user="root",
#             passwd="Hahaha01670",
#             auth_plugin='mysql_native_password',
#             database = "inventorymanagement"
#         )
#         self.myCursor = self.connection.cursor(buffered=True)
#         self.userObject = User.User(self.connection)
#         self.itemObject = Item.Item(self.connection)

#     # print tables
#     def __str__(self):
#         pass    
#     # select operation
#     # input: nothing
#     # return: nothing
#     # method:
#     #   select which option to perform
#     #   call according method

#     # 

#     def selectOption(self):
#         option = input("""Please select an operation:
#         1. Add user
#         2. Update User
#         3. Delete User
#         4. print User Table
#         5. Add Item
#         6. Update Item
#         7. Delete Item
#         8. Print Item Table \n""")
#         while(True):
#             if option == '1':
#                 userName = input("Please insert the User Name: ")
#                 userId = input("Please insert the User Id: ")
#                 self.userObject.addUser(userName, userId)
#                 break
#             elif option == '2':
#                 self.userObject.updateUser()
#                 break
#             elif option == '3':
#                 self.userObject.deleteUser()
#             elif option == '4':
#                 self.userObject.printUserTable()

# # database = Database()
# # print(database)

# # database.printUserTable()
# # database.addUser()
# # database.printUserTable()

# # database.printItemTable()
# # database.updateItem()
# # database.printItemTable()

# # database.printUserTable()
# # database.deleteUser()
# # database.printUserTable()

# # print(database.checkIfRecordExistsInUserTable(10))