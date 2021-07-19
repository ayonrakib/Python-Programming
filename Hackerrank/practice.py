# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 15 The right to left diagonal = 17. Their absolute difference is |15-17| = 2.


# getAbsoluteDifferenceofDiagonalSum
# input: n -> row/column of matrix, arr -> 2d list
# return: modulus of primary diagonal sum and secondary diagonal sum
# method:
#   1. primaryDiagonalSum and secondaryDiagonalSum 0
#   2. n porjonto sob number er jonno -> count:
#       1. primaryDiagonalSum er sathe add arr[count][count]
#   3. row = 0
#   4. n theke shuru kore 0 porjonto sob column er jonno:
#       1. secondaryDiagonalSum er sathe add arr[row][column]
#       2. row++
#   5. return mod of secondaryDiagonalSum - primaryDiagonalSum

def getAbsoluteDifferenceofDiagonalSum(n, arr):
    primaryDiagonalSum = 0
    secondaryDiagonalSum = 0
    for count in range(n):
        primaryDiagonalSum += arr[count][count]
    row = 0
    for column in range(n-1, -1, -1):
        secondaryDiagonalSum += arr[row][column]
        row += 1
    return abs(primaryDiagonalSum - secondaryDiagonalSum)


print(getAbsoluteDifferenceofDiagonalSum(3, [[1,2,3], [4,5,6],[9,8,9]]))


# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with 6 places after the decimal.

# example: arr = [1,1,0,-1,-1]
# There are n=5 elements, two positive, two negative and one zero. Their ratios are: 2/5 = 0.4000000, 2/5 = 0.4000000, 1/5 =  0.2000000
# Results are printed as:

# 0.400000
# 0.400000
# 0.200000

# getRatios
# input: numbers list
# return: nothin, just print rations
# method:
#   1. positiveNumbers, negativeNumbers, zeros
#   2. numbers er sob number er jonno:
#       1. jodi number -ve hoy:
#           2. negativeNumbers += 1
#       2. othoba jodi number 0 hoy:
#           1. zeros++
#       3. othoba jodi +ve hoy:
#           1. positiveNumbers++
#   3. print positiveNumbers/length, negativeNumbers/length and zeros/length
def getRatios(numbers):
    positiveNumbers = 0
    negativeNumbers = 0
    zeros = 0
    for number in numbers:
        if number < 0:
            negativeNumbers += 1
        elif number == 0:
            zeros += 1
        elif number > 0:
            positiveNumbers += 1
    totalNumbers = len(numbers)
    print("{:.7f}".format(positiveNumbers/totalNumbers))
    print("{:.7f}".format(negativeNumbers/totalNumbers))
    print("{:.7f}".format(zeros/totalNumbers))

# getRatios([1,1,0,-1,-1])


# Staircase detail

# This is a staircase of size 4:

#    #
#   ##
#  ###
# ####
# Its base and height are both equal to 4. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size 4.

# printStairCase
# input: number as int
# return: # as stair case
# method:
#   1. stairCase empty string
#   2. number porjonto iterate -> count:
#       1. number - count-2 porjonto iterate:
#           1. stairCase e concat space
#       2. 0 theke space porjonto iterate:
#           1. stairCase e concat
def printStairCase(number):
    stairCase = ""
    for row in range(1,number+1):
        for space in range(number-row-1,-1,-1):
            stairCase += " "
        hashsTring = ""
        for hash in range(row):
            hashsTring += "#"
        if row != number:
            stairCase += hashsTring + "\n"
        else:
            stairCase += hashsTring
    print(stairCase)

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example
# arr= [1,3,5,7,9]
# The minimum sum is 1+3+5+7 = 16  and the maximum sum is 3+5+7+9 = 24 . The function prints
# 16 24

# getMinimumAndMaximum
# input: numbers list
# return: nothing just print two numbers
# method:
#   1. firstSum secondSum 0
#   2. sort arr
#   2. numbers er 1st 2 index er jonno:
#       1. jodi index 0 hoy:
#           1. firstSum = arr[index]
#       2. noile:
#           1. secondSum = arr[index]
#       3. index+1 theke 3 ta number iterate:
#           1. jodi index 0 hoy:
#               1. firstSum += arr[secondIndex]
#           2. noile:
#               1. secondSum += arr[secondIndex]
#       4. jodi firstSum choto hoy secondSUm theke:
#           1. print(first second)
#       5. noile:
#           1. print(second first)


