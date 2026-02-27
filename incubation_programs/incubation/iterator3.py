
a=  "I was following Indian cricket from long time"
b=a.split()

it=iter(b)

print(next(it))
print(next(it))
print(next(it))
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
for i in b:
    try:
        print(next(it))
    except StopIteration:
        break