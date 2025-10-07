import pytest
import random
import time

@pytest.mark.tag("smoke")
def test_addition():
    assert 1 + 1 == 2


@pytest.mark.tag("regression")
def test_multiplication():
    time.sleep(1)
    assert 2 * 3 == 6


@pytest.mark.tag("flaky")
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_flaky():
    assert random.choice([True, False])
