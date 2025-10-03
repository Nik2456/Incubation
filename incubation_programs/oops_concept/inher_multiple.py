
class GrandFather:

    def skill(self):
        print("GrandFather: Tailor")

class Father:

    def skill(self):
        print("Father: Shopkeeper")

class Child(Father, GrandFather):

    def skill(self):
        print("Child: Software Tester")
c1=Child()
c1.skill()

f1=Father()
f1.skill()

g1=GrandFather()
g1.skill()