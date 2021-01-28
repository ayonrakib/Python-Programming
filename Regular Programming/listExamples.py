from random import randint
# pylint: disable=unused-variable
#1. sum of all lists
def getSumOfNumbers(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    result = 0
    for number in list:
        result += number
    return result


#2. multiply of all lists
def getMultiplicationOfNumbers(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    result = 1
    for number in list:
        result *= number
    return result

    
#3. get largest number in list
def getLargestNumberFromList(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    if len(list) == 0:
        return []
    largerNumber = list[0]
    for index in range(1,len(list)):
        if largerNumber<list[index]:
            largerNumber = list[index]
    return largerNumber


#4. get smallest number in list
def getSmallestNumberFromList(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    if len(list) == 0:
        return []
    smallerNumber = list[0]
    for index in range(1,len(list)):
        if smallerNumber>list[index]:
            smallerNumber = list[index]
    return smallerNumber

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def getNumberOfStringsWithSameFirstAndLastElement(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    count=0
    for element in list:
        if element[0] == element[len(element)-1]:
            count += 1
    return count


#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# input: list
# return: ;ist
# method:
#   raise exception if not list
#   temporarytuple = ()
#   proti ta element er jonno iterate:
#       abar iterate:
#           jodi currenttuple[1] > nexttuple[1] hoy:
#               temporarytuple = currenttuple
#               currenttuple = nexttuple
#               nexttuple = temporarytuple
#   return list
def getSortedList(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    temporaryTuple = ()
    for element in range(len(list)):
        for index in range(len(list)-1):
            if list[index][1] > list[index+1][1]:
                temporaryTuple = list[index]
                list[index] = list[index+1]
                list[index+1] = temporaryTuple
    return list


#7. Write a Python program to remove duplicates from a list.
def removeDuplicatesFromList(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    uniqueElementList = []
    for index in range(len(list)):
        if list[index] not in uniqueElementList:
            uniqueElementList.append(list[index])
    return uniqueElementList


#8. Write a Python program to check a list is empty or not.
def checkIfListIsEmpty(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    if len(list) == 0:
        return True
    return False  


#9. Write a Python program to clone or copy a list
def copyList(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    # copiedList = list
    copiedList = []
    for element in list:
        copiedList.append(element)
    return copiedList


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def getListOfWordsGreatherThanN(list, n):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    count = 0
    for word in list:
        if str(type(word)) != "<class 'str'>":
            raise Exception("all elements are not strings.")
        if len(word) > n:
            count += 1
    return count


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def checkIfListsHaveCommonElement(list1, list2):
    if str(type(list1)) != "<class 'list'>":
        raise Exception("input list1 is not a list")
    if str(type(list2)) != "<class 'list'>":
        raise Exception("input list2 is not a list")
    for element in list1:
        if element in list2:
            return True
    return False

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def removeSpecificIndexElements(list):
    if str(type(list)) != "<class 'list'>":
        raise Exception("input is not a list")
    newList = []
    for index in range(len(list)):
        if index != 0 and index != 4 and index != 5:
            print(index)
            newList.append(list[index])
    return newList


# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

# threeDimensionalArray = [[[1,2,3,1,2,3],[4,5,6,4,5,6],[[1,2,3,1,2,3],[4,5,6,4,5,6]],
#                          [[7,8,9,7,8,9],[10,11,12,10,11,12],[7,8,9,7,8,9],[10,11,12,10,11,12]],
#                          [[13,14,15,13,14,15],[16,17,18,16,17,18],[13,14,15,13,14,15],[16,17,18,16,17,18]]]]
# # for page in threeDimensionalArray:
# #     for row in page:
# #         for column in row:
# #             print(column)
# print(threeDimensionalArray[0][1][2])
# print(threeDimensionalArray)

# twoDimensionalArray = [[1,2,3],[4,5,6]]

# print(twoDimensionalArray[1][2])
def getThreeDimensionalMatrix():
    threeDimensionalArray = []
    temporaryRow = []
    temporaryList = []
    for page in range(3):
        for row in range(4):
            for column in range(6):
                temporaryList.append('*')
            temporaryRow.append(temporaryList)
            temporaryList = []
        threeDimensionalArray.append(temporaryRow)
        temporaryRow = []
    return threeDimensionalArray
    
# print(getThreeDimensionalMatrix())


# 14.Write a Python program to print the numbers of a specified list after removing even numbers from it.
# input: list
# return: list
# method:
#   raise exception if input is not list
#   newList = []
#   for each element in list:
#       if element is not even:
#           newList e add
#   return newList
def getListWithOddNumbers(list):
    # if str(type(list)) != "<class 'list'>":
    #     raise Exception("input is not a list")
    # for element in list:
    #     if str(type(element)) != "<class 'int'>":
    #         raise Exception("All elements have to be integer.")
    newList = []
    for element in list:
        if element % 2 != 0:
            newList.append(element)
    return newList


# 15. Write a Python program to shuffle and print a specified list
def printShuffledList(list):
    newList = []
    while(True):
        if len(newList) == len(list):
            break
        randomIndex = randint(0,len(list)-1)
        if list[randomIndex] not in newList:
            newList.append(list[randomIndex])
    print(newList)


# 16. Write a Python program to generate and print a list of first and last 
# 5 elements where the values are square of numbers between 1 and 30 (both included).
def printFirstAndLastFiveSquaredElements():
    list = []
    for number in range(1,31):
        list.append(number*number)
    print(list[:5])
    print(list[len(list)-5:len(list)])

# 17. Write a Python program to generate and print a list except for the first 5 elements, 
# where the values are square of numbers between 1 and 30 (both included).
def printSpecificIndexedList():
    list = []
    for number in range(1,31):
        list.append(number*number)
    print(list[5:len(list)])


# 18. Write a Python program to generate all permutations of a list in Python.
def getPermutationOfList(list):
    return 0

# 19. Write a Python program to get the difference between the two lists.
def getDifferenceBetweenTwoLists(list1, list2):
    listOfDifference = []
    for index in range(len(list1)):
        listOfDifference.append(list1[index]-list2[index])
    return listOfDifference


# 20. Write a Python program access the index of a list.
def printIndexOfList(list):
    for index in range(len(list)):
        print(index, list[index])


# 21. Write a Python program to convert a list of characters into a string.
def convertListOfCharactersIntoString(list):
    string = ""
    for character in list:
        string += character
    return string


# 22. Write a Python program to find the index of an item in a specified list.
def getIndexOfSpecificItem(list, item):
    for index in range(len(list)):
        if list[index] == item:
            return index
    return None


# 23. Write a Python program to flatten a shallow list.
def getFlattenedList(list):
    newList = []
    for nestedList in list:
        for element in nestedList:
            newList.append(element)
    return newList


# 24. Write a Python program to append a list to the second list.
def appendListToAnotherList(list1, list2):
    for element in list2:
        list1.append(element)
    return list1


# 25. Write a Python program to select an item randomly from a list.
def getRandomElementFromList(list):
    return list[randint(0,len(list)-1)]


# 26. Write a python program to check whether two lists are circularly identical.
# 27. Write a Python program to find the second smallest number in a list.
def getSecondSmallestNumberFromList(list):
    uniqueNumbers=[]
    for element in list:
        if element not in uniqueNumbers:
            uniqueNumbers.append(element)
    uniqueNumbers.sort()
    return uniqueNumbers[1]


# 28. Write a Python program to find the second largest number in a list.
def getSecondLargestNumberFromList(list):
    uniqueNumbers=[]
    for element in list:
        if element not in uniqueNumbers:
            uniqueNumbers.append(element)
    uniqueNumbers.sort()
    return uniqueNumbers[-2]


# 29. Write a Python program to get unique values from a list.
def getUniqueValuesFromList(list):
    uniqueNumbers=[]
    for element in list:
        if element not in uniqueNumbers:
            uniqueNumbers.append(element)
    return uniqueNumbers


# 30. Write a Python program to get the frequency of the elements in a list.
def getFrequenceOfNumbersInList(list):
    frequency = {}
    frequency[list[0]] = 1
    for element in range(1,len(list)):
        if list[element] not in frequency:
            frequency[list[element]] = 1
        else:
            frequency[list[element]] += 1
    return frequency


# 31. Write a Python program to count the number of elements in a list within a specified range.
def getCountOfNumbersWithinRange(list, initialNumber, finalNumber):
    count=0
    for element in list:
        if element >= initialNumber and element <= finalNumber:
            count+=1
    return count


# 32. Write a Python program to check whether a list contains a sublist.
def checkIfSublistIsInMainList(mainList,subList):
    for element in subList:
        if element not in mainList:
            return False
    return True


# 33. Write a Python program to generate all sublists of a list.
# [1,2,3] erjonno hobe [[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
# 1. copy existing elements to result list.
# code:
#   resultList = 
# 2. add new element to previous lists.
# code:
#   for subList in resultList:
#       subList.append(element)
# 3. append new item as a list to result list.
# code:
#   resultList.append([element])
# 4. return result list.

def getSublistsFromlist(list, element):
    resultList = []
    temporaryList = resultList.copy()
    for subList in resultList:
        subList.append(element)


# evaluation
# listOfSubLists=[]
# listOfSubLists.append([list[0]])
# listOfSubLists.append(1)
# listOfSubLists = [[1]]
# print(listOfSubLists)
# for index in range(1,len(list)):
# for index in range(1,4):
# for index in [1,2,3,4]:
#   loop 1: index = 1
#       1. for previousNumbers in listOfSubLists:
#       2. for previousNumbers in [[1]]:
#       loop 1: previousNumbers = [1]
#           1. previousNumbers.append(list[index])
#           2. previousNumbers.append(list[1])


# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
# allNumbers korbo 2 theke lastNumber+1 porjonto
# 2 theke sheshNumber+1 porjonto:
#   abar 2 theke sheshNumber+1 porjonto:
#       jodi number*element compositeNumbers e na thake:
#           compositeNumbers e append korbo number*element
# allNumbers er sob element er jonno:
#   jodi element compositeNumbers e na thake:
#       primeNumbers e append
# return primeNumbers
def getPrimeNumbers(lastNumber):
    allNumbers=[]
    compositeNumbers = []
    primeNumbers = []
    for number in range(2, lastNumber+1):
        allNumbers.append(number)
    for number in range(2, lastNumber):
        for element in range(2,lastNumber):
            if number*element not in compositeNumbers and number*element <= lastNumber:
                compositeNumbers.append(number*element)
    for element in allNumbers:
        if element not in compositeNumbers:
            primeNumbers.append(element)
    return primeNumbers


# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n = 5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# resultList banabo.
#   1 theke n+1 er soman sonkhok iteration:
#       sample er list er proti ta element read korbo:
#           resultList e append(element + string of current n)
# return list
def getCustomizedList(list,n):
    resultList = []
    for number in range(1,n+1):
        for element in list:
            resultList.append(element+str(number))
    return resultList


# 36. Write a Python program to get variable unique identification number or string.
# randomString banabo.
# randomLength banabo.
# oi randomlength porjonto iterate:
#   randomNumberToGetInput banabo, from 1 to 2.
#   if 1:
#       randomString += chr(randint(A to z))
#   else:
#       randomString += chr(randint(0 to 9))
# return randomString
def getRandomizedString():
    randomString = ""
    for number in range(randint(4,10)):
        randomNumberToGetInput = randint(1,3)
        if randomNumberToGetInput == 1:
            randomString += chr(randint(65,90))
        elif randomNumberToGetInput == 2:
            randomString += chr(randint(97,122))
        else:
            randomString += chr(randint(48,57))
    return randomString


# 37. Write a Python program to find common items from two lists.
# first list er proti ta element er jonno:
#   jodi 2nd list e thake:
#       result list e append
# return resultlist
def getCommonElements(list1, list2):
    commonElements = []
    for element in list1:
        if element in list2:
            commonElements.append(element)
    return commonElements


# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
# length of list even.
# newList banabo.
# list er proti ta index er jonno iterate 0 theke and 2 baraye:
#   newList e append(index+1)
#   newList e append(index-1)
# return newList
def getResortedList(list):
    newList = []
    for index in range(0,len(list)-1,2):
        newList.append(list[index+1])
        newList.append(list[index])
    return newList


# 39. Write a Python program to convert a list of multiple integers into a single integer.
# string number banabo.
# list er proti ta element er jonno iterate:
#   number hobe number + string of element
# return int of number
def getConcatenatedNumber(list):
    stringNumber = ''
    for element in list:
        stringNumber += str(element)
    return int(stringNumber)


# 40. Write a Python program to split a list based on first character of word.
# string er first character resultString e.
# temporaryString banabo.
# 1 theke string er length porjonto iterate:
#   jodi string[index] " " na hoy:
#       temporaryString er sathe add
#   





# 41. Write a Python program to create multiple lists.
# resultList banabo
# random number porjonto iterate:
#   resultList e empty list append
# return resultList
def getMultipleLists():
    resultList = []
    for number in range(randint(5,10)):
        resultList.append([])
    return resultList


# 42. Write a Python program to find missing and additional values in two lists.
# missingElementsInList2 and extraElementsOfList1, if list1> list2
# missingElementsInList1 and extraElementsOfList2, if list2> list1
# if len of list1>len list2:
#   list1 er sobgula element er jonno:
#       jodi element list2 e na thake:
#           extraElementsOfList1.append(element)
#   list2 er sobgula element er jonno:
#       jodi element list1 e na thake:
#           
def getMissingAndExtraElements(list1,list2):
    missingElementsInList2 = []
    extraElementsOfList1 = []
    if len(list1) > len(list2):
        for element in list1:
            if element not in list2:
                missingElementsInList2.append(element)
            else:
                extraElementsOfList1.append(element)
        return missingElementsInList2, extraElementsOfList1
    missingElementsInList1 = []
    extraElementsOfList2 = []
    for element in list2:
        if element not in list1:
            missingElementsInList1.append(element)
        else:
            extraElementsOfList2.append(element)
    return missingElementsInList1, extraElementsOfList2


# 43. Write a Python program to split a list into different variables.
# list = [1,2,3]
# variable1 = 1
# variable2 = 2
# variable3 = 3
# 


# 44. Write a Python program to generate groups of five consecutive numbers in a list.
# result: list = [11,12,13,14,15]
# list = []
# for number in range(11,16):
#   list.append(number)
# return list
def getConsecutiveNumbers():
    list = []
    for number in range(11,16):
        list.append(number)
    return list


# 45. Write a Python program to convert a pair of values into a sorted unique array.
# pair of values = (20,25)
# list = [20,21,22,23,24,25]
# method input: pair = (20,25)
# method:
#   lowerNumber = min(pair)
#   higherNumber = max(pair)
#   list = []
#   for number in range(lowerNumber, higherNumber+1):
#       list.append(number)
#   return list
def getSortedUniqueNumbers(pair):
    lowerNumber = min(pair)
    higherNumber = max(pair)
    list = []
    for number in range(lowerNumber, higherNumber+1):
        list.append(number)
    return list


# 46. Write a Python program to select the odd items of a list.
# oddNumbers = []
# for number in list:
#   if number%2 != 0:
#       oddNumbers.append(number)
#   return oddNumbers
def getOddNumbers(list):
    oddNumbers = []
    for number in list:
        if number%2 != 0:
            oddNumbers.append(number)
        return oddNumbers


# 47. Write a Python program to insert an element before each element of a list.
# input: list, element
# modifiedList = []
# list er proti ta data er jonno:
#   modifiedList e element add
#   modifiedList e data add
# return modifiedList
def addElementBeforeListData(list, element):
    modifiedList = []
    for data in list:
        modifiedList.append(element)
        modifiedList.append(data)
    return modifiedList


# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
# for subList in list:
#   prin(subList)
def printElementsInList(list):
    for subList in list:
        print(subList)


# evaluation:
# for sublist in list:
# for sublist in [[1],[2],[3]]:
# loop 1: sublist = [1]
#   print([1])
# loop 2: subList = [2]
#   print([2])
# loop 3: subList = [3]
#   print([3])
# .........?


# 49. Write a Python program to convert list to list of dictionaries.
# names, heights
# dictionary = {}
# for index in range(len(names)):
#   dictionary er key hobe names er current index and value hobe heights er current index.
# return dictionary
def getDictionary(names, heights):
    dictionary = {}
    for index in range(len(names)):
        dictionary[names[index]] = heights[index]
    return dictionary


# 50. Write a Python program to sort a list of nested dictionaries.
# list er proti ta element er jonno:
#   element(dictionary) er proti ta value er jonno:
#       value(nested dict) er proti ta value er jonno:
#           jodi 1st value>2nd value hoy:
#               temporaryValue = lower value wala list element.
#               lowerValue wala list element er index e higherValue wala index element set korbo.
#               highervalue te temporary value set korbo.



# 51. Write a Python program to split a list every Nth element.
# input: list, n
# result = []
# temporaryList = []
# list er proti ta element er jonno:
#   tempo te add
#   jodi tempo er length == n hoy:
#       result e add korbo tempo
#       tempo = []
def splitList(list, n):
    result = []
    temporaryList = []
    for element in list:
        temporaryList.append(element)
        if len(temporaryList) == n:
            result.append(temporaryList)
            temporaryList = []
    if temporaryList != []:
        result.append(temporaryList)
    return result



# 52. Write a Python program to compute the similarity between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
# result = {}
# extraElementsOfList1 = []
# extraElementsOfList2 = []
# list1 er sob element er jonno:
#   jodi element list2 e na thake:
#       extraElementsOfList1 e append
# list2 er sob element er jonno:
#   jodi list1 e element na thake:
#       extraElementsOfList2 e append
# result['list1-list2'] = extraElementsOfList1
# result['list2-list1'] = extraElementsOfList2
# return result
def getListSimilarities(list1, list2):
    result = {}
    extraElementsOfList1 = []
    extraElementsOfList2 = []
    for element in list1:
        if element not in list2:
            extraElementsOfList1.append(element)
    for element in list2:
        if element not in list1:
            extraElementsOfList2.append(element)
    result['list1-list2'] = extraElementsOfList1
    result['list2-list1'] = extraElementsOfList2
    return result


# 53. Write a Python program to create a list with infinite elements.
# list = []
# number = 0
# infinite loop:
#   list.append(number)
#   number += 1
def createInfiniteElements():
    list = []
    number = 0
    while(True):
        list.append(number)
        number += 1


# 54. Write a Python program to concatenate elements of a list.
# input list
# returnString = ''
# for element in list:
#   returnstring e add
# return returnstring
def concatenateListElements(list):
    returnString = ''
    for element in list:
        returnString += element
    return returnString


# time: O(n)
# space: 1


# 55. Write a Python program to remove key values pairs from a list of dictionaries.
# ekta ekta kore dictionary access korbo list theke.
#   remove key value pair

def getUpdatedDictionariesFromList(items, name):
    for item in items:
        removePairFromDictionary(item, name)
    return items


# time: O(n)
# space: n+1+n+1=2n+2
    
# items er proti ta key value er jonno:
#   jodi key name er soman hoy:
#       oi key value pair ta delete.
#       break
def removePairFromDictionary(items, name):
    for key in items.keys():
        if key == name:
            del items[key]
            break


# time: O(n)
# space: n+1

# 56. Write a Python program to convert a string to a list.
# list = []
# string er proti ta character er jonno:
#   list e character jog
# return list
def convertStringToList(string):
    list = []
    for character in string:
        list.append(character)
    return list

# time: O(n), n= length of string
# space: 1+n


# 57. Write a Python program to check whether all items of a list is equal to a given string.
# temporaryString = ''
# for element in list:
#   temporarystring e element add
# if tempo == string:
#   return True
# return False
def checkIfElementsBelongInList(string, list):
    temporarystring = ""
    for element in list:
        temporarystring += element
    if temporarystring == string:
        return True
    return False

# time complexity: O(n)
# space complexity: 1+n+n=2n+1


# 58. Write a Python program to replace the last element in a list with another list. 
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
# input: list1, list2
# return list
# list = []
# list1 er shesh element er ager element porjonto:
#   list e sob append
# list2 er sob element er jonno:
#   list e list2 append
# return list   
def replaceLastElementWithList(list1, list2):
    list = []
    for index in range(len(list1)-1):
        list.append(list1[index])
    for element in list2:
        list.append(element)
    return list

# time complexity: O(n), n= lenght of highest list
# space complexity: n+n+n-1+n = 3n-1

# 59. Write a Python program to check whether the n-th element exists in a given list.
# input: n, element, list
# if n<len(list) and list[n-1] == element:
#   return True
# return False
def checkIfNthElementExists(n, element, list):
    if n < len(list) and list[n-1] == element:
        return True
    return False

# time complexity: O(1)
# space complexity: 1+1+n=n+2


# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# tuple = ()
# list er length er ag porjonto proti ta index er jonno:
#   if list[index][1] < list[index+1][1]:
#       tuple = list[index][1]
def getLeastSecondIndexedTuple(list):
    for index in range(len(list)-1):
        if list[index][1] < list[index+1][1]:
            tuple = list[index]
        else:
            tuple = list[index+1]
    return tuple

# time complexity: O(n)
# space complexity: O(n)


# 61. Write a Python program to create a list of empty dictionaries.
# list = []
# 10 porjonto iterate:
#   list e empty dict append
# return list
def getEMptyDictionaries():
    list = []
    for number in range(10):
        list.append({})
    return list

# time complexity: O(1)
# space complexity: O(1)

# 62. Write a Python program to print a list of space-separated elements.
# input: none
# return: list
# method:
#   spacedNumbers
#   1 theke 10 porjonto iterate:
#       spacedNumbers e append number
#       spacedNumbers e append space
#   return spacedNumbers
def getSpacedNumbers():
    spacedNumbers = []
    for number in range(1,11):
        spacedNumbers.append(number)
        spacedNumbers.append(" ")
    return spacedNumbers

# print(getEMptyDictionaries())

# reverse list
# input: list
# output: list
# method:
# reversed list define korbo.
# list er shesh index-1 theke -1 er jonno 1 kore index komabo:
#   reversed list e index er element add korbo.
# return reverse list
def reverseList(list):
    reverseList = []
    for index in range(len(list)-1,-1,-1):
        reverseList.append(list[index])
    return reverseList


# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# input: list, string
# return: list
# method:
#   appendedList
#   list er sob element er jonno:
#       appendedList e append(string+str(element))
#   return appendedList
def getAppendedList(numbers, name):
    appendedList = []
    for element in numbers:
        appendedList.append(name+str(element))
    return appendedList


print(getAppendedList([1,2,3,4],'ayon'))

# time complexity: O(n), n = length of list
# space complexity: 
# 1. executed once
# 2. for loop executed n times at worst case, 0 times at best
# 3. append executed n times at worst case, 0 times at best
# 4. return executed once
# total: 1 + N^2 + N^2 + 1 = 2*N^2 + 2 at worst, 2 at best  