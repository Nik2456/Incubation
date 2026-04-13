class One:
    def one(self):
        print("One")

class Two(One):
    def two(self):
        print("Two")

class Three(Two):
    def three(self):
        print("Three")

class Four(Three):
    def four(self):
        print("Four")
c1=Four()
c1.one()
c1.two()
c1.three()
c1.four()