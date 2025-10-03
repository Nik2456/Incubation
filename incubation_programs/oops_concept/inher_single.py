
class Parent:

    def __init__(self,name):
        self.name = name
    def method(self):
        print(self.name)

class Child(Parent):

    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def method(self):
        print(self.name,self.age)

c1= Child("Nik",35)

c1.method()
p1= Parent("Nik")
p1.method()

