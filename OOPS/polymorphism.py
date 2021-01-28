print(1+2)

# eikhane, + ekta binary operator. er dui pashe integer boshche and return korse integer

print("Hello"+" World")

# eikhane, + binary operator er dui pashe string concatenate korse

# so, eki + operator dui different type er kaaj korte paare

class Bike():
    def __init__(self):
        self.engine = 1


    def move(self):
        return "The bike is accelerating"


class Ducati(Bike):
    def __init__(self):
        self.steering = 1
        self.engine = 2


    def move(self):
        return "The Ducati is accelerating"


bike = Bike()
print(bike.move())

ducati = Ducati()
print(ducati.move())
print(ducati.engine)


# eikhane, ducati object tar move howar kotha chilo Bike class er ta, but hoise ducati object tar
# eita ke bole method over writing

# ducati er ducati.engine howar kotha chilo 1 from Bike, hoise 2 from Ducati class
# so, property o over write hoise