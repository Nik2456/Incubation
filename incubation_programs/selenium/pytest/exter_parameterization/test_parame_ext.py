import csv

import pytest


def load_csv_data():
    with open("testdata.csv") as f:
       reader = csv.DictReader(f)
       return [(int(row["a"]),int(row["b"]),int(row["expected"]))for row in reader]


@pytest.mark.parametrize("a,b,expected", load_csv_data())
def test_addition(a, b, expected):
    assert a + b == expected