import itertools
# 10 ta number er ekta list ase. ekhon n ta number chai. ei n ta number thekei 100 ta chai, kintu randomly na. ei cyclic order e return korbo. random howa jabe na, cyclic howa lagbe.

# numbers = [1,2,3,4,5,6,...]
# output = [1,2,3]

# getNNumbers
# input: n
# return: n numbers
# method:
#   1. numbers = [1,2,3,4,5,6,...] 100 porjonto
#   2. targetNumbers empty list 
#   3. numbers er sob number er jonno iterator cycle:
#       1. jodi targetNumbers er length n er soman hoy:
#           1. return targetNumbers
#       2. targetNumbers e append number

def getNNumbers(n):
    numbers = []
    for count in range(1,101):
        numbers.append(count)
    targetNumbers = []
    for number in itertools.cycle(numbers):
        if len(targetNumbers) == n:
            return targetNumbers
        targetNumbers.append(number)

print(getNNumbers(200))