namesAndAges = {"Ayon":28,"Eva":24,"Golam":36}
iterableElements = iter(namesAndAges)

while(True):
    try:
        print(next(iterableElements))
    except StopIteration:
        print("There are no more elements")
        break


class Names():
    def __init__(self, names):
        self.names = names
        self.index = 0


    def __str__(self):
        pass


    def __iter__(self):
        return self


    def __next__(self):
        if self.index == len(self.names):
            self.index = 0
            raise StopIteration
        currentIndex = self.index
        self.index += 1
        return self.names[currentIndex]


names = Names(["Ayon","eva","golam"])
iterateNames = iter(names)


while(True):
    try:
        print(next(iterateNames))
    except StopIteration:
        print("No more names available")
        break

while(True):
    try:
        print(next(iterateNames))
    except StopIteration:
        print("No more names available")
        break

for name in names:
    print(name)