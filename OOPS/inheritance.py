class Animal():
    def __init__(self):
        self.living = True

    
    def move(self):
        return "The animal is moving"


class Human(Animal):
    def __init__(self):
        self.hands = 2
        self.legs = 2


    def walk(self):
        return "The human is moving"


animal = Animal()
print(animal.move())

ayon = Human()
print(ayon.walk())
print(ayon.move())

# eikhane, Animal parent class and Human class child. Human class er object ayon. ayon Animal class er sob property and method inherit korse.
# eijonnoi ayon.walk and ayon.move duita tei print hoy