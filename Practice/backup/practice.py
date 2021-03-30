# import enum
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
#   7. print(name, count)
namesToEmailCount = {}
fileHandler = open(input("Please enter your file name: "))
for line in fileHandler:
    line.rstrip()
    words = line.split()
    if words != []:
        if words[0] == "From":
            if words[1] not in namesToEmailCount:
                namesToEmailCount[words[1]] = 1
            else:
                namesToEmailCount[words[1]] += 1
name = ""
count = 0
for key, value in namesToEmailCount.items():
    if value > count:
        name = key
        count = value
print(name, count)