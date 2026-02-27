import copy

original=[1,2,[3,4]]

shallow=copy.copy(original)
print("Original:", original)
print("Shallow:", shallow)
print("After modify***********")
shallow[2][0]=13
print("Original:", original)
print("Shallow:", shallow)
print("***********************")
import copy

a=[0,1,2,3,4,5,6,7,8,9,10]

shallow=copy.copy(a)
print(a)
print(shallow)

print("**********************")
shallow[5]=15
print(a)
print(shallow)


