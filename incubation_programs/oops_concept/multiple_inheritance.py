class Name:

    def __init__(self,name):
        self.name = name

class Age:

    def __init__(self,age):
        self.age = age

class Details(Name,Age):

    def __init__(self,name,age,height):
        super().__init__(name)
        Age.__init__(self,age)
        self.height = height

    def display(self):
        print("Name=",self.name,"Age=",self.age,"height=",self.height)

d1=Details(name="A",age=10,height=20)
d1.display()


