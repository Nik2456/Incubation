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
        print("Car is Started")
    def stop(self):
        print("Car is Stopped")

class Truck(Vehicle):
    def start(self):
        print("Truck is Started")
    def stop(self):
        print("Truck is Stopped")
t1=Truck()
c1=Car()
t1.start()
t1.stop()
c1.start()
c1.stop()
