class Car:

    def __init__(self,model,year):
        self.model=model
        self.year = year

    def display(self):
        print(f"Model: {self.model}",f"Year: {self.year}")

c1=Car("Mercede",2005)
c1.display()