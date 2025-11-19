a=[64, 34, 25, 12, 22, 11, 90, 48, 95]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
