a=[9,2,7,3,5,4,10,14,18,84,54,48,39]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)