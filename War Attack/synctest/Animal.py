# animal class
# contains constructor
# default value for animals if not inserted


class Animal():
    def __init__(self, health=250, power=100):
        self.health = health
        self.power = power
        pass


    def __str__(self):
        return f"The health of the animal is {self.health} and the power is {self.power}.\n"


#   def isDead
#   input: self
#   return: boolean
#   method:
#       if self.health == 0:
#           return True
#       return False
    def isDead(self):
        if self.health == 0:
            return True
        return False