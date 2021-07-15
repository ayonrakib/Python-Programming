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
from typing import final


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



# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# addTwoNumbers
# input: two lists
# return: list
# method:
#   1. duita list er sobcheye kom length ta bair korbo
#   2. lowest length porjonto index gula iterate:
#       1. dui list er corresponding element and carryOver add korbo
#       2. jodi sum > 10 hoy:
#           1. final list e 0 append korbo
#           2. carryOver e 1 assign korbo
#       3. noile:
#           1. final list e sum append
#   3. jodi duita list er length same na hoy:
#       1. higher length list er baki sob element er jonno:
#           1. result hobe carryOver + current element
#           2. jodi result >= 10 hoy:
#               1. final list e append result - 10
#               2. carryOver 1
#           3. noile:
#               1. final list e append result
#               2. carryOver 0
#   5. jodi carryOver 1 hoy:
#       1. finalList e append 1
#   4. return final list
def addTwoNumbers(l1, l2):
    if len(l1) < len(l2):
        lowestLength = len(l1)
    else:
        lowestLength = len(l2)
    carryOver = 0
    finalList = []
    for index in range(lowestLength):
        addResult = carryOver + l1[index] + l2[index]
        if addResult >= 10:
            finalList.append(addResult - 10)
            carryOver = 1
        else:
            finalList.append(addResult)
    if len(l1) == len(l2):
        return finalList
    if len(l1) > len(l2):
        for index in range(lowestLength, len(l1)):
            addResult = carryOver + l1[index]
            if addResult >= 10:
                finalList.append(addResult - 10)
                carryOver = 1
            else:
                finalList.append(addResult)
                carryOver = 0
    else:
        for index in range(lowestLength, len(l2)):
            addResult = carryOver + l2[index]
            if addResult >= 10:
                finalList.append(addResult - 10)
                carryOver = 1
            else:
                finalList.append(addResult)
                carryOver = 0
    if carryOver == 1:
        finalList.append(1)
    return finalList

# print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))

# reverse order e ase.so l1 = [2,4,3], l2 = [5,6,4]
# er mane: 1st number: 342, 2nd number 465

# 1. l1 = [1,2], l2 = [3]
# 2. if len(l1) < len(l2):
# 3. if len([1,2]) < len(l2):
# 4. if 2 < len(l2):
# 5. if 2 < len([3]):
# 6. if 2 < 1:
# 7. if false:
# 8. else:
#   1. 


# 83. Remove Duplicates from Sorted List
# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


# removeDuplicates
# input: head object
# return: head node object
# method:
#   1. jodi head er value none hoy:
#       1. return none
#   2. currentNode hobe head er soman
#   3. jotokkhon currentNode er next object er value none na hocche:
#       1. jodi currentNode er value == currentNode.next er value:
#           1. currentNode.next = currentNode.next.next
#       2. currentNode = currentNode.next
#   4. return head
def removeDuplicates(head):
    if head.val is None:
        return None
    currentNode = head
    while(currentNode.next is not None):
        if currentNode.val == currentNode.next.val:
            currentNode.next = currentNode.next.next
        currentNode = currentNode.next
    return head

# print(removeDuplicates([1,1,2,3,3]))
# 1 = x123, 1 = x124, 2 = x125, 3 = x126, 3 = x127

# head = object of node with value 1, x123
#   1. if head.val is None:
#   2. if x123.val is None:
#   3. if 1 is None:
#   4. if false:
#   5. currentNode = head
#   6. currentNode = x123
#   7. while(currentNode.next is not None):
#   8. while(x123.next is not None):
#   9. while(node of 1 is not None):
#   10. while(true):
#       10.1. if currentNode.val == currentNode.next.val:
#       10.2. if x123.val == currentNode.next.val:
#       10.3. if 1 == currentNode.next.val:
#       10.4. if 1 == x123.next.val:
#       10.5. if 1 == x124.val:
#       10.6. if 1 == 1:
#       10.7. if true:
#           10.1.1. currentNode.next = currentNode.next.next
#           10.1.2. x123.next = currentNode.next.next
#           10.1.3. x123.next = x123.next.next
#           10.1.4. x123.next = x124.next
#           10.1.5. x123.next = x125 (2 er node)
#           10.1.6. currentNode = currentNode.next
#           10.1.7. currentNode = x123.next
#       10.8. currentNode = x125 (2 er node)
#   11. while(currentNode.next is not None):
#   12. while(x125.next is not None):
#   13. while(x126, node of 3 is not None):
#   14. while(true):
#       14.1. if currentNode.val == currentNode.next.val:
#       14.2. if x125.val == currentNode.next.val:
#       14.3. if 2 == currentNode.next.val:
#       14.4. if 1 == x125.next.val:
#       14.5. if 1 == x126.val:
#       14.6. if 1 == 3:
#       14.7. if false:
#       14.8. currentNode = currentNode.next
#       14.9. currentNode = x125.next
#       14.10. currentNode = x126
#   15. while(currentNode.next is not None):
#   16. while(x126.next is not None):
#   17. while(x127, 3 er node is not None):
#   18. while(true)
#       18.1. if currentNode.val == currentNode.next.val:
#       18.2. if x126.val == currentNode.next.val:
#       18.3. if 3 == currentNode.next.val:
#       18.4. if 3 == x126.next.val:
#       18.5. if 3 == x127.val:
#       18.6. if 3 == 3:
#       18.7. if true:
#           18.1.1. currentNode.next = currentNode.next.next
#           18.1.2. x126.next = currentNode.next.next
#           18.1.3. x126.next = x126.next.next
#           18.1.4. x123.next = x127.next