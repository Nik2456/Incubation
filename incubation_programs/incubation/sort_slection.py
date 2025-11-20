

def selection_sort(arr):

    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

numbers = [64, 25, 12, 22, 11]
print("Unsorted:", numbers)
sorted_list = selection_sort(numbers)
print("Sorted:", sorted_list)
