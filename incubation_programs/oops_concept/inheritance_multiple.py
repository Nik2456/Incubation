class Father:
    def skill(self):
        print("Father: Driving")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill(self):
        print("Child: Coding")

c = Child()
c.skill()
c1=Mother()
c1.skill()
c2=Father()
c2.skill()
