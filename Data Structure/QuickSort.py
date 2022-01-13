# quick sort
# divide and conquer:
# divide:
#   divide the array into two subarrays and partition them
# conquer:
#   use the same partition method for the two different subarrays
# A[p,q,r] -> Here, p = lowest index, q = pivot index, r = highest index
# A[q] = pivot, so we will take two subarrays 
# A[p, q-1] and A[q+1, r]
# 

# A = [3,2,1,4]
# pivot = 2
# A[p...r] -> p = 0, r = 3 -> p,q,r are all indices.
# here, q = 1 cause A[1] = 2
# A[0,0] and A[2,3] -> two subarrays need to be partitioned
# partition(A,p,r)