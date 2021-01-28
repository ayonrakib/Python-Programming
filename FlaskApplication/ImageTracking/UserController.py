# from User import User
import mysql.connector as mysql
import hashlib, binascii, json, datetime, peewee

databaseConnection = peewee.MySQLDatabase("imagetracking",host="localhost",user="root",password="Hahaha01670")

class User(peewee.Model):
    id = peewee.AutoField()
    email = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = databaseConnection

class Pet(peewee.Model):
    id = peewee.AutoField()
    owner = peewee.ForeignKeyField(User,backref="pets")
    name = peewee.CharField()
    animalType = peewee.CharField()

    class Meta:
        database = databaseConnection

databaseConnection.connect()
# databaseConnection.create_tables([User, Pet])
# databaseConnection.create_tables([User])
# databaseConnection.create_tables([Pet])

# user1 = User(email = "ayon", userId = 10, password = "asd")
# user1.save()

# user2 = User(email = "ayon", userId = 10, password = "asd")
# print(user2.save())
# grandma = User.create(email = "grandma", userId = 12, password = "asd")
# print(grandma)

# grandma = User(email = "grandma", userId = 12, password = "asd")
# grandma.email = "afg"
# print(grandma.save())

# uncleBob = User(email="bob", userId = 30, password = "qwe")
# print(uncleBob.save())
# herb = User.create(email="herb", userId = 40, password = "qwer")
# bobKitty = Pet.create(owner = uncleBob, name = "Kitty", animalType = "cat")
# print(herb.save())
# print(bobKitty.save())

# uncleBob = User(email="bob", password = "asd")
# print(uncleBob.save())
# grandma = User.create(email = "grandma", password = "asd")
# print(grandma)
# herb = User.create(email="herb", password = "qwer")
# print(herb)

uncleBob = User.get(User.id == 2)
# bobKitty = Pet.create(owner = uncleBob, name = "Kitty", animalType = "cat")

herb = User.get(User.id == 3)
bobCat = Pet.get(Pet.id == 1)
bobDog = Pet.get(Pet.id == 3)

# bobPigeon = Pet.create(owner = uncleBob, name = "Pigeon", animalType = "bird")
# print(bobPigeon.save())

# bobPigeon = Pet.get(Pet.id == 4)
# bobPigeon.delete_instance()

# bobDog.owner = herb
# print(bobDog.save())

# for user in User.select():
#     print(user.email)

# query = (Pet.select(Pet,User).join(User).where(Pet.animalType=="cat"))
# for pet in query:
#     print(pet.name, pet.owner.email)

for pet in Pet.select().join(User).where(User.email == "herb"):
    print(pet.name)
