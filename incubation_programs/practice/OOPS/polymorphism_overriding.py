
class  Car:

    def show(self):
        return "Car is looking good"

class Motorcycle(Car):

    def show(self):
        return "Motorcycle is looking good"
m1=Motorcycle()
c1=Car()
print(m1.show())
print(c1.show())