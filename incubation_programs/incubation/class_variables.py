class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


s1 = Student("Nikhil")
s2 = Student("Priya")

print(s1.name, s1.school)
print(s2.name, s2.school)
