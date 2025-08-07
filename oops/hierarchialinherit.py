###one parent - many childs


class Parent:
    def speak(self):
        print("Parent: Speaks wisely")

class Child1(Parent):
    def dance(self):
        print("Child1: Likes dancing")

class Child2(Parent):
    def sing(self):
        print("Child2: Likes singing")

c1 = Child1()
c1.speak()
c1.dance()

c2 = Child2()
c2.speak()
c2.sing()
