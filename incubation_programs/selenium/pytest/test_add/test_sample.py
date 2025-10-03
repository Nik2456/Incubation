
def add(a,b):
    return a+b

def test_add_positive():
    assert add(2,3)==5

def test_add_negative():
    assert add(-1,-2)==-3

def test_mixed():
    assert add(-1,1)==0