namesAndAges = {"Ayon":28,"Eva":24,"Golam":36}
iterableElements = iter(namesAndAges)

while(True):
    try:
        print(next(iterableElements))
    except StopIteration:
        print("There are no more elements")
        break


class GetWeight():
    def __init__(self, finalWeight):
        self.finalWeight = finalWeight
        self.__iter__()
    

    def __str__(self):
        pass


    def __iter__(self):
        self.initialWeight = 100
        return self


    def __next__(self):
        if self.initialWeight <= self.finalWeight:
            currentWeight = self.initialWeight
            self.initialWeight += 1
            return currentWeight
        else:
            raise StopIteration

 
getWeight = GetWeight(105)
iterateWeight = iter(getWeight)

while(True):
    try:
        print(next(iterateWeight))
    except StopIteration:
        print("No more weights available")
        break

while(True):
    try:
        print(next(iterateWeight))
    except StopIteration:
        print("No more weights available")
        break