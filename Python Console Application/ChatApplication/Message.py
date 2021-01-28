class Message():
    def __init__(self, receiverId, senderId, message):
        self.receiverId = receiverId
        self.senderId = senderId
        self.message = message
        pass


    def __str__(self):
        return f"The receiver id is {self.receiverId}, the sender id is {self.senderId} and the message is {self.message}."

    def getReceiverId(self):
        return self.receiverId


    def getSenderId(self):
        return self.senderId


    def getMessage(self):
        return self.message


    def setReceiverId(self, receiverId):
        self.receiverId = receiverId
        pass


    def setSenderId(self,senderId):
        self.senderId = senderId
        pass


    def setMessage(self, message):
        self.message = message
        pass

