import pytest


def test_add():
    assert 2+3==5

@pytest.mark.parametrize("a,b,result",[(3,3,6),(4,3,7),(5,5,10)])
def test_param(a,b,result):
    assert a+b==result