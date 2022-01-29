number = 5
numbers = [1,2]

def increment(number):
    number = number + 1

def append(numbers):
    numbers.append(3)

# increment(number)
append(numbers)
append([1,2,3])
append(numbers)

# print("new number value is: ",number)
print("new numbers is: ",numbers)
# [1,2,3,1,2]