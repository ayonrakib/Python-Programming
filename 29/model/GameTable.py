import peewee
from library.DatabaseConnection import DatabaseConnection
from model.User import User

class GameTable(peewee.Model):
    id = peewee.AutoField()
    firstPlayer = peewee.ForeignKeyField(User, to_field="id")
    secondPlayer = peewee.ForeignKeyField(User, to_field="id")
    thirdPlayer = peewee.ForeignKeyField(User, to_field="id")
    fourthPlayer = peewee.ForeignKeyField(User, to_field="id")
    time = peewee.TimeField()
    date = peewee.DateTimeField()
    class Meta:
        database = DatabaseConnection.getConnection()