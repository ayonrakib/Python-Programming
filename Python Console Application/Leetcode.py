from random import randint
# sortArrayByParity. 1st e even, pore baki gula
# input: list
# output: list
# method er vitore:
#   newList banabo.
#   A er proti ta element er against e iterate:
#       jodi A[element]%2 == 0 hoy:
#           newList.append(A[element])
#   A er proti ta element er jonno iterate:
#       JODI A[element] odd hoy:
#           newlist.append(A[element])
#   return newList

def sortArrayByParity(A):
    newList = []
    for integer in A:
        if integer%2 == 0:
            newList.append(integer)
    for integer in A:
        if integer %2 != 0:
            newList.append(integer)
    return newList

# print(sortArrayByParity([1,1,1,2,4]))

# selfDividingNumbers
# method name: selfDividingNumbers
# input: left number, right number
# output: list
# method er vitore:
#   if left < 1 or right > 10000:
#       return None
#   newList = []
#   left theke right porjonto iterate korbo:
#       proti ta number er jonno iterate:
#           jodi number % (number%10) == 0 hoy:
#               number /= 10
#           else:
#               break
#           if number < 10:
#               newList.append(number)
#   return newList

def selfDividingNumbers(left, right):
    if left < 1 or right > 10000:
        return None
    newList = []
    temporaryNumber = 0
    for number in range(left, right+1):
        temporaryNumber = number
        while number > 0:
            if number % 10 == 0:
                break
            if temporaryNumber % (number%10) == 0:
                print(number)
                number = int(number / 10)
            else:
                break
        if number == 0:
            newList.append(temporaryNumber)
    return newList

# print(selfDividingNumbers(1,22))

# def judgeCircle
# input: string
# output: binary
# method:
#   result = 0
#   string er proti ta character er against e iterate:
#       U = +2
#       D = -2
#       L = -1
#       R = +1
#       result += int(string[character])
#   if result == 0:
#       return True
#   return False

def judgeCircle(moves):
    result = 0
    for movement in moves:
        if movement == 'U':
            direction = +2
        elif movement == 'D':
            direction = -2
        elif movement == 'L':
            direction = -1
        else:
            direction = +1
        result += direction
    if result == 0:
        return True
    return False

# print(judgeCircle('UDLR'))

# def diStringMatch
# input: string
# output: list
# joto gula character string er vitore, er cheye ek beshi list er element.
# from random import randint
# method:
#   newList = []
#   stringLength = len(S)
#   newList.append(randint(0,stringLength))
#   for character in S:
#       if character == 'I':
#           newList.append(newList[len(newList)-1],stringLength)
#       else:
#           newList.append(0,newList[len(newList)-1])
#   return newList
def diStringMatch(S):
    newList = []
    stringLength = len(S)
    newList.append(randint(0,stringLength+1))
    for character in S:
        if character == 'I':
            newList.append(randint(newList[len(newList)-1],stringLength+1))
        else:
            newList.append(randint(0,newList[len(newList)-1]))
    return newList

# print(diStringMatch('IDID'))

# def hammingDistance
# input: x, y duitai integer
# output: integer -> jei duita bit alada, shei duita
# method:
#   differentBit variable, firstBinaryInString and secondBinaryInString
#   firstBinaryInString = bin(x).replace('0b','')
#   secondBinaryInString = bin(y).replace('0b','')
#   zero padding korte hobe. jeitar length boro, oitar length dhore baki number zero padding korte hobe.
#   zero padding kore reverse kore dibo choto number ta.
#   1stbinary er proti ta character er against e iterate:
#       2ndBinary er proti ta character er against e iterate:
#           jodi duita alada hoy:
#               differentBit += 1
#           jodi 2ndBinaryBit er sheshe pouchai:
#               break
#   return differentBit

def hammingDistance(x,y):
    def zeroPadding(higherLengthString, lowerLengthString):
        for stringLength in range(len(higherLengthString)- len(lowerLengthString)):
            lowerLengthString = '0' + lowerLengthString
        return lowerLengthString
    differentBit = 0
    firstBinaryInString = bin(x).replace('0b','')
    secondBinaryInString = bin(y).replace('0b','')
    if len(firstBinaryInString) > len(secondBinaryInString):
        secondBinaryInString = zeroPadding(firstBinaryInString,secondBinaryInString)
        print('first and second binary: ',firstBinaryInString, secondBinaryInString)
    elif len(firstBinaryInString) < len(secondBinaryInString):
        firstBinaryInString = zeroPadding(secondBinaryInString,firstBinaryInString)
        print('first =',firstBinaryInString)
        print('first and second binary: ',firstBinaryInString, secondBinaryInString)
    else:
        pass
    for bit in range(len(firstBinaryInString)):
            if firstBinaryInString[bit] != secondBinaryInString[bit]:
                differentBit += 1
    return differentBit

# print(hammingDistance(4,14))

# def arrayPairSum
# input: nums: list
# output: integer, sum of smallest number in groups
# method:
#   result = 0
#   newList = []
#   lengthOfList = len(nums)
#   for element in range(0,len(nums),lengthOfList/2):
#       
# def arrayPairSum():
    result = 0
    nums= [1,4,3,2]
    newList = []
    lengthOfList = len(nums)
    for element in range(0,len(nums),int(lengthOfList/2)):
        newList = []
        for number in nums:
            if len(newList) != int(lengthOfList/2):
                newList.append(number)
        print(newList)


# def peakIndexInMountainArray
# input: A, list
# output: integer, an index
# method:
#   for index in range(len(list)):
#       if list[index] < list[index+1]:
#           continue
#       else:
#           return index+1
def peakIndexInMountainArray(A):
    for index in range(len(A)):
        if A[index] < A[index+1]:
            continue
        else:
            return index
# print(peakIndexInMountainArray([0,2,1,0]))

# def minSubsequence
# input: nums, list
# output: list
# method:
#   newList = []
#   for index in range(len(nums)):
#       newList.append(nums[element])
#       if element > sum(nums[index,len(nums)]):
#           continue
#       else:
#           return newList

def minSubsequence(nums):
    newList = []
    nums.sort()
    nums.reverse()
    for index in range(len(nums)):
        newList.append(nums[index])
        if sum(newList) <= sum(nums[index+1:len(nums)]):
            continue
        else:
            return newList
    
# print(minSubsequence([6]))

# def uniqueOccurrences
# input: arr, list
# output: boolean. if all elements repeated unique, true. else, false
# method:
def uniqueOccurrences(arr):
    dict = {}
    newList = []
    for element in arr:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] += 1
    for repeat in dict.values():
        if repeat not in newList:
            newList.append(repeat)
        else:
            return False
    return True
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))