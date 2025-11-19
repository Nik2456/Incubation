a=[64, 34, 25, 12, 22, 11, 90, 48, 95]
n=len(a)

for i in range(n):
    min_i = i
    for j in range(i+1, n):
        if a[j] < a[min_i]:
            min_i = j
    a[i], a[min_i] = a[min_i], a[i]
print(a)
