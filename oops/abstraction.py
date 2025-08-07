from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*(self.r)**2
    
obj = Circle(8)
print(obj.area())    
        
            