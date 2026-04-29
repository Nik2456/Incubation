def rev_digit_string(n):
    s = str(n)
    s = list(s)
    s.reverse()
    s="".join(s)
    n = int(s)
    return n
print(rev_digit_string(4567))

def rev_slicing(n):
    s = str(n)
    s = s[::-1]
    n = int(s)
    return n
print(rev_slicing(12345))