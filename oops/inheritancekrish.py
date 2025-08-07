# inheritance is a fundamental concept in OOP that a class to inherit attributes and methods from another class.

# Parent class
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    def drive(self):
        print("The person will drive the {self.enginetype} car")

car1 = Car(4,5,"petrol")
car1.drive()
            
# child class
class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        # super means calling the parernt class and its init method
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving = is_selfdriving
        
    def selfdriving(self):
        print(f"Tesla supports {self.is_selfdriving}")
            
     
            