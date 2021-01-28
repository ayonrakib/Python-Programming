import peewee
from library.DatabaseConnection import DatabaseConnection
from model.User import User

class Friends(peewee.Model):
    id = peewee.AutoField()
    userId = peewee.ForeignKeyField(User, to_field = 'id')
    friendId = peewee.ForeignKeyField(User, to_field = 'id')
    status = peewee.CharField()
    class Meta:
        database = DatabaseConnection.getConnection()