class One:

    def __init__(self,name):
        self.name = name

    def parent(self):
        print(f"{self.name} from One class")

class Two(One):

    def __init__(self,name):
        self.name = name

    def son(self):
        print(f"{self.name} from Two class")

c1=Two("Parent")
c2=Two("Son")
c1.parent()
c2.son()