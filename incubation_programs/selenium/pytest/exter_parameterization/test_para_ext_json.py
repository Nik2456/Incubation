import json

import pytest


def load_json_data():
    with open("testdata.json") as f:
       return [(item["a"],item["b"],item["expected"])for item in json.load(f)]


@pytest.mark.parametrize("a,b,expected", load_json_data())
def test_addition(a, b, expected):
    assert a + b == expected