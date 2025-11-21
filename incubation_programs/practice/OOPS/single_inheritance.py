class Person:

    def __init__(self,name):
        self.name = name
    def method(self):
        print(self.name)

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def method(self):
        print(self.name,"has age is",self.age)
s1=Student("John",20)
s1.method()
