
def prime_nobs(a,b):
    for num in range(a,b+1):
        if num>1:
            for i in range(2,b):
                if num % i ==0:
                    break
                else:
                    print(num)
prime_nobs(0,19)