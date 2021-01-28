from random import randint
from Animal import Animal

# lion = Animal()
# tiger = Animal(200,150)

# lionArmy = []
# tigerArmy = []

# random = randint(5,10)

# for number in range(random):
#     lion = Animal()
#     lionArmy.append(lion)

# random = randint(random+2, random+10)
# for number in range(random):
#     tiger = Animal(200,150)
#     tigerArmy.append(tiger)

# # war function
# # input: duita list of army
# # return: updated lists
# # method:
# #   check korbo list input kina. na hoile error
# #   minimum length of armies bair korbo.
# #   ei length er theke kom ber fight hobe.
# #   ekta random variable (numberofAttacks) generate korbo ei length er theke kom er.
# #   numberofAttacks bar loop ghurbe and random lion tiger mara mari korbe.
# #   ei loop e:
# #       infinite while loop:
# #           lionIndex = random variable jeitar health 

# def war(tigerArmy, lionArmy):
#     if str(type(tigerArmy)) != "<class 'list'>":
#         raise Exception("Tiger army is not a list.")
#     if str(type(lionArmy)) != "<class 'list'>":
#         raise Exception("Lion army is not a list.")
#     minimumLengthOfArmies = min(len(tigerArmy), len(lionArmy))

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

# class er naam war
# war er constrcutor:
#   lionArmy, tigerArmy - duita empty list jeikhane animal object gula thakbe
#   randomTigerNumber = koyta animal hoite paare sheitar jonno variable
#   randomLionNumber = randomTigerNumber theke randomTigerNumber+10 porjonto random variable
class War():
    def __init__(self):
        self.lionArmy = []
        self.tigerArmy = []
        self.randomTigerNumber = randint(5,10)
        self.randomLionNumber = randint(self.randomTigerNumber+2, self.randomTigerNumber + 6)
        pass

    def __str__(self):
        pass


#   method name: createTigerArmy
#   parameter: self
#   return: None
#   method:
#       randomTigerNumber porjonto iterate:
#           tiger object banabo from class Animal, with health = 200, power = 150
#           tigerArmy te append
    def createTigerArmy(self):
        for number in range(self.randomTigerNumber):
            tiger = Animal(200,150)
            self.tigerArmy.append(tiger)

#   method name: createLionArmy
#   parameter: self.randomLionNumber, self.lionArmy
#   return: None
#   method:
#       randomLionNumber porjonto iterate:
#           lion object banabo from class Animal, with health = 150, power = 200
#           lionArmy te append
    def createLionArmy(self):
        for number in range(self.randomLionNumber):
            lion = Animal(150,200)
            self.lionArmy.append(lion)


#   method name: getRandomTiger
#   input: tiger List
#   return: random tiger object who is alive(health >=0)
#   method:
#       if parameter is not list:
#           throw exception
#       while(infinite loop):
#           random index
#           xxxif tigerlist[randomIndex].health != 0:xxx -> eita dorkar nai karon ami delete korsi dead animal der
#               return tigerlist[randomIndex]
    def getRandomTiger(self):
        randomTigerIndex = randint(0,len(self.tigerArmy))
        return self.tigerArmy[randomTigerIndex]
                

#   method: get random lion
#   input: 
#   method name: attack
#   input: number of runs
#   return: random lion object
#   method:
#       if parameter is not a list:
#           raise exception
#       infinite loop:
#           random lion index
#           if lionlist[randomlionindex].health != 0:
#               return that lion
    def getRandomLion(self):
        randomlionindex = randint(0,len(self.lionArmy))
        return self.lionArmy[randomlionindex]


#   remove tiger
#   input: tiger object
#   return: nothing
#   method:
#       tigerlist.remove(object)
    def removeTiger(self, tigerObject):
        self.tigerArmy.remove(tigerObject)


#   remove lion
#   input: lion object
#   return:nothing
#   method:
#       lionlist.rmeove(object)
    def removeLion(self, lionObject):
        self.lionArmy.remove(lionObject)


#   fight method
#   input: two different animal objects. first is tiger object, then lion object.
#   return: no return
#   method:
#       self.tigerHealth -= self.lionAttack
#       self.lionHealth -= self.tigerAttack
#       no return
    def fight(self, tiger, lion):
        tiger.health -= lion.power
        lion.health -= tiger.power


#   return: string
#   method:
#       number of runs porjonto iterate:
#           1. get a random tiger: getRandomTiger()
#           2. get a random lion: getRandomLion()
#           3. fight(tiger, lion)
#           4. remove if anyone is dead after fight
    def attack(self, numberofAttacks):
        animal = Animal()
        for run in range(numberofAttacks):
            #1. get a random tiger: getRandomTiger()
            randomTiger = self.getRandomTiger()

            #2. get a random lion: getRandomLion()
            randomLion = self.getRandomLion()

            # 3. fight(tiger, lion)
            self.fight(randomTiger, randomLion)

            # 4. remove if anyone is dead after fight
            isTigerDead = animal.isDead()
            if isTigerDead:
                self.removeTiger(randomTiger)

            isLionDead = animal.isDead()
            if isLionDead:
                self.removeLion(randomLion)


#   method: resultOfWar
#   input: army of aftermath of war
#   return: string representation of updated animals
#   method:
#       for tiger list:
#           conditionOfTigers = get tiger health and print like tiger index: health = ...
#           conditionOfTigers+= '\n'
#       print(conditionOfTigers)
#       for lion list:
#           conditionOfLions = get 

# vul:
# 1. animals file er naam ta vul. animal hobe.
# 2. isdead method ta animal er method hobe, war er hobe.
# 3. removedeadanimal-> confusion toiri kore, animal er ektai collection ase. duita collection ase, so confusion hocche.
# 4. better hocche-> duita different method hobe, removetiger and remove lion


# evaluation
# war = War()
# war.attack(5) where numberOfAttacks = 5
#   1. self.lionArmy = []
#   2. self.tigerArmy = []
#   3. self.randomTigerNumber = randint(5,10)
#   4. self.randomTigerNumber = 6
#   5. self.randomLionNumber = randint(self.randomTigerNumber+2, self.randomTigerNumber + 6)
#   6. self.randomLionNumber = randint(6+2, self.randomTigerNumber + 6)
#   7. self.randomLionNumber = randint(8, self.randomTigerNumber + 6)
#   8. self.randomLionNumber = randint(8, 6+6)
#   9. self.randomLionNumber = randint(8,12)
#   10. self.randomLionNumber = 10