from incubation_programs.selenium.src.calculator import add


def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_add_direct():
    assert add(2, 3) == 5

