x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Looks in Local → Enclosing → Global → Built-in
    inner()

outer()
