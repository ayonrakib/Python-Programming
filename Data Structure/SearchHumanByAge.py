# HumanFinder class
# import humans ist class
# constructor: a list,whose elements are 100 lists of human objects 
# those nested lists are indexed according to age, so 100 lists
# str: none
from Human import Human
from CreateHumans import CreateHumans

class HumanFinder():
    def __init__(self) -> None:
        humans = CreateHumans()
        self.humans = humans.createHumans()


    def __str__(self) -> str:
        pass


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


humanFinder = HumanFinder()
human1 = Human("Ayon",30,210)
human2 = Human("Ayon",30,210)
humanFinder.addHumansithAge(human1)
humanFinder.addHumansithAge(human2)
print(humanFinder.searchHumansWithAge(30))