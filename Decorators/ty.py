x = 1
y = 2
x,y = y,y
print(x+y)
a = "ac"
print(a.upper())
print('Ba123'.islower())

class Test():
    def __init__(self, num) -> None:
        self.num = num
        num = 12

x = Test(3)
print(x.num)