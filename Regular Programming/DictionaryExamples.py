# pylint: disable=unused-variable
# pylint: enable=too-many-lines
import sys
class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def __str__(self):
        pass
# 1. Write a Python script to sort (ascending and descending) a profile by value.
# sortByIncreasingValue
# profile = {'a':5,'b':2,'c':-3}
#   temporaryKey = ['a','b']
#   temporaryValue = [5,2]
#   5 > 2 so:
#       temporarydict{tempkey[0]} = tempvalue[0]
#       dict{tempkey[0]} = dict{tempvalue[0]} 
# input: dict
# return: dict
# method:
#   temporaryprofile = {}
#   temporaryKey = []
#   temporaryValue = []
#   count = 0
#   dict er proti ta initial key initial value er jonno:
#       dict er proti ta key value er jonno:
#           count += 1
#           temporaryKey e append(key)
#           temporaryValue e append(value)
#           jodi count 2 hoy(2 bar loop ghurse):
#               jodi temporaryValue[0] > temporaryValue[1] hoy:
#                   temporaryprofile[key] 


# 2. Write a Python script to add a key to a profile.
# addKeyValuePair
# input: dict, key, value
# return: true if done, false if not
# method:
#   jodi key dict e thake:
#       false
#   dict[key] = value
#   true
def addKeyValuePair(profile, key, value):
    if key in profile:
        return False
    profile[key] = value
    print(profile)
    return True


# 3. 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
# Sample profile :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# input: dic1, dic2, dic3
# return: appendedDic
# method:
#   appendedDic empty dic
#   dic1 er sob key value pair er jonno:
#       jodi key exist na kore:
#           appendedDic[key] = value
#   dic2 er sob key value pair er jonno:
#       jodi key exist na kore:
#           appendedDic[key] = value
#   dic3 er sob key value pair er jonno:
#       jodi key exist na kore:
#           appendedDic[key] = value
#   return
def concatenateDictionaries(dic1, dic2, dic3):
    appendedDic = {}
    for key, value in dic1.items():
        if key not in appendedDic:
            appendedDic[key] = value
    for key, value in dic2.items():
        if key not in appendedDic:
            appendedDic[key] = value
    for key, value in dic3.items():
        if key not in appendedDic:
            appendedDic[key] = value
    return True


# 4. Write a Python script to check whether a given key already exists in a profile.
# input: dict, key
# return: true if found, false if not
# method:
#   if key in dict:
#       true
#   false
def chekcIfKeyExists(profile, key):
    if key in profile:
        return True
    return False


# 5. Write a Python program to iterate over dictionaries using for loops.
# input: dict
# return: nothing
# method:
#   dict er key value er jonno:
#       print(key, value)
def iterateOverprofile(profile):
    for key, value in profile:
        print(key, value)

    
# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
# getDictionary
# input: n
# return: dict
# method:
#   profile empty dic
#   1 theke n+1 porjonto iterate:
#       profile[n] = n*n
#   return profile
def getDictionary(n):
    profile = {}
    for number in range(1, n+1):
        profile[number] = number * number
    return profile


# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
# valuesquareofkeys
# input: none
# return: dict
# method:
#   profile empty dic
#   1 theke 16 porjonto iterate:
#       profile[current] = current *current
#   profile return
def valueSquareOfKeys():
    profile = {}
    for number in range(1, 16):
        profile[number] = number * number
    return profile


# 8. Write a Python script to merge two Python dictionaries.
# mergeTwoDicts
# input: dic1, dic2
# return: mergedDic
# method:
#   mergedDic empty dic
#   dic1 er key value er jonno:
#       mergedDic[key] = value
#   dic2 er key value er jonno:
#       mergedDic[key] = value
#   return
def mergeTwoDicts(dic1, dic2):
    mergedDic = {} 
    for key, value in dic1.items():
        mergedDic[key] = value
    for key, value in dic2.items():
        mergedDic[key] = value
    return mergedDic


# 9. Write a Python program to iterate over dictionaries using for loops.
# input: dict
# return: none
# method:
#   dict er sob key, value er jonno:
#       print(key, value)
def iterateOverDictionary(profile):
    for key,value in profile.items():
        print(key, value)


# 10. Write a Python program to sum all the items in a dictionary.
# input: dict
# return: dict
# method:
#   result
#   dict er sob value er jonno:
#       result er sathe value add
#   return result
def getSumOfValues(profile):
    result = 0
    for value in profile.values():
        result += value
    return result