def getMinimumAndMaximum(arr):
    firstSum = 0
    secondSum = 0
    arr.sort()
    for index in range(2):
        if index == 0:
            firstSum = arr[index]
        else:
            secondSum = arr[index]
        for secondIndex in range(index+1, index+4):
            if index == 0:
                firstSum += arr[secondIndex]
            else:
                secondSum += arr[secondIndex]
    if firstSum < secondSum:
        print(firstSum, secondSum)
    else:
        print(secondSum, firstSum)

# getMinimumAndMaximum([7,69,2,221,8974])

# You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4,4,1,3]

# The maximum height candles are 4 units high. There are 2 of them, so return 2.

# getTallestCandleNumber
# input: candles list
# return: number of tallest candles in int
# method:
#   1. tallestCandle = canldes[0]
#   2. candles er sob candle er jonno:
#       1. jodi canlde[index] > tallestCandle hoy:
#           1. tallestCandle = candles[index]
#   3. numberOfTallestCandle 0
#   3. canldes er sob candle er jonno:
#       1. jodi candle[index] = tallestCandle hoy:
#           1. numberOfTallestCandle ++
#   4. return numberOfTallestCandle
def getTallestCandleNumber(candles):
    tallestCandle = candles[0]
    for index in range(len(candles)):
        if candles[index] > tallestCandle:
            tallestCandle = candles[index]
    numberOfTallestCandle = 0
    for candle in candles:
        if tallestCandle == candle:
            numberOfTallestCandle += 1
    return numberOfTallestCandle
# print(getTallestCandleNumber([4,4,1,3]))


# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45

# getMilitaryTime
# input: time s as string
# return" militaryTime as str
# method:
#   1. militaryTime ""
#   2. jodi s er last dui char PM hoy:
#       1. jodi 1st dui char 12 hoy:
#           1. militaryTime e concat str of 12 and int of s er 1st 2 char
#       2. noile:
#           1. militaryTime e concat 12 str
#   3. othoba s er last dui char AM and 1st dui char 12 hoy:
#       1. militaryTime e concat 00 str
#   4. noile:
#       1. militaryTime e concat s er 1st dui char
#   5. militaryTime e concat 3rd char theke s er shesh 2 char er ag porjonto
#   6. return militaryTime
def getMilitaryTime(s):
    militaryTime = ""
    if s[len(s)-2:len(s)] == "PM":
        if s[0:2] != "12":
            militaryTime += str(12 + int(s[0:2]))
        else:
            militaryTime += "12"
    elif s[len(s)-2:len(s)] == "AM" and s[0:2] == "12":
        militaryTime += "00"
    else:
        militaryTime += s[0:2]
    militaryTime += s[2:len(s)-2]
    return militaryTime

# print(getMilitaryTime("07:05:45PM"))


# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to100 .
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 40, no rounding occurs as the result will still be a failing grade.

# Sample Input 0

# 4
# 73
# 67
# 38
# 33

# Sample Output 0
# 
# 75
# 67
# 40
# 33
# 4-> no grading, 73 -> 75 cause 2 diff, 67 -> 67 cause 3 diff from 70, 38 -> 40 cause 2 diff from 40. 33 -> 33 cause below 40


# gradingStudents
# input: grades as int
# return: roundedGrade as int
# method:
#   1. roundedGrades []
#   1. grades er sob grade er jonno:
#       1. jodi grade < 38 hoy othoba grade mod 5 less than equal to 2 hoy:
#           1. roundedGrades e append grade
#       2. othoba jodi grade mod 5 > 2 hoy:
#           1. roundedGrades e append grade + 5 - grade mod 5


def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        if grade < 38 or grade % 5 <= 2:
            roundedGrades.append(grade)
        elif grade % 5 > 2:
            roundedGrades.append(grade + 5 - grade % 5)
    return roundedGrades

# print(gradingStudents([4,73,67,38,33])) 