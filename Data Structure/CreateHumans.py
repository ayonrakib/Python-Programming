# create humans class
# input: none
# method: create humans list
class CreateHumans():
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