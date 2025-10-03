import pytest


@pytest.fixture
def user():
    return {'id':1,'name':'Alice'}

@pytest.fixture
def product():
    return {'id':101,'name':'laptop'}

def test_order(user, product):
    assert user['name']=='Alice'
    assert product['name']=='laptop'