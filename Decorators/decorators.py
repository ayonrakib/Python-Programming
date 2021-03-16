def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def performOperation(operation):
    return operation(20,10)

# print("Using decorator for add function:",performOperation(add))

# print("Using decorator for subtract function:",performOperation(subtract))

def getAyonDetails(name):
    print("Will get Ayons details")

    def getHeight():
        print("Height is 5 ft 10 inch")

    def getAge():
        print("Age is 28")

    if name == "ayon":
        return getHeight()
    return getAge()


# getAyonDetails("ayon")
# getHeight()

x = 10
def getANewFunction():
    y = x + 10
    def getName():
        print(hex(id(y)))
        return y

    return getName

# print(getANewFunction)
a = getANewFunction()
# print("a variable is:",a)
# print("value of a() is:",a())
x = 100
b = getANewFunction()
# print("b variable is:",b)
print("y value for b variable is:",b())
# print("modified a variable is:",a)
print("modified a() value is:",a())
# jokhon ekta function definition pabe, tokhon variable e notun function object banabe.

# assignment:
# return x dile 100 hocche, return y dile 20 theke jacche, keno?

# 1. b() er return value
# 2. return x dile 100 hocche, return y dile 20 theke jacche, keno?

# 1. x = 10
# 2. def getANewFunction():
    # y = x + 10
    # def getName():
    #     return y

    # return getName
# 3. getANewFunction = x123, object address for getANewFunction function
# 4. a = getANewFunction()
#   1. y = x + 10
#   2. y = 10 + 10
#   3. y = 20
#   4. def getName():
#           return y
#   5. getName = x456, object address for getName function
#   6. return getName
#   7. return x456
# 5. a = x456
# 6. print("a variable is:",a)
# 7. print("a variable is:",x456)
# 8. "a variable is: x456"
# 9. print("value of a() is:",a())
# 10. print("value of a() is:",getName())
# 11. print("value of a() is:",20)
# 12. "value of a() is: 20"
# 13. x = 100
# 14. b = getANewFunction()
#   1. y = x + 10
#   2. y = 100 + 10
#   3. y = 110
#   4. def getName():
#           return y
#   5. getName = x789, object address for getName function
#   6. return getName
#   7. return x789
# 15. b = x789
# 16. print("b variable is:",b)
# 17. print("b variable is:",x789)
# 18. "b variable is: x789"
# 19. print("y value for b variable is:",b())
# 20. print("y value for b variable is:",getName())
# 21. print("y value for b variable is:",110)
# 22. "y value for b variable is: 110"
# 23. print("modified a variable is:",a)
# 24. print("modified a variable is:",x456)
# 25. "modified a variable is: x456"
# 26. print("modified a() value is:",a())
# 27. print("modified a() value is:",getName())
# 27. print("modified a() value is:",110)


def wrapper():
    a = 10
    print(hex(id(a)))

# wrapper()
# wrapper()