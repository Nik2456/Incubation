
a=  "I was following Indian cricket from long time"
b=a.split()

it=iter(b)

print(next(it))
print(next(it))
print(next(it))

for i in b:
    print(i)