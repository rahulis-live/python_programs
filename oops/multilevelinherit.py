###multiplevel inheritance

class GrandParent:
    def legacy(self):
        print("Grandparent: Family traditions")

class Parent(GrandParent):
    def guidance(self):
        print("Parent: Gives advice")

class Child(Parent):
    def learn(self):
        print("Child: Learns values")

c = Child()
c.legacy()
c.guidance()
c.learn()
