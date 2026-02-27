class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def show(self):
        print("Hello from Child1")

class Child2(Parent):
    def show(self):
        print("Hello from Child2")

c1 = Child1()
c1.greet()
c1.show()

c2 = Child2()
c2.greet()
c2.show()