# 11. Write a Python program to multiply all the items in a dictionary.
# input: dict
# return: dict
# method:
#   result
#   dict er sob value er jonno:
#       result er sathe value multiply
#   return result
def getMultiplicationOfValues(profile):
    result = 1
    for value in profile.values():
        result *= value
    return result


# 12. Write a Python program to remove a key from a dictionary.
# key remove korar pore, jodi key khuje na pai, taile true otherwise false
# input: dict, keyToBeDeleted
# return:modifieddict
# method:
#   newProfile = {}
#   dict er sob key, value er jonno:
#       jodi key keyToBeDeleted er soman na hoy:
#           newProfile[key] = value
#   newProfile er sob key er jonno:
#       jodi key == keyToBeDeleted:
#           return false
#   return true
def removeKeyFromDictionary(profile, keyToBeDeleted):
    newProfile = {}
    for key, value in profile.items():
        if key != keyToBeDeleted:
            newProfile[key] = value
    for key in newProfile.keys():
        if key == keyToBeDeleted:
            return False
    return True


# 13. Write a Python program to map two lists into a dictionary.
# input: two lists
# return: mapped dict
# method:
#   jodi duita list er len soman na hoy:
#       return false
#   mappedDictionary
#   jekono ekta list er sob index er jonno:
#       mappedDictionary[list1[index]] = list2[index]
#   return mappedDictionary
def getMappedDictionary(names, ages):
    if len(names) != len(ages):
        return False
    mappedDictionary = {}
    for index in range(len(names)):
        mappedDictionary[names[index]] = ages[index]
    return mappedDictionary


# 14. Write a Python program to sort a dictionary by key.
# input: profile
# return: sortedDict
# method:
#   currentSmallestKey, currentSmallestValue
#   for key in profile.keys:
#       if key < currentSmallestKey:
#           

# 15. Write a Python program to get the maximum and minimum value in a dictionary.
# getMaximumAndMinimumValue
# input: dict
# output: maximum value, minimum value
# method:
#   dict er proti ta value er jonno:
#       maximumValue = value
#       minimumValue = value
#       break
#   dict er proti ta value er jonno:
#       if value <= minimumValue:
#           minimumValue = value
#       elif value > maximumValue:
#           maximumValue = value
def getMaximumAndMinimumValue(profile):
    for value in profile.values():
        maximumValue = value
        minimumValue = value
        break
    for value in profile.values():
        if value <= minimumValue:
            minimumValue = value
        elif value > maximumValue:
            maximumValue = value
    return maximumValue, minimumValue


# 16. Write a Python program to get a dictionary from an object's fields.
# input: object
# return: dictionary
# method:
#   return korbo inputobject.__dict__
def getObjectProperties(humanObject):
    propertyDictionary = humanObject.__dict__
    newPropertyDictionary = {}
    for key,value in propertyDictionary.items():
        newPropertyDictionary[key] = value
    return newPropertyDictionary 


# ayon = Human("Ayon",25)
# ayon.age = 12
# print(getObjectProperties(ayon))


# change the value of a key of the returned dictionary
# input: object
# return: dictionary
# method:
#   propertyDictionary hobe object.__dict__
#   newPropertyDictionary banabo
#   propertyDictionary er sob key value er jonno:
#       newPropertyDictionary[key] = value
#   return newPropertyDictionary
# class Human theke ayon object banabo
# getObjectProperties(ayon) er return value store korbo propertyDictionary te
# newPropertyDictionary[key] er value banabo.
# print kore dekhbo newPropertyDictionary ta



# ayon = Human("Ayon",30)
# propertyDictionary = getObjectProperties(ayon)
# propertyDictionary["age"] = 40
# print(propertyDictionary)
# print(ayon.age)



# 1. ayon = Human("Ayon",30)
# 2. ayon = x12345
# 3. propertyDictionary = getObjectProperties(ayon)
# 4. propertyDictionary = getObjectProperties(x12345)
# 5. def getObjectProperties(humanObject):
# 6.    humanObject = x12345
# 7.    return humanObject.__dict__
# 8.    return x12345.__dict__
# 9.    return {"name":"Ayon", "Age":30}
# 10. propertyDictionary = {"name":"Ayon", "Age":30}
# 11. propertyDictionary["age"] = 40
# 12. propertyDictionary = {"name":"Ayon", "Age":40}
# 13. print(propertyDictionary)
# 14. print({"name":"Ayon", "Age":40})
# 15. print(ayon.age)
# 16. print(x12345.age)
# 17. print(x12345.__dict__["Age"])
# 18. print(40)


