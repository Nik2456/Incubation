import requests

headers = {"content-type": "application/json"}
base_url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

response = requests.get(base_url, headers=headers)

data = response.json()
print(data)
assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json'

for pet in data:
    assert "id" in pet
    assert "name" in pet
    assert pet["status"] == "available"