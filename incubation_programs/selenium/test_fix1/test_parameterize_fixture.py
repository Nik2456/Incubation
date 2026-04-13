import pytest

@pytest.fixture(params=[1,2,3,4,5])
def student(request):
    return request.param

def test_student(student):
    print(student)