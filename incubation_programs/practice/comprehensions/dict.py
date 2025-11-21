a=[1,2,3,4,5,6,7,8,9]
b={i:i for i in a}
print("b=",b)

c={n:n*n for n in a}
print("c=",c)

d={m:(m**2 if m%2!=0 else m) for m in a}
print("d=",d)