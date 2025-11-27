def getMaximumOnes(s, k):
    s = list(s)
    n = len(s)
    for i in range(n - 2, -1, -1):
        if k == 0:
            break
        if s[i] == '0' and s[i+1] == '1':
            s[i] = '1'
            k -= 1
    return s.count('1')
print(getMaximumOnes("01010", 2))