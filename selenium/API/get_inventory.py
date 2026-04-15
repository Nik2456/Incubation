import requests

base_url = "https://petstore.swagger.io/v2"

headers = {"content-type": "application/json"}

response = requests.get(f"{base_url}/store/inventory", headers = headers)
data = response.json()
print(data)
assert data["sold"] == 155
assert data["string"] == 120
assert response.headers["content-type"] == "application/json"