class One:

    def parent(self):
        print("Parent")
        
class Two(One):

    def son(self):
        print("Son")

c1=Two()
c1.parent()
c1.son()