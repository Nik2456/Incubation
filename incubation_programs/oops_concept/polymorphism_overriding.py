
class Dog:
    def speak(self):
        print("Woof")

class Cat(Dog):
    def speak(self):
        print("Meow")

c1=Cat()
d1=Dog()
c1.speak()
d1.speak()