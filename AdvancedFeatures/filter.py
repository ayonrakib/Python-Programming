numbers = [1,2,3,4,5,6]

def isOdd(number):
    if number % 2 == 0:
        return False
    return True

filteredOddNumbers = filter(isOdd,numbers)
for oddNumber in filteredOddNumbers:
    print(oddNumber)