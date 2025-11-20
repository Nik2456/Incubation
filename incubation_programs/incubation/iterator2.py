
a="I am an Indian"

it=iter(a)
print(next(it))
print(next(it))
print(next(it))
print("**************************")
for i in a:
    try:
        print(next(it))
    except StopIteration:
        break