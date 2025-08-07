class dog:
    def sound (self):
        print("Woof")
class cat:
    def sound (self):
        print("Meow")
def make_a_sound(animal):
    animal.sound()
d=dog()
c=cat()
make_a_sound(c)
make_a_sound(d)