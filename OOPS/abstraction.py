from abc import abstractmethod, ABC

class Vehicle(ABC):
    def __init__(self, body, engine):
        self.body = body
        self.engine = engine


    def start(self):
        return "The vehicle has started"


    def stop(self):
        return "The vehicle has stopped"


    @abstractmethod
    def move(self):
        pass


# Vehicle class ta call kora jabe na, oita 2.7 er concept
# ekhon korte hobe super().__init__()
# eita return kore: tara super mane parent er object tao banay. proti ta parent er object banay, oitar method call dite parbo
# dummy reference o hoite paare
class Car(Vehicle):
    def __init__(self, wheels):
        self.wheels = wheels
        super().__init__(1,1)


    def move(self):
        return "The car is moving"


kia = Car(4)
print(kia.move())

# ami jodi vehicle object banaitam, error khaito karon move() method ta define kora nai, only pass ase
# Car class er method move() ta over write korse. 
# jotoi child class banai Vehicle theke, sobar MUST move method lagbe, noile error khabe
# so, child er jeno ekta method thakei sheita ensure kore abstarct mathod