# class Item
# properties, getter, setter
# database column name: name, id
# so, methods:
#   getname, getid, setname, setid
# properties: self.name, self.id
class Item():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    # def __str__(self):
    #     return self
    # method: getname
    def getName(self):
        return self.name
    # method: getid, return id
    def getId(self):
        return self.id
    # method: setname, set name
    def setName(self, name):
        self.name = name
    # method: setid, set id
    def setId(self, id):
        self.id = id