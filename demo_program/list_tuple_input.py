
values= input("input numbers: ")

List=values.split(",")
print(type(List),List)
print(type(values))

a="a b c d e f g"
b=a.split(" ")
print(type(b),b)
c=" ".join(b)
print(c,type(c))