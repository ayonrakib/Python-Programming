class Cat():
    def __init__(self):
        self.__legs = 4
        self.__tail = 1

    
    def getLegs(self):
        return self.__legs


    def increaseLeg(self):
        self.__legs += 1
        return self.__legs


    def __feed(self):
        return "The cat is eating"


    def petCat(self):
        return self.__feed()


persianCat = Cat()
# print(persianCat.__legs)
# print(persianCat.getLegs())
# print(persianCat.increaseLeg())
# print(persianCat.__feed())
print(persianCat.petCat())