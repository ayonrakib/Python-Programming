from MessageController import MessageController
from Message import Message
import mysql.connector as mysql
import json


connect = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hahaha01670",
    auth_plugin='mysql_native_password',
    database = "Chat"
)


testMessageController = MessageController(connect)
# testMessageController.sendMessage(5,7,"June 3 2020 Seventh Message")
# testMessageController.findConversationBetweenSenderAndReceiver(7,5)
# print(testMessageController.findMessageById(3))
print(testMessageController.updateMessage(14, "June 3 2020 Fourth Message"))