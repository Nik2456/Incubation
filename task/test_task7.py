import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected",[(2, 3, 5), (-1, 1, 0), (0, 0, 0), (10, 5, 15)])
def test_addition(a, b, expected):
    assert add(a, b) == expected,"Addition of two numbers are not as Expected"
