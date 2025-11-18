a=[5, 8, 12, 15, 20, 23, 30, 45, 60]
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Low={low}, High={high}, Mid={mid}, MidValue={arr[mid]}")

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

binary_search(a, 12)