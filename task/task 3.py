def prime_range(start, end):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n % i == 0:
                return False
        return True

    for number in range(start, end+1):
        if is_prime(number):
            yield number

for number in prime_range(10,100):
    print(number)