a=[1,3,4,0,4,7,5,9,1,4,7,9]

fre={}

for i in a:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(fre)
