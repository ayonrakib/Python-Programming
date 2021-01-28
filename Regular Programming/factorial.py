# factorial n
# equation: n! = n*(n-1)!
# so, (n-1) bar call korte hobe.

def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("NA")
    else:
        return n*recur_factorial(n-1)


# n = 4
# if n== 1:
# if 4 == 1:
# if false:
# elif n < 1:
# elif 4 < 1:
# elif false:
# else:
#   return n * recur_factorial(n-1)
#   return 4 * recur_factorial(n-1)
#   return 4 * recur_factorial(4-1)
#   return 4 * recur_factorial(3)
#       n = 3
#       if n== 1:
#       if 3 == 1:
#       if false:
#       elif n < 1:
#       elif 3 < 1:
#       elif false:
#       else:
#           return n * recur_factorial(n-1)
#           return 3 * recur_factorial(n-1)
#           return 3 * recur_factorial(3-1)
#           return 3 * recur_factorial(2)
#               n = 2
#               if n== 1:
#               if 2 == 1:
#               if false:
#               elif n < 1:
#               elif 2 < 1:
#               elif false:
#               else:
#                   return n * recur_factorial(n-1)
#                   return 2 * recur_factorial(n-1)
#                   return 2 * recur_factorial(2-1)
#                   return 2 * recur_factorial(1)
#                       n = 1
#                       if n== 1:
#                       if 1 == 1:
#                       if true:
#                           return 1
#                  return 2 * 1
#                  return 2
#           return 3 * 2
#           return 6
#   return 4 * 6
#   return 24 