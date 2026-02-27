def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def test_add():
    print("Add code run")
    assert add(2, 3) == 5

def test_sub():
    print("Sub code run")
    assert sub(5, 3) == 2
