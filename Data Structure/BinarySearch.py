# binary search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# sorted array thaka lagbe must
# array er majhkhan er index er element er sathe match korbo
# jodi match kore, index return
# noile:
#   jodichoto hoy:
#       0 theke oi index er ager index porjonto array kete nibo and oi array te same operation chalabo
#   jodi boro hoy:
#       mid index theke dkom shesh index porjonto array kete nibo and oi array te sam eoperation chalabo
# jotokkhon na array er length 1 hocche eigula korte thakbo
# length 1 hoile match korbo. mille index return, noile -1 return

# corner cases:
#   1. jodi kono element na thake?
#       return -1
#   2. jodi 1 ta element thake?
#       oi element er sathe match. mille return 0, noile return -1
#   3. jodi 2 ta element thake?
#       [1,2] -> length = 2. mid index = 1.
#       0 theke 1, 1 theke end.
#       numbers = [1,2]
#       numbers[0:1] = [1] -> match kore? korle return 0, na korle -1
#       numbers[1:] = [2] -> match korle return 1, na korle -1
#   4. jodi 3 ta element thake?
#       numbers = [1,2,3]
#       length = 3, mid index = 3 / 2 (int division) = 1
#       numbers[0:1] = [1]
#       numbers[1:] = [2,3]
#       recursive call of the same array

nums = [-1,0,3,5,9,12]
target = 2

def findElement(nums, target):
    if(len(nums) == 0):
        return -1
    if (len(nums) == 1):
        if target ==  nums[0]:
            return 0
        else:
            return -1
    midIndex = int(len(nums) / 2)
    if target == nums[midIndex]:
        return midIndex
    elif target < nums[midIndex]:
        return findElement(nums[0:midIndex], target)
    else:
        rightArrayIndex = findElement(nums[midIndex:], target)
        if rightArrayIndex == -1:
            return -1
        else:
            return midIndex + rightArrayIndex

# print(findElement(nums, target))

# print(findElement([-1,0,3], 2))
# 1. mid index = 1
# 2. if target == nums[midIndex]:
# 3. if 2 == nums[midIndex]:
# 4. if 2 == nums[1]:
# 5. if 2 == 0:
# 6. elif target < nums[midIndex]:
# 7. elif 2 < nums[1]:
# 8. elif 2 < 0:
# 9. else:


# 278. First Bad Version
# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# 10 , bad at 6
# currentMinimumBadVersion = n = 10
# currentMaxGoodVersion = 1
# avg = 5
# 10-5!=0 so:
#   isBad(5) -> true or false
#   here, isBad(5) = false
#   currentMaxGoodVersion = 5

# currentMaxGoodVersion+1, currentMinimumBadVersion -> 6,10:
#   avg = 8
#   8-10 != 0 so:
#       isBad(8) = true
#       currentMinimumBadVersion = 8
#   currentMaxGoodVersion+1, currentMinimumBadVersion -> 6,8:
#   avg = 7
#   7-10 != 0 so:
#       isBad(7) = true
#       currentMinimumBadVersion = 7
#   currentMaxGoodVersion+1, currentMinimumBadVersion -> 6,7


# n and 1 er average bair korbo
# jodi average n er soman hoy:
#   jodi avg bad hoy:
#       return avg
#   noile:
#       return -1
# jodi avg good hoy:
#   avg hobe current maximum good version
#   recursive call with current maximum good version +1
# jodi avg bad hoy:
#   current minimum bad version hocche avg