import enum
# class Student():
#     counter = 0
#     collegeName = "NDC"
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         Student.counter += 1

    
#     @classmethod
#     def objectCount(cls):
#         return cls.counter


# student1 = Student("ayon", 1)
# student2 = Student("rakib", 2)
# print("student1 object college name: ", student1.collegeName)
# print("Student class college name: ", Student.collegeName)
# print("Class counter variable: ",Student.objectCount())
# print("Second student object counter variable: ",student2.counter)
# why not self.college = "NDC" for all objects? difference between class prop and obj prop?

# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)

# nameToAge = {"name":"Ayon","age":29}
# for name,age in enumerate(nameToAge):
#     print(name, age)

class Animal(enum.Enum): 
    dog = 1
    cat = 2
    lion = 3

# printing enum member as string 
print ("The string representation of enum member is : ",end="") 
print (Animal.dog) 
  
# printing enum member as repr 
print ("The repr representation of enum member is : ",end="") 
print (repr(Animal.lion)) 
  
# printing the type of enum member using type() 
print ("The type of enum member is : ",end ="") 
print (type(Animal.lion)) 
  
# printing name of enum member using "name" keyword 
print ("The name of enum member is : ",end ="") 
print (Animal.dog.name) 

# printing value of enum member using "value" keyword 
print ("The name of enum member is : ",end ="") 
print (Animal.dog.value) 
