# hashtable dsa
# a list of data, arranged as key value pair
# we need to define the length of list, so that will be a constructor
# we can search any pair with key.
# the pair will be indexed according to the key
# [(0,2),(3,4)]
# here, (0,2) -> 0 % 2 = 0, so the pair (0,2) is saved on the 0th index.
# here, (3,4) -> 3 % 2 = 1, so the pair (3,4) is saved on the 1st index.
# now, what happens if there are multiple pairs which has same index?
# two ways:
#   1. just put in the next available spot
#   2. modify the design. in stead of pairs as elements, put lists as elements.
from _typeshed import Self


class HashTable():
    def __init__(self, length) -> None:
        self.length = length
        self.table = []

    def __str__(self) -> str:
        return f"The length of the hash table is: {self.length}"

    def createTable(self):
        for length in range(self.length):
            self.table.append((None , None))

    def insert(self, key, value):
        if(type(key) != int):
            raise Exception("Not int!")
        # index = key mod table size
        # 