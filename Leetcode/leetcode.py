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
# def getIntFromRoman(romanNumber):
#     currentIndex = 0
#     temporaryString = ""
#     result = 0
#     while(currentIndex < len(romanNumber)):
#         temporaryString += romanNumber[currentIndex]
#         if temporaryString == "V":
#             result += 5
#             currentIndex += 1
#             temporaryString == ""
#         elif temporaryString == "L":
#             result += 50
#             currentIndex += 1
#             temporaryString == ""
#         elif temporaryString == "D":
#             result += 500
#             currentIndex += 1
#             temporaryString == ""
#         elif temporaryString == "M":
#             result += 1000
#             currentIndex += 1
#             temporaryString == ""
#         elif temporaryString == "I":
#             if romanNumber[currentIndex+1] == "V":
#                 result += 4
#                 currentIndex += 2
#                 temporaryString = ""
#             elif romanNumber[currentIndex+1] == "X":
#                 result += 9
#                 currentIndex += 2
#                 temporaryString = ""
#             else:
#                 result += 1
#                 currentIndex += 1
#                 temporaryString = ""
#         elif temporaryString == "X":
#             if romanNumber[currentIndex+1] == "L":
#                 result += 40
#                 currentIndex += 2
#                 temporaryString = ""
#             elif romanNumber[currentIndex+1] == "C":
#                 result += 90
#                 currentIndex += 2
#                 temporaryString = ""
#             else:
#                 result += 10
#                 currentIndex += 1
#                 temporaryString = ""
#         elif temporaryString == "C":
#             if romanNumber[currentIndex+1] == "D":
#                 result += 400
#                 currentIndex += 2
#                 temporaryString = ""
#             elif romanNumber[currentIndex+1] == "M":
#                 result += 900
#                 currentIndex += 2
#                 temporaryString = ""
#             else:
#                 result += 100
#                 currentIndex += 1
#                 temporaryString = ""
#     return result


# take a char from right to left
# if currentChar < previous:
#   sum -= value of currentChar
# else:
#   sum += value of currentChar

# print(getIntFromRoman("III"))
def getIntFromRoman(romanNumber):
    romanNumberToIntegerMapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    sum = 0
    for index in range(-1, -(len(romanNumber)-1), -1):
        if romanNumberToIntegerMapping[romanNumber[index]] < romanNumberToIntegerMapping[romanNumber[index-1]]:
            sum -= romanNumberToIntegerMapping[romanNumber[index]]
        else:
            sum += romanNumberToIntegerMapping[romanNumber[index]]
    return sum

# print(getIntFromRoman('LVIII'))

# binaryAdd
# input: two string
# return: string
# method:
#   1. jodi firstNumber length > secondnumber length hoy:
#       1. secondnumber er 1st e (secondNumber-firstNumber) length poriman 0 string append
#   2. othoba firstNumber length < secondnumber length hoy:
#       1. firstNumber er 1st e (firstNumber-secondnumber) length poriman 0 string append
#   3. overFlow = ""
#   4. sum = ""
#   3. index -1 theke komte komte anynumber length porjonto iterate:
#       1.  jodi secondNumber[index] and firstNumber[index] duitai "0" hoy:
#           1. joid overFlow == "0" hoy:
#               1. sum += 0 
#               2. overFlow = 0
#           2. othoba "1" hoy:
#               1. sum += 1
#               2. overFlow = 0
#       2. othoba secondNumber[index] = "1" and firstNumber[index] = "0" hoy:
#           1. joid overFlow == "0" hoy:
#               1. sum += 1
#               2. overFlow = 0
#           2. othoba "1" hoy:
#               1. sum += 0
#               2. overFlow = 1
#       3. othoba secondNumber[index] = "0" and firstNumber[index] = "1" hoy:
#           1. joid overFlow == "0" hoy:
#               1. sum += 1
#               2. overFlow = 0
#           2. othoba "1" hoy:
#               1. sum += 0
#               2. overFlow = 1
#       4. othoba secondNumber[index] = "1" and firstNumber[index] = "1" hoy:
#           1. joid overFlow == "0" hoy:
#               1. sum += 0
#               2. overFlow = 1
#           2. othoba "1" hoy:
#               1. sum += 0
#               2. overFlow = 1
#   3. jodi overFlow == "1" hoy:
#       1. sum += overFlow
#   4. return sume r reverse
def binaryAdd(firstNumber, secondNumber):
    zeros = ""
    sum = ""
    overFlow = "0"
    if len(firstNumber) > len(secondNumber):
        numberOfZeros = len(firstNumber) - len(secondNumber)
        for zero in range(numberOfZeros):
            zeros += "0"
        secondNumber = zeros + secondNumber
    elif len(firstNumber) < len(secondNumber):
        numberOfZeros = len(secondNumber) - len(firstNumber)
        for zero in range(numberOfZeros):
            zeros += "0"
        firstNumber = zeros + firstNumber
    for index in range(-1, -(len(firstNumber)+1), -1):
        if firstNumber[index] == "0" and secondNumber[index] == "0":
            if overFlow == "0":
                sum += "0"
                overFlow = "0"
            elif overFlow == "1":
                sum += "1"
                overFlow = "0"
        elif firstNumber[index] == "1" and secondNumber[index] == "0":
            if overFlow == "0":
                sum += "1"
                overFlow = "0"
            elif overFlow == "1":
                sum += "0"
                overFlow = "1"
        elif firstNumber[index] == "0" and secondNumber[index] == "1":
            if overFlow == "0":
                sum += "1"
                overFlow = "0"
            elif overFlow == "1":
                sum += "0"
                overFlow = "1"
        elif firstNumber[index] == "1" and secondNumber[index] == "1":
            if overFlow == "0":
                sum += "0"
                overFlow = "1"
            elif overFlow == "1":
                sum += "1"
                overFlow = "1"
    if overFlow == "1":
        sum += overFlow
    return sum[::-1]


# print(binaryAdd("1001","1001"))

# getSquareRoot
# maximum number: 2^31, so 2147483698, 10 digit
# amra kori daan pash theke pair dhore, so maximum 5 ta pair hobe, 0 theke 5 ta pair
# decimal er poreo
# input: int
# return: int
# method:
#   1. jodi input 0 hoy:
#       1. return 0
#   2. pairs = []
#   3. jotokkhon na number 0 hoy:
#       1. pairs e append number % 100
#       2. number %= 100
#   4. print(pairs)
def getSquareRoot(number):
    if number == 0:
        return 0
    pairs = []
    while(number > 1):
        pairs.append(int(number%100))
        number /= 100
    pairs = pairs[::-1]
    print(pairs)


# getSquareRoot(214748369)

# getLengthOfLastWord
# input: s, string
# return: length of last word in int
# method:
#   1. indexOfSpace= 0
#   2. wordLength = 0
#   3. s er sob index er jonno:
#       1. jodi s[index] space/tab/newline hoy:
#           1. spaceIndex = index
#           2. infinite loop:
#               1. spaceIndex++
#               2. jodi  
#               



# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight","f"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# end condition:
# 1. jodi character match na kore
# 2. jodi end of string paai

# getLongestPrefix
# input: list of words, strs
# return: highest common substring
# method: