from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def company(self):
        pass

class Suzuki(Car):

    def company(self):
        print("Suzuki")

class Hyundai(Car):
    def company(self):
        print("Hyundai")

c1=Hyundai()
c2=Suzuki()
c1.company()
c2.company()