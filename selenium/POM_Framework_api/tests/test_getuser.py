import pytest

from POM_Framework_api.utils.api import Api


@pytest.fixture(scope= 'module')
def api():
    return Api()

def test_getuser(api):
    response = api.get('users')
    data = response.json()
    print(data)


