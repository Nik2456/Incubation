
class Dog:

    def speak(self):
        print("Dog")

class Cat:

    def speak(self):
        print("Cat")



def make_sound(animal):
    animal.speak()
make_sound(Dog())
make_sound(Cat())
