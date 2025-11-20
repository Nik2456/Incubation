
a="Global variable"

class One:

    def method(self):
        print(a)

class Two:

    def method(self):
        print(a)

o1=One()
o2=Two()
o1.method()
o2.method()