# 17. Write a Python program to remove duplicates from Dictionary.
# input: dict
# return: dict with unique values
# method:
#   uniqueValuedDictionary
#   dict er sob key,value er jonno:
#       jodi uniqueValuedDictionary.values() e value na thake:
#           uniqueValuedDictionary[key] = value
#   return uniqueValuedDictionary
def getUniqueValuedDictionary(profile):
    uniqueValuedDictionary = {}
    for key,value in profile.items():
        if value not in uniqueValuedDictionary.values():
            uniqueValuedDictionary[key] = value
    return uniqueValuedDictionary


# 18. Write a Python program to check a dictionary is empty or not.
# input: dict
# return: boolean. true if empty, false if not
# method:
#   if input is {}:
#       return true
#   return false
def checkIfDictionaryIsEmpty(data):
    if data == {}:
        return True
    return False


# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# input: 2 dicts
# return: dict
# method:
#   addedDictionary banabo
#   dict1 er sob key value er jonno:
#       jodi key thake addedDictionary.keys e:
#           addedDictionary[key] += value
#       else:
#           addedDictionary[key] = value
#   dict2 er sob key value er jonno:
#       jodi key thake addedDictionary.keys e:
#           addedDictionary[key] += value
#       else:
#           addedDictionary[key] = value
def addCommonKeys(data1, data2):
    addedDictionary = {}
    for key,value in data1.items():
        if key in addedDictionary.keys():
            addedDictionary[key] += value
        else:
            addedDictionary[key] = value
    for key,value in data2.items():
        if key in addedDictionary.keys():
            addedDictionary[key] += value
        else:
            addedDictionary[key] = value
    return addedDictionary


# 20. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
# input:dict
# return: set
# method:
#   empty set uniqueValueSet
#   list er sob dict er jonno:
#       dict er sob value er jonno:
#           jodi value set e na thake:
#               uniqueValueSet e append korbo value
#   return uniqueValueSet
def getUniqueValuedSet(data):
    uniqueValueSet = set()
    for element in data:
        for value in element.values():
            if value not in uniqueValueSet:
                uniqueValueSet.add(value)
    return uniqueValueSet


# print(getUniqueValuedSet([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))
# udaharon howa lagbe meaningful. jemon, ekta dictionary hoite pare sobar salary: ayon: 50000 golam:80000 eivabe. eitar naam hobe salaryDictionary


# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

# method: getAllCombinationOfLetters
# input:  stringToList {'1':['a','b','c'], '2':['d','e','f'],'3':['g','h']}
# return: words ["adg","adh","aeg","aeh","afg","afh",...]
# top down method:
#   function addNewCharactersToWords
#   input: previousWords, newCharacters
#   output: newWords
#   method:
#       outputWords empty list
#       previousWords er proti ta word er jonno:
#           newCharacters er proti ta charcter er jonno:
#               outputWords e append (previousWordsCharacter+newCharactersCharacter)  
#       return outputWords
def addNewCharactersToWords(previousWords, newCharaceters):
    if previousWords == []:
        return newCharaceters
    if newCharaceters == []:
        return previousWords
    outputWords = []
    for word in previousWords:
        for newCharacetersCharacter in newCharaceters:
            outputWords.append(word + newCharacetersCharacter)
    return outputWords

# 1. def addNewCharactersToWords(previousWords, newCharaceters):
#   2. previousWords = []
#   3. newCharaceters = ['a','b']
#   4. outputWords = []
#   5. for previousWordsCharacter in previousWords:
#       6. loop 1: previousWordsCharacter =[]
#       7. for newCharacetersCharacter in newCharaceters:
#           8. loop 1:
#           9. newCharacetersCharacter = 'a'
#           10. outputWords.append(previousWordsCharacter+newCharacetersCharacter)
#           11. outputWords.append([]+newCharacetersCharacter)
#           12. outputWords.append([]+'a')

# function getAllCombinationOfLetters
# input: stringToList
# return: words
# method:
#   previousWords empty list
#   stringToList er proti ta newCharacters er jonno:
#       previousWords = addNewCharactersToWords(previousWords, newCharaceters)
#   return previousWords

def getAllCombinationOfLetters(stringToList):
    if stringToList == {}:
        return None
    previousWords = []
    for newCharacters in stringToList.values():
        previousWords = addNewCharactersToWords(previousWords, newCharacters)
    return previousWords


