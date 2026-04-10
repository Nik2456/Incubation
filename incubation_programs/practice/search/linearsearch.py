def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return "Element is not present in the array."

print(linear_search([2,5,3,7,9,6,3],1))