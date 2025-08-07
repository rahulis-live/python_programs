class Student:
    def __init__(self,name,age):
        self.name = name  #public variable 
        self.__age = age  #private
    
    def display(self):
        print(f"My Name is {self.name} and age is {self.__age}")      
        
obj = Student("Rahul",23)
print(obj.name)
# print(obj.age)
obj.display()          