# print(getAllCombinationOfLetters({'1':['a','b','c'], '2':['d','e','f'],'3':['g','h']}))
# print(getAllCombinationOfLetters({'1':['a','b','c'], '2':[],'3':['g','h']}))


# 1. def getAllCombinationOfLetters(stringToList):
#   2. stringToList = {'1':['a','b'], '2':['c','d']}
#   3. temporaryCharactersList = []
#   4. previousWords = []
#   5. for characters in stringToList.values():
#       6. loop 1:
#           7. characters = ['a','b']
#           8. temporaryCharactersList.append(characters)
#           9. temporaryCharactersList.append(['a','b'])
#           10. temporaryCharactersList = ['a','b']
#       11. loop 2:
#           12. characters = ['c','d']
#           13. temporaryCharactersList.append(characters)
#           14. temporaryCharactersList.append(['c','d'])
#           15. temporaryCharactersList = [['a','b'], ['c','d']]
#   16. for newCharacters in temporaryCharactersList:
#       17. loop 1:
#           18. newCharacters = ['a','b']
#           19. 




# 22. Write a Python program to find the highest 3 values in a dictionary
# input: nameToNumbers = {"Ayon": 1000, "Rakib": 200, "Hasan": 500, "Golam": 600, "Md": 900, "Muktadir": 1250}
# return: highest three numbers
# method:
#   temporaryHighestNumber integer
#   randomNumbers list
#   nameToNumbers er sob value er jonno:
#       randomNumbers e append value
#   if randomNumbers er length < 3:
#       return randomNumbers
#   randomNumbers er length porjonto:
#       abar randomNumbers er length-1 porjonto:
#           jodi randomNumbers[index] < randomNumbers[index+1] hoy:
#               temporaryHighestNumber = randomNumbers[index+1]
#               randomNumbers[index+1] = randomNumbers[index]
#               randomNumbers[index] = temporaryHighestNumber
#   return randomNumbers[0], randomNumbers[1], randomNumbers[2]
def getThreeHighestNumbers(nameToNumbers):
    temporaryHighestNumber = 0
    randomNumbers = []
    for number in nameToNumbers.values():
        randomNumbers.append(number)
    for position in range(len(randomNumbers)):
        for index in range(len(randomNumbers)-1):
            if randomNumbers[index] < randomNumbers[index+1]:
                temporaryHighestNumber = randomNumbers[index+1]
                randomNumbers[index+1] = randomNumbers[index]
                randomNumbers[index] = temporaryHighestNumber
    return randomNumbers[0], randomNumbers[1], randomNumbers[2]

# corner case: jodi non unique value thake, taile ki korbo
# sorting method


# print(getThreeHighestNumbers({"Ayon": 1000, "Rakib": 200, "Hasan": 500, "Golam": 600, "Md": 900, "Muktadir": 1250}))

# 23. Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
# getCombinedValues
# input: itemToNumberList
# return: combined valued dict
# method:
#   combinedValues empty dict
#   itemToNumberList er sob element er jonno:
#       element er sob key value er jonno:
#           jodi key item hoy:
#               jodi combinedValues e element["item"] key na thake:
#                   combinedValues[element[item]] = element[amount]
#               othoba:
#                   combinedValues[element[item]] += element[amount]
#   return combinedValues
def getCombinedValues(itemToNumberList):
    combinedValues = {}
    for element in itemToNumberList:
        for key, value in element.items():
            if key == "item":
                if element["item"] not in combinedValues.keys():
                    combinedValues[element["item"]] = element["amount"]
                else:
                    combinedValues[element["item"]] += element["amount"]
    return combinedValues

# n=2 er jonno solve kora jabe kina

# print(getCombinedValues([{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]))


# 24. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# getDictionaryFromSentence
# input: sentence
# return: dictionary with the count of characters
# method:
#   countOfCharacters empty dict
#   sentence er sob character er jonno:
#       jodi character getDictionaryFromSentence er key te na thake:
#           getDictionaryFromSentence[character] = 0
#       else:
#           getDictionaryFromSentence[character]+=1
#   return getDictionaryFromSentence
def getDictionaryFromSentence(sentence):
    countOfCharacters = {}
    for character in sentence:
        if character not in countOfCharacters.keys():
            countOfCharacters[character] = 1
        else:
            countOfCharacters[character] += 1
    return countOfCharacters


# print(getDictionaryFromSentence('w3resource'))


