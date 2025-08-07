# OOPS is a programming paradigm that uses "objects" to design applications and computer programs.OOP allows for modelling real world scenarios using classes and objects.

# Basic OOP Syntax
# class Car:
#     pass

# audi = Car()
# print(type(audi))
# print(audi)


# Instance Variables and Creating objects
# class dog:
#     # constructor, #name and age are instance variables
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# # create objects
# dog1 = dog("buddy",3)
# print(dog1)
# print(dog1.name)
# print(dog1.age) 


# Define a class with instance methods
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #  creating instance method
    def bark(self):
        print(f"{self.name} says wooof")
        
        
dog1 = Dog("rocky",3)
dog1.bark()  
dog2 = Dog("Lucy",4)
dog2.bark()
      
        
            
 
