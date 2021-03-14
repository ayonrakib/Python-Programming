def add(number1, number2):
    return number1 + number2

result = map(add,[1,1],[2.0,3.0,5.0])
print("result object after adding lists is:",result)
print("sum in list is:",list(result))

result = map(add,{"number1":1,"number2":2},{"number1":3,"number2":4})
print("result object after adding dicts is:",result)
print("sum in dict is:",list(result))

result = map(add,{"number1":1,"number2":2},{"number1":3,"number2":4})
print("result object after adding dicts is:",result)
print("sum in dict is:",list(result))

result = map(add,(1,1),(2.0,3.0,5.0))
print("result object after adding tuples is:",result)
print("sum in tuple is:",tuple(result))

for sum in list(result):
    print("current sum is:",sum)