import pytest


@pytest.fixture
def sample_data():
    print("\n--- Setup ---")
    data = {"username": "test_user", "password": "secret"}
    yield data
    print("\n--- Teardown ---")