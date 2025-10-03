from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        return "Car engine started"
    def stop(self):
        return "Car engine stopped"

class Motorcycle(Vehicle):

    def start(self):
        return "Motorcycle engine started"
    def stop(self):
        return "Motorcycle engine stopped"
m1=Motorcycle()
print(m1.start())
print(m1.stop())
c1=Car()
print(c1.start())
print(c1.stop())
