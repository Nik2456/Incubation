import requests
from jsonschema import validate

def test_user_schema():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    expected_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }

    validate(instance=data, schema=expected_schema)
