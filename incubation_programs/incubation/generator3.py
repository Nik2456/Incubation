
def gen(n):

    num=1
    while num <= n:
        yield num
        num+=1
for i in gen(5):
    print(i)