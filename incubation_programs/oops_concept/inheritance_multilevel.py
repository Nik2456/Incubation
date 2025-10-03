class One:
    def method(self):
        print("One")
class Two(One):
    def method(self):
        print("Two")
class Three(Two):
    def method(self):
        print("Three")
class Four(Three):
    def method(self):
        print("Four")
o1=Four()
o1.method()
o2=Three()
o2.method()
o2=Two()
o2.method()
o2=One()
o2.method()