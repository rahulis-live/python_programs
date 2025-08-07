# class Sample:
#      x = "rahul"
     
#      def demo(self):
#          print(f"{self.x} says hello makkale...")

# obj = Sample()
# obj.demo()         


class Sample:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
    def demo(self):
        print(f"{self.name} age is {self.age}")
        

obj = Sample("rahul","23")
obj.demo()
        