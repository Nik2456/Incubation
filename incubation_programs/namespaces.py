
a="Global Namespaces"

def outer():
    a="Enclosed Namespaces"

    def inner():
        a = "Local Namespaces"
        print(a)
    inner()

outer()
