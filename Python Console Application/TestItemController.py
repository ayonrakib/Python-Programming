import ItemController
import mysql.connector as mysql
import json
import Item

connect = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hahaha01670",
    auth_plugin='mysql_native_password',
    database = "inventorymanagement"
)

testItemController = ItemController.ItemController(connect)
print(testItemController.deleteItem("pencil"))