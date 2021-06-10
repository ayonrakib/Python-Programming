# smart hash table
# difference with linear probing: eita faster karon proti ta index e list of tuples thakbe.
# faster karon proti ta index e iccha moton element rakha jabe.



# class hashtable
# constructor: self, tablesize
# method:
#   self tablseize
#   empty self table
#   call createemptytable
class HashTable():
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.table = []
        self.createEmptyTable()


    # str function
    # return string
    def __str__(self):
        return "This is a smart hash table."


    # create empty table
    # input: self
    # return: nothing
    # method:
    #   tablesize porjonto iterate:
    #       table e empty list append
    def createEmptyTable(self):
        for number in range(self.tableSize):
            self.table.append([])
    

    # get index hash function
    # input: key as integer
    # return: index as integer
    # method:
    #   return key mod tablesize
    def getIndexFromInteger(self, key):
        return key % self.tableSize


    # get index from character
    # input: string
    # return: key as integer
    # method:
    #   totalIntegerValue = 0
    #   key er proti ta character er jonno:
    #       totalIntegerValue += int value of character
    #   return int of totalIntegerValue mod tablesize
    def getIndexFromString(self, key):
        totalIntegerValue = 0
        for character in key:
            totalIntegerValue += ord(character)
        return totalIntegerValue % self.tableSize


    # get table
    # input: self
    # return: table
    # method:
    #   return table
    def getTable(self):
        return self.table


    # add element
    # input: key, value
    # return: true if added, false if not
    # method:
    #   get index from hash function
    #   table[index] e key value tuple hishebe add korbo
    #   return true
    def addElement(self, key, value):
        if type(key) is int:
            index = self.getIndexFromInteger(key)
        else:
            index = self.getIndexFromString(key)
        index = self.getIndexFromInteger(key)
        self.table[index].append((key,value))
        return True


    # delete
    # input: key, value
    # return: true if deleted, false if not
    # method:
    #   temporaryList = []
    #   get index from key
    #   table[index] er sob tuple er jonno:
    #       jodi tuple[0] key er soman na hoy:
    #           temporaryList e tuple append
    #   table[index] = temporaryList
    #   true
    def delete(self, key, value):
        temporaryList = []
        if type(key) is int:
            index = self.getIndexFromInteger(key)
        else:
            index = self.getIndexFromString(key)
        for tuple in self.table[index]:
            if tuple[0] != key:
                temporaryList.append(tuple)
        self.table[index] = temporaryList
        return True


    # update element
    # input: key, value
    # return: true if updated, false if key not found
    # method:
    #   get index from key
    #   table[index] er sob tuple er jonno:
    #       jodi tuple[0] key er soman hoy:
    #           tuple = key value pair
    #           true
    #   false
    def updateElement(self, key,value):
        if type(key) is int:
            index = self.getIndexFromInteger(key)
        else:
            index = self.getIndexFromString(key)
        for tuple in self.table[index]:
            if tuple[0] == key:
                tuple = ((key, value))
                return True
        return False


    # get pair
    # input: key
    # return: key value pair as tuple, false if none
    # method:
    #   get index from key
    #   table[index] er sob tuple er jonno:
    #       jodi tuple[0] key er soman hoy:
    #           return tuple
    #   return false
    def getPair(self, key):
        if type(key) is int:
            index = self.getIndexFromInteger(key)
        else:
            index = self.getIndexFromString(key)
        for tuple in self.table[index]:
            if tuple[0] == key:
                return tuple
        return False

    # get keys, values
    # get keys
    # input: self
    # return: list of keys
    # method:
    #   keys []
    #   table er sob keyValuePairs er jonno:
    #       keyValuePairs er sob keyValuePair er jonno:
    #           keys e append korbo keyValuePairs[0]
    #   return keys
    def getKeys(self):
        keys = []
        for keyValuePairs in self.table:
            for keyValuePair in keyValuePairs:
                keys.append(keyValuePair[0])
        return keys


    # get values
    # input: self
    # return: values as list
    # method:
    #   values []
    #   table er sob keyValuePairs er jonno:
    #       keyValuePairs er sob keyValuePair er jonno:
    #           values e append(keyValuePair[1])
    #   return values
    def getValues(self):
        values = []
        for keyValuePairs in self.table:
            for keyValuePair in keyValuePairs:
                values.append(keyValuePair[1])
        return values


if __name__ == "__main__":
    hashTable = HashTable(3)
    hashTable.addElement(0,1)
    hashTable.addElement(3,2)
    hashTable.addElement(1,3)
    hashTable.addElement(2,4)
    hashTable.addElement(5,7)
    print(hashTable.getTable())
    print(hashTable.getKeys())
    print(hashTable.getValues())