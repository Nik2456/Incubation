import pytest

from Incubation.task.API.utils.api_client import APIClient

BASE_URL = "https://api.example.com"

@pytest.fixture(scope="module")
def client():
    return APIClient(BASE_URL)

test_data = [
    ("basic", {"type": "basic"}),
    ("extended", {"type": "extended"}),
    ("admin", {"type": "admin"}),
]

@pytest.mark.parametrize("test_type, payload", test_data)
def test_dynamic_response_structure(client, test_type, payload):

    response = client.post("/user/details", payload)
    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    data = response.json()
    print(f"\n🔹 Validating response for type: {test_type}")
    print(f"Response: {data}")

    if test_type == "basic":
        expected_keys = {"id", "name"}
    elif test_type == "extended":
        expected_keys = {"id", "name", "address", "email"}
    elif test_type == "admin":
        expected_keys = {"id", "name", "permissions"}
    else:
        pytest.fail(f"Unknown test type: {test_type}")

    missing_keys = expected_keys - data.keys()
    assert not missing_keys, f"Missing keys in response: {missing_keys}"

    for key in expected_keys:
        if key == "id":
            assert isinstance(data[key], int)
        elif key in ["name", "address", "email"]:
            assert isinstance(data[key], str)
        elif key == "permissions":
            assert isinstance(data[key], list)