# 25. Write a Python program to print a dictionary in table format.
# {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
# input: sampleDictionary
# return: nothing, just print
# method:
#   keyString, valueString
#   sampleDictionary er sob key er jonno:
#      keyString e key add plus maximum number space
#   print keyString
#   sampleDictionary er sob value er jonno:
#       listOfValues e append listOfValues
#   value empty string
#   listOfValues er sob values er jonno:
#       values er sob element er jonno:
#           valuer te add element er str and space plus maximum number space
#       value e add newline -> eita pore dibo na, aage dibo
#   print(newline)
def printTableFromDictionary(dictionary):
    keyString = ""
    valueString = ""
    listOfValues = []
    for key in dictionary.keys():
        keyString += key + " "
    print(keyString)
    for value in dictionary.values():
        listOfValues.append(value)
    value = ""
    for values in listOfValues:
        for element in values:
            value += str(element) + " "
        value += str("\n")
    print(value)


# printTableFromDictionary({'C1':[1,2,3],'C2':[5,6,7],'C3':[9,100000000,11]})


# 26. Write a Python program to count the values associated with key in a dictionary. 
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

# getNumberOfDictionaryWithValidCondition
# input: dictionaries, targetKey, targetValue
# return: numberOfDictionaryWithValidCondition as integer
# method:
#   numberOfDictionaryWithValidCondition is 0
#   dictionaries er sob dictionary er jonno:
#       dictionary er sob key, value pair er jonno:
#           jodi key = targetKey and value = taregtValue hoy:
#               numberOfDictionaryWithValidCondition += 1
#   return numberOfDictionaryWithValidCondition
def getNumberOfDictionaryWithValidCondition(dictionaries, targetKey, targetValue):
    numberOfDictionaryWithValidCondition = 0
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            if key == targetKey and value == targetValue:
                numberOfDictionaryWithValidCondition += 1
    return numberOfDictionaryWithValidCondition


# print(getNumberOfDictionaryWithValidCondition([{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}], "success", True))


# 27. Write a Python program to convert a list into a nested dictionary of keys.
# input: [1, 2, 3, 4]
# return: nestedDictionary {1: {2: {3: {4: {}}}}}
# method:
#   recursive method
#   induction method: use for n-1, will get answer for n
#   try with [1,2] get {1:{2:{}}}
#   index 0 er jonno:
#       {index 0 element: value}
#   index 1 er jonno:
#       {index 0 er element: {index 1 er element: value}}
#       jehetu last index, value hobe empty dict.
#   so final result: {index 0 er element: {index 1 er element: {}}}
#   2 functions: 1st one makes nested value
#   2nd one makes the entire dict
#   getNestedValue
#   input: index, list
#   return: {} if last index, {index: self function call} for others
#   method:
#       if index is last index:
#           return {}
#       return {list[index]: self function call with index+1 and list as parameter}
#   getListToDict
#   input: list
#   return: nested dict
#   method:
#       return getNestedValue(0, inputlist)
def getNestedValue(index, list):
    if index == len(list):
        return {}
    return {list[index]: getNestedValue(index+1, list)}


def getListToDict(list):
    return getNestedValue(0, list)


# print(getListToDict([1]))


# 28. Write a Python program to sort a list alphabetically in a dictionary.
# input: {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# return: {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
# method:
#   dont use n^2, use sorting method like merge sort


# 29. Write a Python program to remove spaces from dictionary keys.
# input: {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# return: {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}
# removeSpaceInKeys
# input: dictionary
# return: True if done, false if not
# method:
#   temporaryKeyString
#   modifiedDictionary
#   input er sob key value pair er jonno:
#       key er sob character er jonno:
#           jodi character space na hoy othoba tab na hoy othoba newline na hoy:
#               temporaryKeyString e add
#       modifiedDictionary[temporaryKeyString] = value
#       temporaryKeyString = ""
#   return modifiedDictionary
def removeSpaceInKeys(dictionary):
    temporaryKeyString = ""
    modifiedDictionary = {}
    for key, value in dictionary.items():
        for character in key:
            if character != ' ' and character != "\t" and character != "\n":
                temporaryKeyString += character
        modifiedDictionary[temporaryKeyString] = value
        temporaryKeyString = ""
    return modifiedDictionary


# print(removeSpaceInKeys({'S   001': ['Math', 'Science'], 'S    002': ['Math', 'English']}))


# 30. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
# sorting method


