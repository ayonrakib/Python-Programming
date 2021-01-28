import mysql.connector as mysql
import json

class TransactionHistory():
    def __init__(self):
        self.mydb = mysql.connect(
            host="localhost",
            user="root",
            passwd="Hahaha01670",
            auth_plugin='mysql_native_password',
            database = "inventorymanagement"
)
        self.myCursor = self.mydb.cursor(buffered=True)
    def __str__(self):
        pass
    
    # print TransactionHistory table
    # input: none
    # return: none
    def printTransactionHistoryTable(self):
        self.myCursor = self.mydb.cursor()
        