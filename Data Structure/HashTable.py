# hash table without linear probing
# input: list with tuples
# method:
#   list er length hobe table size
#   index variable banabo
#   list er proti ta tuple er jonno iterate:
#       index hobe element er 0th index mod tableSize
#       index > 0 hoile kemne boshabo?




# hash table with linear probing
# input: list with tuples
# method:
#   list er length hobe table size
#   index variable banabo
#   list er proti ta tuple er jonno iterate:
#       index hobe element er 0th index mod tableSize
# 


class HashTable():
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.table = []
        self.createEmptyTable()


    def __str__(self):
        return f"This is a hash table."
        


    # create empty table with the size of the table
    # input: table size
    # return: empty table
    # method:
    #   tablesize porjonto iterate:
    #       self.table e append korbo None, None er tuple
    #   return self tale


    def createEmptyTable(self):
        for length in range(self.tableSize):
            self.table.append((None, None))
        return self.table


    # add element
    # input: element to be added - a key value pair
    # return: updated table
    # method:
    #   index hobe key mod table size
    #   jodi table[index][0] None na hoy:
    #       False
    #   temporay tuple banabo key value pair diye
    #   table er index e boshabo oi tuple.
    #   True
# eivabe n order e search kora jabe na, hash function diye check korbo 
    def addElement(self, key, value):
        if key is not int:
            raise Exception("Key is not integer.")
        if key < 0:
            raise Exception("Key is negative.")
        if key is None:
            raise Exception("Key cannot be None.")
        index = key % self.tableSize
        if self.table[index][0] is not None:
            return False
        if self.table[index][0] == key:
            raise Exception("The key already exists.")
        temporayTuple = ((key, value))
        self.table[index] = temporayTuple
        print(self.table)
        return True


# test case 1: if key is not integer?
# hashTable = HashTable(3)
# print(hashTable.addElement('a',4))

# test case 2: if key is negative?
# hashTable = HashTable(3)
# print(hashTable.addElement(-1,5))

# test case 3: what if the key already exists?
# hashTable = HashTable(3)
# print(hashTable.addElement(3,2))
# print(hashTable.addElement(3,4))

# test case 4: if index is already full?
# hashTable = HashTable(3)
# print(hashTable.addElement(3,2))
# print(hashTable.addElement(0,4))

# test case 5: if key is None?
# hashTable = HashTable(3)
# print(hashTable.addElement(None,5))

# test case 6: if table is already full?
# print(hashTable.addElement(3,2))
# print(hashTable.addElement(2,4))
# print(hashTable.addElement(1,2))
# print(hashTable.addElement(6,4))

# user input e key dibe value dibe, kivabe ami algo khatabo sheita user janbe na, so tuple check kora jabe na
# iput validation charao aro onek case ase, jemon already index e element thakle ki hobe, full thakleki  hobe etc.

    # update element
    # input: key, value
    # return: true or false
    # method:
    #   index hobe key mod tablesize
    #   jodi table er index er 0th element none hoy:
    #       false
    #   tuple banabo with key and value pair
    #   table er index e boshabo tuple
    #   true
    def updateElement(self, key, value):
        if type(key) != int:
            raise Exception("Key has to be integer.")
        if key < 0:
            raise Exception('Key cannot be negative.')
        if key is None:
            raise Exception("Key cannot be None.")
        index = key % self.tableSize
        if self.table[index][0] is None:
            return False
        temporayTuple = ((key, value))
        self.table[index] = temporayTuple
        return True


# test case 1: if key is not integer?
# hashTable = HashTable(3)
# print(hashTable.addElement('a',4))

# test case 2: if key is negative?
# hashTable = HashTable(3)
# print(hashTable.addElement(-1,5))

# test case 3: if key is None?
# hashTable = HashTable(3)
# print(hashTable.addElement(None,5))

# same problem as add element


# for delete, i have to think from user POV>if return true, either key chilo na or delete hoise. false manei delete hoy nai.
    # delete element
    # input: key, value
    # output: true if the key is found and deleted. if not, false.
    # method:
    #   index hobe key mod tablesize
    #   jodi table er index er 0th element key er soman na hoy othoba 1st index valuer soman na hoy:
    #       false
    #   table er oth index hobe none none er tuple
    #   return true
    def deleteElement(self, key, value):
        if type(key) != int:
            raise Exception("Key is not integer.")
        index = key % self.tableSize
        if self.table[index][0] != key or self.table[index][1] != value:
            return False
        self.table[index] = ((None, None))
        return True

    # test case 1: if key is not int?

    # emptylist = []
    # for tuple in self.table:
    # for tuple in [(3, 2), (1, 2), (2, 2)]:
    #   loop 1: tuple = (3,2)
    #   1. if element[0] != tuple[0]:
    #   2. if 2 != tuple[0]:
    #   3. if 2 != 3:
    #   4. if True:
    #       1. emptylist.append(tuple)
    #       2. emptylist.append((3,2))
    #       3. emptylist = [(3,2)]
    #   loop 2: tuple = (1,2)
    #   1. if element[0] != tuple[0]:
    #   2. if 2 != tuple[0]:
    #   3. if 2 != 1:
    #   4. if True:
    #       1. emptylist.append(tuple)
    #       2. emptylist.append((1,2))
    #       3. emptylist = [(3,2),(1,2)]
hashTable = HashTable(3)
print(hashTable.addElement(3,2))
print(hashTable.addElement(2,4))
print(hashTable.addElement(1,2))
print(hashTable.addElement(6,4))