example_string = "baabrakadabra"

freq={}
order=[]

for i in example_string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        order.append(i)
print("Freq=",freq)
print("Order=",order)

result=""
for i in order:
    result+= i *freq[i]

print("Result=",result)