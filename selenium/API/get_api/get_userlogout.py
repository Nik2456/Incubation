import requests

base_url = "https://petstore.swagger.io/v2"

headers = {"content-type": "application/json"}

response = requests.get(f"{base_url}/user/logout", headers = headers)

data = response.json()
print(data)
assert response.status_code == 200
assert response.headers['content-type'] == 'application/json'
assert data['message'] == 'ok'