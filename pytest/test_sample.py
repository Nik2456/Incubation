def add(a,b):
    return a+b

def test_add():
    assert add(1,2) == 3
    assert add(10,2) == 12
class TestCalculator:
    def test_add(self):
        assert 2 + 2 == 4

    def test_subtract(self):
        assert 5 - 3 == 2