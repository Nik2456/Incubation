from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def name(self):
        pass

class Hyundai(Car):

    def name(self):
        return "Creta"

class TATA(Car):

    def name(self):
        return "Nexon"
t1= TATA()
print(t1.name())
h1=Hyundai()
print(h1.name())
