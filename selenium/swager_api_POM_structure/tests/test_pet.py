import pytest

from selenium.swager_api_POM_structure.api.pet_api import PetAPI


@pytest.fixture
def pet_api():
    return PetAPI()

@pytest.fixture
def pet_payload():
    return {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

def test_create_pet(pet_api, pet_payload):
    response = pet_api.create_pet(pet_payload)
    data = response.json()

    print(data)
    print(response.status_code)
    print(response.headers)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    # ⚠️ Important: API may not return fixed ID
    assert "id" in data, "id missing in response"
    assert data["name"] == "doggie"
    assert data["photoUrls"] == ["string"]
    assert data["status"] == "available"