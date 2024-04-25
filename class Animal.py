class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(" ")

    def what_kind(self):
        print("I am",self.kind)

class Dog(Animal):
    def make_sound(self):
        kind = savec
        print("Haf:", self.name)

class Kitty(Animal):
    kind = savec
    def make_sound(self):
        print("Mňau:", self.name)

class Snake(Animal):
    kind = plaz
    def make_sound(self):
        print("Sssss:", self.name)

class Carp(Animal):
    kind = ryba
    def make_sound(self):
        print("......:", self.name)

zoo = [Dog("Azor"), Kitty("Micina"), Snake("Python"), Carp("Bubla")
for z in zoo:
    z.make_sound()
    z.what_kind()
