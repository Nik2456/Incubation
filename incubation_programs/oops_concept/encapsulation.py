
class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

s1 = Student("Nikhil", 21)
print("Name:", s1.name)
print("Age:", s1.get_age())

s1.set_age(25)                     # Updating age safely
print("Updated Age:", s1.get_age())