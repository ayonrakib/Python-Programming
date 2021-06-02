# FindHuman class
# import humans ist class
# constructor: a list,whose elements are 100 lists of human objects 
# those nested lists are indexed according to age, so 100 lists
# str: none
from HumanList import HumanList

class FindHuman():
    def __init__(self) -> None:
        self.humans = self.createHumans()


    def __str__(self) -> str:
        pass


    # createHumans
    # input: self
    # return: list, contains 100 lists of human objects-each list index is the age of human objects
    # method:
    #   1. humansList empty list
    #   2. 100 bar iterate korbo:
    #       1. humansList e append empty list
    #   3. return humansList
    def createHumans(self):
        humansList = []
        for number in range(100):
            humansList.append([])
        return humansList


    # addHumansWithAge
    # input: self, human object
    # return: true if added, false if not
    # method:
    #   1. index hobe human object er age mod 100
    #   2. self.humans er index tomo list e append human obj
    #   3. return true
    def addHumansithAge(self, human):
        index = human.age % 100
        self.humans[index].append(human)
        return True


    # searchHumanWithAge
    # input: self, age
    # return: list of humans with the age
    # method:
    #   1. index hobe age mod 100
    #   2. return korbo self.humans er index tomo list
    def searchHumansWithAge(self, age):
        index = age % 100
        return self.humans[index]


findHumans = FindHuman()
human1 = HumanList("Ayon",30,210)
human2 = HumanList("Ayon",30,210)
findHumans.addHumansithAge(human1)
findHumans.addHumansithAge(human2)
print(findHumans.searchHumansWithAge(30))