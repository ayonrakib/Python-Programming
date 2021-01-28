# hash map
# ekta list thakbe. list er proti ta element ho

# find pairwise maximum
# input: list
# output: integer
# method:
#   maximumNumber = 1
#   list er 0 theke sob position er jonno:
#       list er position+1 theke sob index porjonto:
#       jodi (list[position] * list[index]) > maximumNumber hoy:
#           maximumNumber = list[index] * list[index+1]
#   return maximumNumber
def getMaximumPairWiseMultiplication(numbers):
    maximumNumber = 1
    for position in range(len(numbers)):
        for index in range(position+1, len(numbers)):
            if (numbers[position] * numbers[index]) > maximumNumber:
                maximumNumber = numbers[position] * numbers[index]
    return maximumNumber

# print(getMaximumPairWiseMultiplication([-98,10,-2,5,9,52,-8]))


# sortList
# input: duita sorted list, higherLengthedArray, indexofHigherLengthedArray
# return: sortedArray
# method:
#   firstIndex, secondIndex
#   loop chalabo jotokkhon porjonto indexofHigherLengthedArray<len(higherLengthedArray):
#       jodi firstList[firstIndex] < secondList[secondIndex] hoy:
#           sortedArray te append firstList[firstIndex]
#           firstIndex++
#       else:
#           sortedArray te append secondList[secondIndex]
#           secondIndex++
#   return sortedArray

# duita sorted list dibo, oder ke ascending order e banaite hobe
# getSortedList
# input: two sorted list
# return: one sorted lsit
# method:
#   jodi firstList empty hoy:
#       return secondList
#   jodi secondlIst empty hoy:
#       return firstList
#   sortedArray
#   firstIndex, secondIndex
#   jodi firstList len >= secondList len hoy:
#       return sortList(list1, list2, list1, firstIndex)
#   else:
#       return sortList(list1, list2, list2, secondIndex)
