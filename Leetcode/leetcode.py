# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# method: getIndices
# input: numbers, target
# return: indices
# method:
#   proti pair wise number jog korbo.
#   numbers er proti position er jonno:
#       numbers er proti index er jonno:
#           sum = numbers[index] + numbers[position]
#   jei pair er sum target er soman hobe, oi dui indice return.
#   if sum == target:
#       return [index, position]
def getIndices(numbers, targetNumber):
    for position in range(len(numbers)):
        for index in range(position+1,len(numbers)):
            sum = numbers[position] + numbers[index]
            if sum == targetNumber:
                return [position, index]


# print(getIndices([3,2,4,9,7],16))


# method: getIntFromRoman
# input: roman number as string
# return: converted integer
# method:
#   temporaryString, result, currentIndex
#   jotokkhon na currentIndex > len(romanNumber) hoy:
#       temporaryString += romanNumber[currentIndex]
#       jodi temporaryString == 'V':
#           result e 5 add
#           temporaryString = ''
#           currentIndex ++
#       othoba temporaryString == 'L':
#           result e 50 add
#           temporaryString = ''
#           currentIndex ++
#       othoba temporaryString == 'D':
#           result e 500 add
#           temporaryString = ''
#           currentIndex ++
#       othoba temporaryString == 'M':
#           result e 1000 add
#           temporaryString = ''
#           currentIndex ++ 
#       othoba temporaryString == 'I':
#           jodi porer char V hoy:
#               result += 4
#               currentIndex += 2
#               tempo = ""
#           othoba porer char X hoy:
#               result += 9
#               currentIndex += 2
#               tempo = ""
#           noile:
#               result += 1
#               currentIndex += 1
#               tempo = ""
#       othoba temporaryString == 'X':
#           jodi porer char L hoy:
#               result += 40
#               currentIndex += 2
#               tempo = ""
#           othoba porer char C hoy:
#               result += 90
#               currentIndex += 2
#               tempo = ""
#           noile:
#               result += 10
#               currentIndex += 1
#               tempo = ""
#       othoba temporaryString == 'C':
#           jodi porer char D hoy:
#               result += 400
#               currentIndex += 2
#               tempo = ""
#           othoba porer char M hoy:
#               result += 900
#               currentIndex += 2
#               tempo = ""
#           noile:
#               result += 100
#               currentIndex += 1
#               tempo = ""
def getIntFromRoman(romanNumber):
    currentIndex = 0
    temporaryString = ""
    result = 0
    while(currentIndex < len(romanNumber)):
        temporaryString += romanNumber[currentIndex]
        if temporaryString == "V":
            result += 5
            currentIndex += 1
            temporaryString == ""
        elif temporaryString == "L":
            result += 50
            currentIndex += 1
            temporaryString == ""
        elif temporaryString == "D":
            result += 500
            currentIndex += 1
            temporaryString == ""
        elif temporaryString == "M":
            result += 1000
            currentIndex += 1
            temporaryString == ""
        elif temporaryString == "I":
            if romanNumber[currentIndex+1] == "V":
                result += 4
                currentIndex += 2
                temporaryString = ""
            elif romanNumber[currentIndex+1] == "X":
                result += 9
                currentIndex += 2
                temporaryString = ""
            else:
                result += 1
                currentIndex += 1
                temporaryString = ""
        elif temporaryString == "X":
            if romanNumber[currentIndex+1] == "L":
                result += 40
                currentIndex += 2
                temporaryString = ""
            elif romanNumber[currentIndex+1] == "C":
                result += 90
                currentIndex += 2
                temporaryString = ""
            else:
                result += 10
                currentIndex += 1
                temporaryString = ""
        elif temporaryString == "C":
            if romanNumber[currentIndex+1] == "D":
                result += 400
                currentIndex += 2
                temporaryString = ""
            elif romanNumber[currentIndex+1] == "M":
                result += 900
                currentIndex += 2
                temporaryString = ""
            else:
                result += 100
                currentIndex += 1
                temporaryString = ""
    return result


# take a char from right to left
# if currentChar < previous:
#   sum -= value of currentChar
# else:
#   sum += value of currentChar

# print(getIntFromRoman("III"))        