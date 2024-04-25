class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(" ")

class Dog(Animal):
    def make_sound(self):
        print("Haf:", self.name)

class Kitty(Animal):
    def make_sound(self):
        print("Mňau:", self.name)

class Snake(Animal):
    def make_sound(self):
        print("Sssss:", self.name)

class Carp(Animal):
    def make_sound(self):
        print("......:", self.name)

zoo = [Dog("Azor"), Kitty("Micina"), Snake("Python"), Carp("Bubla")
for z in zoo:
    z.make_sound()
