class Cat:

    def speak(self):
        return "Meow"

class Dog:

    def speak(self):
        return "Woof"

def make_sound(animal):
    print(animal.speak())

make_sound(Cat())
make_sound(Dog())