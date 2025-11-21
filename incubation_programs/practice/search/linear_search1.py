num=[0,1,2,3,4,5,6,7,8,9]

def linear_search(arr,target):
	for i, value in enumerate(arr):
		if value==target:
			return i
	return f"{target} is not found"
print(linear_search(num,10))