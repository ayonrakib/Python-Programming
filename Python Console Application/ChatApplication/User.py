# class User
# constructor: name, id
# method: getname, setname
class User():
    def __init__(self,id, name):
        self.id = id
        self.name= name
        pass


    def __str__(self):
        return f"The name of the user is {self.name} and the id is {self.id}."


    def getName(self):
        return self.name


    def setName(self, name):
        self.name = name
        pass