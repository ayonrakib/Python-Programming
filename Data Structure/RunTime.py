# getRunTime
# input: m, n
# return: run time of the method as int
# method:
#   1. count 0
#   2. m theke n porjonto loop chalabo:
#       1. count++
#   3. return count
def getRunTime(m,n):
    count = 0
    for number in range(m,n+1):
        count += 1
    return count

print("Run time from 5 to 10 is:",getRunTime(5,10))
# O(bigger number - lower number+1)

print("Run time from 10 to 10 is:",getRunTime(10,10))
# O(1)

print("Run time from 10 to 1 is:",getRunTime(10,1))
# O(0)

# F = n^3 + 100*n^2 + log(n)
# F = n^3 + 100*n^2 + log(n) + m
# c1, c2 > 0
# c1, c2 such that c1* 