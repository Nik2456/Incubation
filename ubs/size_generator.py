import sys

list_nums = [x for x in range(1000)]
gen_nums = (x for x in range(1000))

print(sys.getsizeof(list_nums))  # Larger
print(sys.getsizeof(gen_nums))   # Much smaller