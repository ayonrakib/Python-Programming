# hash table with linear probing
# class hash table
# constructor: empty table, tablesize
class HashTable():
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.table = []
        self.createEmptyTable()


    def __str__(self):
        return f"This is a hash table with linear probing."


    # create empty table
    # input: self
    # method:
    #   table size porjonto:
    #       table e append korbo (none, none)
    def createEmptyTable(self):
        for count in range(self.tableSize):
            self.table.append((None, None))
    

    # get index
    # input: self, key
    # return: index
    # method:
    #    return key mod table size
    def getIndex(self, key):
        return key % self.tableSize


    # add element
    # input: self, key, value
    # return: true if added, false if not
    # method:
    #   index hobe key mod table size
    #   jodi table[index][0] None hoy:
    #       table[index] e (key,value) boshabo
    #       true
    #   currentindex theke tablesize er ek kom iterate:
    #       jodi table[currentindex][0] None hoy:
    #           table[index] e append korbo key value tuple
    #           return True
    #   0 theke currentindex porjonto iterate:
    #           jodi table[currentindex][0] None hoy:
    #           table[index] e append korbo key value tuple
    #           return True 
    #   false
# INDEX GET TA FUNCTION E CONVERT KORTE HOBE
    def addElement(self, key, value):
        index = self.getIndex(key)
        if self.table[index][0] is None:
            self.table[index] = ((key, value))
            return True
        for currentIndex in range(index, self.tableSize):
            if self.table[currentIndex][0] is None:
                self.table[currentIndex] = ((key, value))
                return True
        for currentIndex in range(0, index):
            if self.table[currentIndex][0] is None:
                self.table[currentIndex] = ((key, value))
                return True
        return False


    # update element
    # input: key, value
    # return: true if updated, false if not
    # method:
    #   get index with key
    #   if table[index][0] is None:
    #       false
    #   table[index] = key value tuple
    #   true
    # linear probing er problem hoilo, key soman nao hoite paare. so key check korte hobe, noile fail case.
    def updateElement(self, key, value):
        index = self.getIndex(key)
        if self.table[index][0] is None:
            return False
        self.table[index] = ((key, value))
        return True  


    # delete hok, update hok, dui khetre value important na, key important karon key hocche unique. so key check kortei hobe dui case e.
    # delete element
    # input: self, key, value
    # return: true if deleted, false if not
    # method:
    #   getindex from key
    #   if table[index][0] key er soman na hoy othoba table[index][1] value er soman na hoy:
    #       false
    #   table[index] = empty tuple
    #   true
    def deleteElement(self, key, value):
        index = self.getIndex(key)
        if self.table[index][0] != key and self.table[index][1] != value:
            return False
        self.table[index] = (())
        return True


    # find element
    # input: self, key
    # return: value if found, false if not
    # method:
    #   get index from key
    #   return table[index][1]
    # same issue. key check korte hobe.
    def findElement(self, key):
        index  = self.getIndex(key)
        return self.table[index][1]


    # get all keys
    # input: self
    # return: list of keys
    # method:
    #   

    # get all values
    

hashTable = HashTable(3)
print(hashTable.addElement(0,1))
print(hashTable.addElement(1,1))
print(hashTable.addElement(3,1))

# [(0,1),(1,2),(2,3)]


# [[],[],[]]

# key = 0, value =1
# key = 3, value = 9

# [[(0,1)],[],[]]
# [[(0,1),(3,9)],[],[]]