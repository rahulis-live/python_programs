class GrandParent:
    def story(self):
        print("Grandparent: Tells stories")

class Father(GrandParent):
    def teach(self):
        print("Father: Teaches maths")

class Mother:
    def cook(self):
        print("Mother: Cooks food")

class Child(Father, Mother):  # Hybrid: multilevel + multiple
    def play(self):
        print("Child: Plays video games")

c = Child()
c.story()
c.teach()
c.cook()
c.play()
