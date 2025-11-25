class Class:

    a = "Class variable"

    def method(self):
        print("Inside method", Class.a)

c1 = Class()
c1.method()
print(c1.a)

