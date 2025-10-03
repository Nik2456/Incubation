from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Bhow Bhow")

class Cat(Animal):

    def speak(self):
        print("Meow Meow")

c1=Cat()
c1.speak()
d1=Dog()
d1.speak()
