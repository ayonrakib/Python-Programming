favorite_numbers = [6, 57, 4]
my_iterator = iter(favorite_numbers)
print(type(my_iterator))
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


numbers = (1,2,3,4,5,6,7,8,9,10)
numbersIterator = iter(numbers)
# print(next(numbersIterator))
# print(next(numbersIterator))
# print(next(numbersIterator))
# print(next(numbersIterator))

for number in numbersIterator:
    print(next(numbersIterator))


# 1. for number in numbersIterator:
# 2. loop1:
#   3. number = 1
#   4. print(next(numbersIterator))
#   5. print(next(x12345))
#   6. print(2)
# 7. loop2:
#   






names = [["ayon","saad"],["golam"]]
namesIterator = iter(names)
# print(next(namesIterator))
# print(next(namesIterator))
# print(next(namesIterator))

# for nestedNames in namesIterator:
#     print(next(namesIterator))

# 1. for nestedNames in namesIterator:
# 2. loop1:
#   3. nestedNames = ['ayon', 'saad']
#   4. print(next(namesIterator))
#   5. print(next(x12345))
#   6. print(["golam"])