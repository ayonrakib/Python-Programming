import peewee
from library.DatabaseConnection import DatabaseConnection


class User(peewee.Model):
    id = peewee.AutoField()
    email = peewee.CharField(unique=True)
    password = peewee.CharField()
    salt = peewee.CharField()
    currentSessionCookie = peewee.CharField()
    class Meta:
        database = DatabaseConnection.getConnection()
    

    def __str__(self):
        return f"The email address is {self.email}"


    def getEmail(self):
        return self.email


    def setEmail(self, email):
        self.email = email


    def getSalt(self):
        return self.salt
        

    def setSalt(self, salt):
        self.salt = salt


    def getPassword(self):
        return self.password


    def getCurrentSessionCookie(self):
        return self.currentSessionCookie


    def setCurrentSessionCookie(self, currentSessionCookie):
        self.currentSessionCookie = currentSessionCookie


    def getUserId(self):
        return self.id