
class Student:

    school="KBC International"

    def __init__(self,name):
        self.name = name


s1=Student("shaurya")
s2=Student("Nikhil")
print(s1.school,s1.name)
print(s2.school,s2.name)