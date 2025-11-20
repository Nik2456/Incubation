def sq_top_ten(num):

    n=1
    while n<=num:
        sq=n**2
        yield sq
        n+=1
val=sq_top_ten(50)
for i in val:
    print(i)
