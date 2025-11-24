class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get(self):
        print("Name=",self.__name,"Age=",self.__age)

    def set(self,name,age):
        self.__name = name
        self.__age = age
p1= Person("John",18)
p1.get()
p1.set("Mike",20)
p1.get()