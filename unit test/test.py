# import unittest
def sum(a,b):
    return a+b

def test_sum():
    assert sum(1,2) == 3

def test_sum_again():
    assert sum(1,2) == 4

print(test_sum())
print(test_sum_again())