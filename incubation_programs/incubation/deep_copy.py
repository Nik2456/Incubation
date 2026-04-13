import copy

original=[1,2,[3,4]]

shallow=copy.deepcopy(original)
print("Original:", original)
print("Shallow:", shallow)
print("After modify***********")
shallow[2][0]=13
print("Original:", original)
print("Shallow:", shallow)
print("***********************")

a=[0,1,2,3,4,5,6,7,8,9,10]

deep1=copy.deepcopy(a)
print(a)
print(deep1)

print("**********************")
deep1[5]=15
print(a)
print(deep1)