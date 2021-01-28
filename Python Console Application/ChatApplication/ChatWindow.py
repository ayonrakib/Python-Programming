from UserController import UserController
from User import User
from MessageController import MessageController
import mysql.connector as mysql
import json

class ChatWindow():
    def __init__(self):
        connect = mysql.connect(
            host="localhost",
            user="root",
            passwd="Hahaha01670",
            auth_plugin='mysql_native_password',
            database = "chat"
)
        self.connect = connect


    def __str__(self):
        pass


    # start application
    # input: self
    # return: nothing, so pass
    # senderid input nibo
    # testusercontrollerobject
    # senderid khujbo object er vitore
    # na paile exception
    # select a user to send a message
    # input receiver id
    # find receiver id in db
    # if not found, throw exception
    # please send a message
    # input message
    # jotokkhon na message return objectpai:
    #   write message
    def startApplication(self):
        while(True):
            senderId = input('Please enter your id: ')
            testUserController = UserController(self.connect)
            foundSenderId = testUserController.findUserById(senderId)
            if foundSenderId is None:
                print("The user id that you provided does not exist.")
                continue
            break
        print("\nHere is the current user list: ")
        print(testUserController.findAllUserIdExceptSenderId(senderId))
        while(True):
            receiverId = input("\nSelect a user to send your message to: ")
            foundReceiverId = testUserController.findUserById(receiverId)
            if foundReceiverId is None:
                print("The receiver id that you provided is wrong!")
                continue
            break
        testMessageController= MessageController(self.connect)
        while(True): 
            message = input("Please write your message down: ")
            foundMessage = testMessageController.sendMessage(receiverId, senderId, message)
            if foundMessage is not None:
                print(foundMessage)
            option = input("""Would you like to write another message to the same user? 
            Press 1 to write new message, any other button to quit.\n""")
            if option == "1":
                continue
            break

application = ChatWindow()
application.startApplication()