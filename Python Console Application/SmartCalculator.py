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
def sumNumbers(string):
    print(string)
    # integer = 0
    # for character in string:
    #     if ord(character) == 32:
    #         continue
    #     if ord(character) == 43:
    #         continue
    #     if ord(character) == 48:
    #         integer += 0
    #     elif ord(character) == 49:
    #         integer += 1
    #     elif ord(character) == 50:
    #         integer += 2
    #     elif ord(character) == 51:
    #         integer += 3
    #     elif ord(character) == 52:
    #         integer += 4
    #     elif ord(character) == 53:
    #         integer += 5
    #     elif ord(character) == 54:
    #         integer += 6
    #     elif ord(character) == 55:
    #         integer += 7
    #     elif ord(character) == 56:
    #         integer += 8
    #     elif ord(character) == 57:
    #         integer += 9
    # return integer

# targetStringPrint = 'string value of '
# for integer in range(10):
#     string = str(integer)
#     targetStringPrint += string
#     print(targetStringPrint,ord(string))
#     targetStringPrint = 'string value of '
# print(ord('+'))


# + baad e baki sob ekotre print korbo.
# stringToPrint = ''
# string er sob gula character against e iterate:
#    if string[character] != '+':
#       stringToPrint += string[character]
#    else:
#       print(stringToPrint)
#       stringToPrint = ''
print('Please insert the mathematical operation: ')
while(True):
    result = 0
    string = input()
    if string == 'q':
        break
    stringToPrint = ''
    for character in range(len(string)):
        if string[character] == '+':
            if stringToPrint != '':
                result += int(stringToPrint)
            stringToPrint = ''
            pass
        else:
            stringToPrint += string[character]
    if stringToPrint != '':
        result += int(stringToPrint)
        print(result)
