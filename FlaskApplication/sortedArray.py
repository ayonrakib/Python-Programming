# getSortedArray
# input: 2 arrays
# return: one sorted array
# method:
#   duita array jog korbo
#   temporaryVariable banabo
#   numberOfItems hobe concatenatedArray er length
#   0 theke numberOfItems porjonto iterate:
#       abar concatenatedarray er sob index er jonno iterate:
#       jodi concatenatedarray[index] > concatenatedarray[index]+1 hoy:
#           temporaryVariable = concatenatedarray[index]
#           concatenatedarray[index] = concatenatedarray[index+1]
#           concatenatedarray[index+1] = temporaryVariable
#   return concatenatedarray
# def getSortedArray(array1, array2):
#     if str(type(array1)) != "<class 'list'>":
#         raise Exception("1st Array is not a list.")
#     if str(type(array2)) != "<class 'list'>":
#         raise Exception("2nd Array is not a list.")
#     for element in array1:
#         if str(type(element)) != "<class 'int'>":
#             raise Exception("element in 1st array has to be integer.")
#     for element in array2:
#         if str(type(element)) != "<class 'int'>":
#             raise Exception("element in 2nd array has to be integer.")
#     concatenatedArray = array1 + array2
#     numberOfItems = len(concatenatedArray)
#     for number in range(numberOfItems):
#         for index in range(len(concatenatedArray)-1):
#             if concatenatedArray[index] > concatenatedArray[index+1]:
#                 temporaryVariable = concatenatedArray[index]
#                 concatenatedArray[index] = concatenatedArray[index+1]
#                 concatenatedArray[index+1] = temporaryVariable
#     return concatenatedArray

# time complexity: O(n^2)


# quicksort
# input: 2 sorted arrays
# return: sorted array
# method:
#   1. jodi jekono ekta array empty hoy, baki ta send korbo.
#   2. non empty array duitar element gula compare kore sortedarray te append korbo
#   3. jodi kono array er extra element thake, sortedarray te append korbo oi array er baki element gula.


#   #. jodi jekono ekta array empty hoy, baki ta send korbo.
#   1. jodi first array empty hoy, return second array.
#   2. jodi second array empty hoy, return first array.


#   #. non empty array duitar element gula compare kore sortedarray te append korbo
#   1. empty sortedarray
#   2. while i <= firsarrraylength and j<= secondarraylength:
#       3. jodi firstarray[i] <= secondarray[j]:
#           4. sortedarray te append firstarray[i]
#           5. i++
#       6. else:
#           7. sortedarray te append secondarray[j]
#           8. j++


#   #. jodi kono array er extra element thake, sortedarray te append korbo oi array er baki element gula.
#   1. jodi i <= firsarrraylength and j== secondarraylength:
#       2. call append function (sortedArray, arrayToBeAppended -> firstarray, index -> i)
#   3. else:
#       4. call append function (sortedArray, arrayToBeAppended - > secondarray, index -> j)
#   return
def sortedArray(firstArray, secondArray):
    if firstArray == []:
        return secondArray
    if secondArray == []:
        return firstArray
    sortedArray = []
    i = 0
    j = 0
    while(i<=len(firstArray) and j<=len(secondArray)):
        if firstArray[i] < secondArray[j]:
            sortedArray.append(firstArray[i])
            i+=1
        elif 