# 31. Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6
# getKeyValueAndItem
# input: keyValueCount
# return: nothing, just print
# method:
#   space = maximum possible integer
#   print(sys.maxsize) - 9223372036854775807
#   maximumSpace = ""
#   19 bar loop ghuraye:
#       maximumSpace += " "
#   print("key" + maximumSpace + "value" + maximumSpace + "count")
#   count = 1
#   keyValueCount er sob key value er jonno:
#       print(str(key) + maximumSpace + str(value) + maximumSpace + str(count))
#       count ++
def getKeyValueAndItem(keyValueCount):
    maximumSpace = ""
    for count in range(19):
        maximumSpace += " "
    print("key" + maximumSpace + "value" + maximumSpace + "count")
    count = 1
    for key, value in keyValueCount.items():
        print(str(key) + maximumSpace + "  " + str(value) + "   " + maximumSpace + str(count))
        count += 1


# getKeyValueAndItem({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})


# 32. Print a dictionary line by line
# sample input: { 'Aex': {'class':'V', 'rolld_id':2} , 'Puja' : {'class':'V', 'roll_id':3} }
# print:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3
# method:
#   temporaryLine = ""
#   nestedDict er sob key value(dict) er jonno:
#       print(key)
#       dict er sob key value pair er jonno:
#           temporaryLine += str(key) + " : " + str(value)
#           print(temporaryLine)
#           temporaryLine = ""


def printDictionaryLineByLine(nestedDictionary):
    temporaryLine = ""
    for key, dictionary in nestedDictionary.items():
        print(key)
        for key, value in dictionary.items():
            temporaryLine += str(key) + " : " + str(value)
            print(temporaryLine)
            temporaryLine =""


# printDictionaryLineByLine({ 'Aex': {'class':'V', 'rolld_id':2} , 'Puja' : {'class':'V', 'roll_id':3} })


# 33. Write a Python program to check multiple keys exists in a dictionary.
# sample input: student = { 'name': 'Alex', 'class': 'V','roll_id': '2' }
# return: 


# 34. Write a Python program to count number of items in a dictionary value that is a list.
# sample input: dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# sample return: 5
# method:
#   countElementsInDictionaryValueList
#   input: dict
#   return: integer
#   method:
#       totalElements
#       input er sob value er jonno:
#           jodi value er type list hoy:
#               value er sob element er jonno:
#                   totalElements++
#       return totalElements
def countElementsInDictionaryValueList(dict):
    totalElements = 0
    for value in dict.values():
        if isinstance(value, list):
            for element in value:
                totalElements += 1
    return totalElements


# print(countElementsInDictionaryValueList({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}))

# 35. Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]


# 36. Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
# createDictionaryFromLists
# input: 2 lists as keys and values
# return: dict
# method:
#   jodi dui list er length soman na hoy:
#       return None
#   newDictionary
#   jekono ekta list er length soman iterate:
#       newDictionary[key[index]] = value[index]
#   return newDictionary
def createDictionaryFromLists(keys, values):
    if len(keys) != len(values):
        return None
    newDictionary = {}
    for index in range(len(keys)):
        newDictionary[keys[index]] = values[index]
    return newDictionary


# print(createDictionaryFromLists(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]))

# 37. Write a Python program to replace dictionary values with their average.
# sample input: {'Class-V': 1, 'Class-VI': 2, 'Class-VII': 2, 'Class-VIII': 3} as input dict
# sample return: 2 as int
# replaceWithAverageValue
# method:
#   sum, totalNumbers, average
#   for all values in inputDict:
#       sum += values
#       totalNumbers++
#   totalNumbers 0 hoile return None
#   if totalNumbers == 1:
#       average = value
#   average = sum/totalNumbers
#   inputDict er sob key,value er jonno:
#       inputDict[key] = average
#   return inputDict
def replaceValueWithAverageValue(inputDict):
    sum = 0
    totalNumbers = 0
    average = 0
    for value in inputDict.values():
        sum += value
        totalNumbers += 1
    if totalNumbers == 0:
        return None
    if totalNumbers == 1:
        for key in inputDict.keys():
            inputDict[key] = sum
    average = sum / totalNumbers
    for key in inputDict.keys():
        inputDict[key] = average
    return inputDict


# print(replaceValueWithAverageValue({}))


# 38. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# getMatchingKeys
# input: 2 dicts
# return: list of matching keys
# method:
#   matchedKeys []
#   firstDictionaryKeys secondDictionaryKeys
#   firstDict er sob key er jonno:
#       firstDictionaryKeys e append key
#   secondDict er sob key er jonno:
#       secondDictionaryKeys e append key
#   