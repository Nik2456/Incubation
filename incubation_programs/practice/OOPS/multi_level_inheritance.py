class GrandFather:
    def __init__(self, name):
        self.name = name

    def m1(self):
        print(self.name)

class Father(GrandFather):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def m2(self):
        print(self.name, self.age)

class Child(Father):
    def __init__(self, name, age, skill):
        super().__init__(name,age)
        self.skill = skill

    def m3(self):
        print(self.name, self.age, self.skill)
c1=Child("Raj",68,"Shop")
c1.m1()
c1.m2()
c1.m3()