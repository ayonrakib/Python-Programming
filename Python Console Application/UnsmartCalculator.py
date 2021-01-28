import math
class Calculator():
    def __init__(self):
        pass
    def __str__(self):
        return "Hello! This is a smart calculator. It performs some mathematical operations."
# method: operations of the calculator
# input: self
# output: none. output dorkar nai, shudhu onno method call korbe.
# jodi input intger na hoy, exception
# option 1 hoile add
# option 2 hoile subtract
# 3 hoile division
# 4 hoile multiplication
# 5 hoile exponent
# 6 hoile logarithm
# 7 hoile remainder
    def operationsOfTheCalculator(self):
        stringToShowOnScreen= """Hello! This is a smart calculator. These are the operations that can be performed: 
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exponent
    6. Remainder
    7. Logarithm"""
        print(stringToShowOnScreen)
        while(True):
            print("Please select an option. If you want to quit, please press q or Q.")
            selectOperation = input()
            if selectOperation == 'q' or selectOperation == 'Q':
                print("You have exited the calculator. Thank you!")
                break
            if ord(selectOperation) > 48 and ord(selectOperation) < 55:
                number1 = int(input('Please select the first number: '))
                number2 = int(input('Please select the second number: '))
                if ord(selectOperation) == 49:
                    print('The summission of the 2 numbers is: ', self.sumTwoNumbers(number1,number2))
                elif ord(selectOperation) == 50:
                    print('The subtraction of the 2 numbers is: ', self.subtractTwoNumbers(number1,number2))
                elif ord(selectOperation) == 51:
                    print('The multiplication of the 2 numbers is: ', self.multiplyTwoNumbers(number1,number2))
                elif ord(selectOperation) == 52:
                    print('The division of the 2 numbers is: ', self.divideTwoNumbers(number1,number2))
                elif ord(selectOperation) == 53:
                    print('The exponent of the 2 numbers is: ', self.exponentOfTwoNumbers(number1,number2))
                elif ord(selectOperation) == 54:
                    print('The remainder is: ', self.remainder(number1,number2))
            elif ord(selectOperation) == 55:
                number1 = int(input('Please select the base number: '))
                print('The logarithm of the base number is: ', self.logarithm(number1))
            else:
                print("The input number was not valid. Please insert a valid number.")
    # method: sum 2 numbers
    # input: number1, number 2
    # return: sum of 2 numbers
    # method: return number1+number2
    def sumTwoNumbers(self,number1, number2):
        return number1 + number2

    # method: subtract 2 numbers
    # input: number1, number 2
    # return: subtract 2 numbers
    # method: return number1-number2
    def subtractTwoNumbers(self,number1, number2):
        return number1 - number2

    # method: multiply 2 numbers
    # input: number1, number 2
    # return: multiply 2 numbers
    # method: return number1*number2
    def multiplyTwoNumbers(self,number1, number2):
        return number1 * number2

    # method: divide 2 numbers
    # input: number1, number 2
    # return: divide 2 numbers
    # method: if number2==0, raise Exception("dividend cannot be 0!")
    #         else, return number1/number2
    def divideTwoNumbers(self,number1, number2):
        if number2 == 0:
            raise Exception("Divisor cannot be zero!")
        return number1 / number2

    # method: exponent
    # input: number1, number2. number1 is base and number2 is power.
    # return: exponent answer in integer
    # method: if number1==0, return 0
    #         if number2==0, return 1
    #         result = 1
    #         for count in range(number2):
    #            result *= number1
    #         return result
    def exponentOfTwoNumbers(self, number1, number2):
        if number1==0: 
            return 0
        if number2==0: 
            return 1
        result = 1
        for count in range(number2):
            result *= number1
        return result

# method: logarithm
# input: only one integer number1
# return: log of that integer
# method: 
#    log of <=0 is undefined, so if input == 0, throw exception
#    return math.log(number 1)

    def logarithm(self,number1):
        if number1 == 0:
            raise Exception("Log of 0 is undefined!")
        if number1 < 0:
            raise Exception("Log of -ve number is undefined.")
        return math.log(number1)

# method: remainder
# input: number1, number2
# return: if number2==0:
#            raise exception("divisor cannot be 0")
#         return number1 % number2
    def remainder(self, number1, number2):
        if number2 == 0:
            raise Exception("Divisor cannot be zero.")
        return number1 % number2
calculator = Calculator()
print(calculator)
calculator.operationsOfTheCalculator()