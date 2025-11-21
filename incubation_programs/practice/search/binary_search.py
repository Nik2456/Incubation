a=[5, 8, 12, 15, 20, 23, 30, 45, 60]

def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"{target} is not found"
print(binary_search(a,20))