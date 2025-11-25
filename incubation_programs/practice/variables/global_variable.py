
a = "Global variable"

class Class:

    def method(self):
        global a
        a="Global variable updated"
        print(a)

c1=Class()
c1.method()
print("a =",a)