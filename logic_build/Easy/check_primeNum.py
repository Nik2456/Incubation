
def num(n):
    for i in range(2,n):
        if n % i ==0:
            return "Not a prime number"
        else:
            return "prime number"
print(num(12))