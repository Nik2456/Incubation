
def car(name,*avg,**details):

    print(f"{name} and avg are {avg} and details are {details}")

    for a in avg:
        print(f"Avg are={a}")

car("i10",20,19,18,price=4,tyre=True)