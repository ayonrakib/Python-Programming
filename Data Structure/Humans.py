# ekta human class thakbe, name age property hobe.
# jeisob object banabo human class er, sheigula notun notun var e boshano jabe na, data structure diye save korte hobe.
# method likhte hobe jeno search er-name age weight wise

# class Human
# properties: name, age, weight
# methods: none
from HashTableSmart import HashTable
class Human():
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight


    def __str__(self) -> str:
        pass


# HumansList class
# properties: humans banabo HashTable class theke 100 input diye obj banaye 
# method: searchByName, searchByAge, searchByWeight
class HumanList():
    def __init__(self) -> None:
        self.humans = HashTable(100)


    def __str__(self) -> str:
        pass


    # searchByName
    # input: self, name
    # return: list of human objects whose name matches the given name
    # method:
    #   1. humansWithTargetName empty list
    #   2. self.humans er sokol human object er jonno:
    #       1. jodi human object er name string e input name string thake:
    #           1. humansWithTargetName e append current human object
    #   3. return humansWithTargetName


    # searchByAge
    # input: self, age
    # return: list of human objects whose age matches the input age
    # method:
    #   1. index hobe age mod 100
    #   2. return self.humans er indexth list