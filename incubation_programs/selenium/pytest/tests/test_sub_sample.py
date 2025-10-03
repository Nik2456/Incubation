from incubation_programs.selenium.src.calculator import subtract


def test_subtract_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5

def test_subtract_direct():
    assert subtract(10, 3) == 7

