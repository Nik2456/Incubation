num=[3,5,1,6,9,2,8,4]

def linear_search(arr,target):

    for i, value in enumerate(arr):
        if value==target:
            return i

    return f"{target} not found"
print(linear_search(num,7))
