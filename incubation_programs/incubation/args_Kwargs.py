
def order_pizza(size,*toppings,**details):

    print(f"The size of the pizza is {size}")
    for topping in toppings:
        print(f"toppings are {topping}")
    print(f"-{details}")

order_pizza("large","pepperoni","chicken","onion",delivery=True,tip=5)

def method(a,*b,**c):
    print(f"The value of a= {a}")
    for b in b:
        print(f"b = {b}")
    print(f"The value of c = {c}")
method(1,2,3,4,5,key=True, Run=2,Avg=3)
