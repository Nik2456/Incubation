numbers=[1,2,3,4,5]

add_sqr={n: (n*n if n % 2 != 0 else n) for n in numbers}
print(add_sqr)