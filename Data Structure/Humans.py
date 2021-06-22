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


# HumanManagerWithAge class
# properties: humans banabo HashTable class theke 100 input diye obj banaye 
# method: searchByName, searchByAge, searchByWeight
class HumanList():
    def __init__(self) -> None:
        self.humans = HashTable(100)


    def __str__(self) -> str:
        return f"The human object is {self.humans.getTable()}"

    
    # addHuman
    # input: self, human object
    # return: true if added, false if not
    # method:
    #   1. index pabo object er getIndexFromInteger method theke with human er age as input
    #   2. self.humans er index e append korbo
    #   3. return self.humans
    def addHuman(self, human):
        # index = self.humans.getIndexFromInteger(human.age)
        # self.humans.getTable()[index].append(human)
        self.humans.addElement(human.age,human)
        return True


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
    #   1. return korbo humans obj er search method with input as human age
    def searchByAge(self, age):
        # if type(age) != "<class 'int'>":
        #     raise Exception("The input age has to be an integer.")
        return self.humans.search(age)


human1 = Human("Ayon",30,200)
human2 = Human("Rakib",30,200)
human3 = Human("Eva",40,200)

humans = HumanList()
humans.addHuman(human1)
humans.addHuman(human2)
humans.addHuman(human3)
print(humans)
print(humans.searchByAge(30))
print(humans.searchByAge(40))

# print(type(30) == "<class 'int'>")