from Message import Message
from User import User
from UserController import UserController
import mysql.connector as mysql
import json

class MessageController():
    def __init__(self, connection):
        self.connection = connection
        pass


    def __str__(self):
        pass


    # find message by id
    # input: id
    # return: message object if valid, otherwise None
    # method:
    #   create cursor
    #   select all messages with id
    #   fetch the first row
    #   if found:
    #       create message object from Message Model Class
    #       return message object
    #   else:
    #       return Null
    def findMessageById(self, id):
        if not isinstance(id, int):
            raise Exception("Id has to be an integer.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT receiverId, senderId, message FROM Message WHERE id = %s;",(id,))
        foundMessage = self.myCursor.fetchone()
        if foundMessage is not None:
            message = Message(foundMessage[0], foundMessage[1], foundMessage[2])
            return message
        return None


    # send message
    # input: receiver id, sender id, message
    # return: return of the object of Message model class
    # method:
    #   create cursor
    #   insert into Message table
    #   commit
    #   find all conversation by selecting that sender id and receiver id
    #   save the search tuple in resultSet
    #   testUserController = UserController(connect)
    #   if resultSet != []:
    #       for chat in resultSet:
    #           receiverId = chat[0]
    #           senderId = chat[1]
    #           message = chat[2]
    #           print(f"{senderName} to {receiverName}: {message}.\n")
    #   return None
    def sendMessage(self, receiverId, senderId, message):
        self.myCursor = self.connection.cursor()
        userController = UserController(self.connection)
        self.myCursor.execute("INSERT INTO Message(receiverId, senderId, message) VALUES(%s, %s, %s);",(receiverId, senderId, message))
        self.connection.commit()
        self.myCursor.execute("SELECT * from message where (receiverId = %s and senderId = %s) or (receiverId = %s and senderId = %s) ORDER BY id;",(receiverId,senderId,senderId,receiverId))
        resultSet = self.myCursor.fetchall()
        if resultSet != []:
            for chat in resultSet:
                receiver = userController.findById(chat[0])
                sender = userController.findById(chat[1])
                receiverName = receiver.getName()
                senderName = sender.getName()
                conversation = senderName + " to " + receiverName + ": " + chat[3]
                print(conversation)
                conversation= ''
                # receiverName = testUserController.findUserById(chat[0]).getName()
                # senderName = testUserController.findUserById(chat[1]).getName()
                # print(f"{senderName} to {receiverName}: {message.getMessage()}.\n")
        return None



    # find two way message between sender and receiver
    # input: self, receiverid, senderid
    # return: if found, tuple. else, None
    # method:
    #   create cursor
    #   SELECT message from message where (receiverId = 7 and senderId = 5) or (receiverId = 5 and senderId = 7);
    #   fetchall
    #   if not null:
    #       receiver object banabo
    #       sender object banabo
    #       receiver name banabo from receiver object
    #       sender name banabo from sender object
    #       message nibo from 2nd index of chat
    #       string banabo
    #       print string
    #       string = ''
    #   return None
    def findConversationBetweenSenderAndReceiver(self, receiverId, senderId):
        # userController = UserController(self.connection)
        # receiver = userController.findUserById(receiverId)
        # sender = userController.findUserById(senderId)
        userController = UserController(self.connection)
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT receiverId, senderId, message  from message where (receiverId = %s and senderId = %s) or (receiverId = %s and senderId = %s) ORDER BY id;",(receiverId,senderId,senderId,receiverId))
        resultSet = self.myCursor.fetchall()
        if resultSet != []:
            for chat in resultSet:
                receiver = userController.findById(chat[0])
                sender = userController.findById(chat[1])
                receiverName = receiver.getName()
                senderName = sender.getName()
                message = receiverName + " to " + senderName + ": " + chat[2]
                print(message)
                message = ""
        return None


    # delete message
    # input: receiverid, senderid, messagenumber
    # return: the updated conversation
    # method:
    #   find all the conversations with all the messages as tuples
    #   find the message number
    #   iterate until the message number and keep adding all until that number
    #       skip that message
    #   add all messages after those
    #   show the newly created tuple
    def deleteMessage(self, receiverId, senderId, messageNumber):
        if not isinstance(receiverId, int):
            raise Exception("Receiver id has to be integer.")
        if not isinstance(senderId, int):
            raise Exception("Sender Id has to integer.")
        if messageNumber < 0:
            raise Exception("message number has to be positive.")
        if not isinstance(messageNumber, int):
            raise Exception("message number has to be integer.")
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("SELECT receiverId, senderId, message  from message where (receiverId = %s and senderId = %s) or (receiverId = %s and senderId = %s) ORDER BY id;",(receiverId,senderId,senderId,receiverId))
        resultSet = self.myCursor.fetchall()
        if messageNumber > len(resultSet):
            raise Exception("message number cannot be greater than the length of conversation.")
        for message in resultSet:
            count += 1
            if count == messageNumber:
                continue
            newConversation += message
        return newConversation


    # update message
    # input: id, newmessage
    # return: tuple of conversation with updated message
    # method:
    #   check if id is int
    #   check if newmessage is string
    #   create cursor
    #   update message by id
    #   commit
    #   close cursor
    #   print updated messages
    def updateMessage(self, id, newMessage):
        self.myCursor = self.connection.cursor()
        self.myCursor.execute("UPDATE message SET message = %s where id = %s;",(newMessage, id))
        self.connection.commit()
        self.myCursor.execute("SELECT * FROM message WHERE id = %s and isDeleted = 0;",(id,))
        resultSet = self.myCursor.fetchone()
        self.connection.close()
        print(resultSet)