# quick sort
# i,j,p,r always index. er moddhe p and r constant.
# p hocche first index and r hocche last.
# r index er value ta pivot.
# 1. find first number greater than A[r]. set that index to j and i = j-1
# 2. find next value smaller or equal to A[r] from current j. set j with new index.
# 3. switch A[i+1], A[j] and then i++. go back to 2.

# 1. find first number (A[j]) greater than A[r]. set that index to j and i = j-1.
# while checking, j always has to be less than r. that is the corner case.
while(A[j] <= A[r]):
    j +=1
i = j-1

# 2. find next value smaller or equal to A[r] from current j. set j with new index.
# same corner case, if no smaller value
def getSmallerValue():
    while(A[j]>A[r]):
        j+=1

# 3. switch A[i+1], A[j] and then i++. go back to 2.
# i cannot go over last index. plus proti function call er jonno i different hobe.
    temporaryVariable = A[i+1]
    A[i+1] = A[j]
    A[j] = temporaryVariable
    i+=1 
    getSmallerValue()


# quicksort
# input: array
# output: sorted array
# method:
#   1. i,j,p,r define korbo. j = 0 shuru te.
#   2. p hocche shurur index, r hocche shesh index.
#   3. r index er value hocche pivot.
#   4. find first number greater than A[r].
#   5. jotokkhon porjonto arrray[j] <= A[r] and j<=r:
#       6. set that index to j and i = j-1
#       7. j += 1
#   8. i = j-1
#   9. find next value smaller or equal to A[r] from current j. 
#   10. jotokkhon porjonto A[j] > A[r] and j <= r:
#       11. set j with new index.
#       12. j += 1
#   13. switch A[i+1], A[j]
#   14. temporaryVariable define korbo  A[i+1] value diye.
#   15. A[j] er value rakhbo A[i+1] e.
#   16. temporaryVariable er value rakhbo A[j] te.
#   17. call korbo step 5