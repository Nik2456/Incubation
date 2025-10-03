import pytest


@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_multi_two_number(number):
    result=number*2
    assert result in [2,4,6]