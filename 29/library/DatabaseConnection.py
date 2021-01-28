import peewee, mysql.connector as mysql

class DatabaseConnection():
    existingDatabaseConnection = None
    @staticmethod
    def getConnection():
        if DatabaseConnection.existingDatabaseConnection is None:
            DatabaseConnection.existingDatabaseConnection = peewee.MySQLDatabase("twentynine", host = "localhost", user = "root", password = "Hahaha01670", port = 3306)
            DatabaseConnection.existingDatabaseConnection.connect()
            return DatabaseConnection.existingDatabaseConnection
        return DatabaseConnection.existingDatabaseConnection