class Father:
    def skill(self):
        print("Father: Knows carpentry")

class Mother:
    def talent(self):
        print("Mother: Knows painting")

class Child(Father, Mother):
    def own_skill(self):
        print("Child: Plays guitar")

c = Child()
c.skill()
c.talent()
c.own_skill()
