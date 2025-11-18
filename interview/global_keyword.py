x = 10

def m1():

    global x
    print("inside fun without modified", x)
    x = 20
    print("inside fun with modified",x)

m1()
print("outside fun with modified",x)
