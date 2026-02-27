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