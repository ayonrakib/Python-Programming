import enum, socket, array, sys, sysconfig, pickle

from datetime import date
# # class Student():
# #     counter = 0
# #     collegeName = "NDC"
# #     def __init__(self, name, id):
# #         self.name = name
# #         self.id = id
# #         Student.counter += 1

    
# #     @classmethod
# #     def objectCount(cls):
# #         return cls.counter


# # student1 = Student("ayon", 1)
# # student2 = Student("rakib", 2)
# # print("student1 object college name: ", student1.collegeName)
# # print("Student class college name: ", Student.collegeName)
# # print("Class counter variable: ",Student.objectCount())
# # print("Second student object counter variable: ",student2.counter)
# # why not self.college = "NDC" for all objects? difference between class prop and obj prop?

# # values = ["a", "b", "c"]
# # for count, value in enumerate(values):
# #     print(count, value)

# # nameToAge = {"name":"Ayon","age":29}
# # for name,age in enumerate(nameToAge):
# #     print(name, age)

# class Animal(enum.Enum): 
#     dog = 1
#     cat = 2
#     lion = 3

# # printing enum member as string 
# print ("The string representation of enum member is : ",end="") 
# print (Animal.dog) 
  
# # printing enum member as repr 
# print ("The repr representation of enum member is : ",end="") 
# print (repr(Animal.lion)) 
  
# # printing the type of enum member using type() 
# print ("The type of enum member is : ",end ="") 
# print (type(Animal.lion)) 
  
# # printing name of enum member using "name" keyword 
# print ("The name of enum member is : ",end ="") 
# print (Animal.dog.name) 

# # printing value of enum member using "value" keyword 
# print ("The name of enum member is : ",end ="") 
# print (Animal.dog.value) 

# isAyonSmart = True

# def seeIfAyonIsSmart():
#     print(isAyonSmart)

# seeIfAyonIsSmart()

# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
    
# emails = []
# count = 0
# fh = open(fname)
# for line in fh:
#     words = line.rsplit()
#     if words != []:
#         print(words[0])

# print("There were",count, "lines in the file with From as the first word")


# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
# they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to 
# find the most prolific committer.

# findUserWhoSentMostMail
# input: none
# return: email, count of email
# method:
#   1. namesToEmailCount empty dic
#   2. file name input dibo
#   3. file handler banabo file open kore
#   4. file handler er sob line er jonno:
#       1. unnecessary space remove korbo
#       2. words list banabo line theke
#       3. jodi words empty list na hoy:
#           1. jodi words er 0th element "From" hoy: 
#               1. jodi words[1] namesToEmailCount e exist na kore:
#                   1. namesToEmailCount[words[1]] = 1
#               2. noile:
#                   1. namesToEmailCount[words[1]] += 1
#   5. name empty string, count 0
#   6. namesToEmailCount er sob key value er jonno:
#       1. jodi value > count hoy:
#           1. name = key
#           2. count = value
# #   7. print(name, count)
# namesToEmailCount = {}
# fileHandler = open(input("Please enter your file name: "))
# for line in fileHandler:
#     line.rstrip()
#     words = line.split()
#     if words != []:
#         if words[0] == "From":
#             if words[1] not in namesToEmailCount:
#                 namesToEmailCount[words[1]] = 1
#             else:
#                 namesToEmailCount[words[1]] += 1
# name = ""
# count = 0
# for key, value in namesToEmailCount.items():
#     if value > count:
#         name = key
#         count = value
# print(name, count)

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out from the 'From ' line by 
# finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# findCountOfHour
# input: nothing
# return: nothing, just print the hour and count of hour
# method:
#   1. file name read korbo
#   2. hourToCount empty dict
#   3. result empty list
#   4. file handler khulbo
#   5. file handler er sob line er jonno:
#       1. line er sob space uthabo
#       2. line er propti ta word niye ekta list banabo
#       3. jodi oigula empty list na hoy:
#           1. : er index nibo
#           2. index-2 theke index porjopnto slice korbo hour variable e
#           3. results iterate korbo sob element er jonno:
#               1. jodi hour element[0] er soman na hoy:
#                   1. results e append (hour,1)
#               2. noile:
#                   1. element[1] += 1
#   6. print result
# hourToCount = {}
# result = []
# name = input("Please insert file name: ")
# fileHandler = open(name)
# for line in fileHandler:
#     line.rstrip()
    
#     if line[0:4] == "From" and line[4] != ":":
#         # print(line[0:4])
#         try:
#             index = line.index(":")
#         except ValueError:
#             continue
#         # print(index)
#         hour = line[index-2:index]
#         if int(hour) < 10:
#             hour = int("{:02}".format(int(hour)))
#         else:
#             hour = int(hour)
#         print(hour)
#         if hour not in hourToCount:
#             hourToCount[hour] = 1
#         else:
#             hourToCount[hour] += 1


# hourToCount = {k: v for k, v in sorted(hourToCount.items(), key=lambda item: item[0])}
# for key, value in hourToCount.items():
#     print(key, value)

# print(type("{:05}".format(123)))

# newSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# newSocket.connect(('data.py4e.com',80))

# command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0/n/n'.encode()
# newSocket.send(command)
# while(True):
#     data = newSocket.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# newSocket.close()

# myArray = array.array('b',[1,2,3])
# print(myArray)

class Human():
    def __init__(self, name) -> None:
        self.name = name
        self.hands = 2


    def __str__(self) -> str:
        return f"My name is {self.name}"


    def walk(self):
        return "I am walking!"


# ayon = Human("ayon")
# print(ayon)
# ayon.walk()

a = range(1,10)
  
# initializing a with xrange()
# x = xrange(1,10000)
  
# testing the type of a
# print ("The return type of range() is : ")
# print (type(a))
# print(a[1])
  
# testing the type of x
# print ("The return type of xrange() is : ")
# print (type(x))

def pickle_data():
    data = {
                'name': 'Prashant',
                'profession': 'Software Engineer',
                'country': 'India'
        }
    filename = 'D:/PythonProgramming/Practice/backup/PersonalInfo.txt'
    outfile = open(filename, 'wb')
    pickle.dump(data,outfile)
    outfile.close()
pickle_data()


def unpickling_data():
    filename = 'D:/PythonProgramming/Practice/backup/PersonalInfo.txt'
    file = open(filename,'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data


# print(unpickling_data())

names = ["ayon", "eva", "golam"]
nextName = iter(names)
# print( nextName)
# for name in range(len(names)):
#     print(next(nextName) )

    # A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 2
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
myGenerator = my_gen()
# print(next(myGenerator))
# print(next(myGenerator))
# print(next(myGenerator))
# print(next(myGenerator))

# a=array.array('d', [1.1 , 2.1 ,3.1] )
# a.append(3.4)
# print(a)
# a.extend([4.5,6.3,6.8])
# print(a)
# a.insert(2,3.8)
# print(a)

   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
       
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
   
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
   
print (person1.age)
print (person2.age)
   
# print the result
print (Person.isAdult(22))
print(person1.fromBirthYear('mayank',30))