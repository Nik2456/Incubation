my_dict={"a":[2,3,4], "b": [1,2,3], "c":[4,5,6]}


sum_dict={keys:sum(values) for keys,values in my_dict.items()}

print(sum_dict)