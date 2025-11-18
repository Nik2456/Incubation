num=[3,5,1,6,9,2,8,4]

def linear_search(arr,target):
    for i,value in enumerate(arr):
        print(f"Checking index {i}, value {value}")

        if value== target:
            return i

    return f"Value {target} is not in the list "
result=linear_search(num,7)
print(result)