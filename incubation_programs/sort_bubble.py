a=[1,5,3,7,2,8,9,4,6]

n=len(a)

for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)