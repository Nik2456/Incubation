
def order_pizza(size,*toppings,**details):

    print(f"The size of the pizza is {size}")
    for topping in toppings:
        print(f"-{topping}")
    print(f"-{details}")

order_pizza("large","pepperoni","chicken","onion",delivery=True,tip=5)