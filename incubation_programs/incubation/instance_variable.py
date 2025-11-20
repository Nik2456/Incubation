class Car:
    def __init__(self, brand, color):
        self.brand = brand      
        self.color = color

c1 = Car("Toyota", "Red")
c2 = Car("Honda", "Blue")

print(c1.brand, c1.color)
print(c2.brand, c2.color)
