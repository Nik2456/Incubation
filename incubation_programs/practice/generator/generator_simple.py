
def count(n):

    count = 0
    while count<=n:
        yield count
        count += 1

gen = count(10)

for num in count(10):
    print(num)
