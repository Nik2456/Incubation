a=[1,2,3,4,5,6,7]

it=iter(a)
print(next(it))
print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        break

