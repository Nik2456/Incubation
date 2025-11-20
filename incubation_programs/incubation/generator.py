a=list(range(1,11))
print(a)

b=[]
i=1
while i<11:
    b.append(i)
    i=i+1
print(b)

print("***************************")
def create1():
    i=1
    while i<11:
        yield i
        i=i+1

x=create1()
print(next(x))
print(next(x))
print(next(x))
print(list(x))
