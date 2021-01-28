import mysql.connector as mysql
import json, hashlib, binascii, peewee
from model.User import User
from library.DatabaseConnection import DatabaseConnection
import peewee, os


class UserController():
    def hashPassword(self, password):
        encodedPassword = hashlib.sha512(password.encode('utf-16',errors='strict'))
        hashedPassword = encodedPassword.hexdigest()
        return hashedPassword


    def getUserWithEmail(self, email):
        return User.get(User.email == email)


    def getUserSalt(self, email):
        return (User.get(User.email == email)).getSalt()


    def createCurrentUserSessionCookie(self, email):
        currentSessionCookie = str(os.urandom(20))
        self.updateCurrentUserSessionCookie(email, currentSessionCookie)
        return currentSessionCookie


    def getCurrentUserSessionCookie(self, email):
        return (User.get(User.email == email)).getCurrentSessionCookie()


    def updateCurrentUserSessionCookie(self, email, currentSessionCookie):
        user = (User.update({User.currentSessionCookie : currentSessionCookie}).where(User.email == email))
        user.execute()


    def getUserId(self, email):
        return (User.get(User.email == email)).getUserId()
    # method authenticate
    # input: email, pass
    # return: true if authenticated, false if not
    # method:
    #   try korbo input email diye salt porte db theke
    #   DoesNotExist error throw korle false return
    #   password hobe usersalt + password er hash
    #   db er email read korbo -> peewee call diye return object er getemail method call
    #   db er pass read korbo -> peewee te email er sathe match kore call kore return object er getpass method call
    #   jodi inputemail == dbemail and inputpass == dbpass hoy:
    #       true
    #   noile false
    def authenticate(self, email, password):
        try:
            userSalt = self.getUserSalt(email)
        except peewee.DoesNotExist:
            return False
        password = self.hashPassword(userSalt + password)
        databaseUserEmail = (User.get(User.email == email)).getEmail()
        databaseUserPassword = (User.get(User.email == email)).getPassword()
        if email == databaseUserEmail and password == databaseUserPassword:
            return True
        return False