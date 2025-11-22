class Cat:

    def sound(self):
        return "Meow"

class Dog:

    def sound(self):
        return "Bhow"

def make_sound(animal):
    print(animal.sound())

make_sound(Cat())
make_sound(Dog())