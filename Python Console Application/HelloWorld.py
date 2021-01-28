# print('Hello World')
# myName = input()
# print(myName)
# for count in range(10):
#     takeInput = input()
# method: sum 2 numbers
# input: string pura
# return: sum of 2 numbers
# method: 
#   string borabor iteration:
#       jodi space pai, continue.
#       kemne check korbo space? ord(charater) == 32 paile continue
#       jodi ord(character) == 43 hoy:
#           call sumTwoNumbers method with string as parameter.
#   function er vitore:
#       integer1= 0
#       string borabor iteration:
#           jodi space pai, continue.
#           jodi ord(character) == 43 hoy, break
#           jodi ord(character) == 32 hoy, continue
#           jodi ord(character) == 48 hoy, integer1 += 0
#           jodi ord(character) == 49 hoy, integer1 += 1


def sumTwoNumbers(string):
    integer = 0
    for character in string:
        if ord(character) == 32:
            continue
        if ord(character) == 43:
            continue
        if ord(character) == 48:
            integer += 0
        elif ord(character) == 49:
            integer += 1
        elif ord(character) == 50:
            integer += 2
        elif ord(character) == 51:
            integer += 3
        elif ord(character) == 52:
            integer += 4
        elif ord(character) == 53:
            integer += 5
        elif ord(character) == 54:
            integer += 6
        elif ord(character) == 55:
            integer += 7
        elif ord(character) == 56:
            integer += 8
        elif ord(character) == 57:
            integer += 9
    return integer

# number1Input = int(input('Please insert the 1st number: '))
# number2Input = int(input('Please insert the 2nd number: '))
# print('The sum of number1 and number2 is: ',sumTwoNumbers(number1Input, number2Input))
while(True):
    string = input('Please insert the addition string. Press q to exit: ')
    if string == 'q':
        break
    for character in string:
        if character == '+':
            print(sumTwoNumbers(string))
            break
