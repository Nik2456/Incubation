def infinite_generator(start=1):

    while True:
        yield start
        start += 1
gen = infinite_generator()

for num in gen:
    if num>10:
        break
    print(num)