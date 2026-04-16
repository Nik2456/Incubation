import requests
headers = {"Content-Type": "application/json"}
body= {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
base_url='https://petstore.swagger.io/v2'
response = requests.post(f"{base_url}/pet", json=body, headers=headers)
data = response.json()
print(data)
print(response.status_code)
print(response.headers)
print(response.json())
assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json'
assert "id" in data, "id missing in response"
assert data['id']== 9223372036854775807, "id is also wrong"
assert data['name'] == 'doggie', "name wrong"
assert data['photoUrls'] == ['string'], "photoUrls are wrong"
assert data['status'] == 'available', "status wrong"
