import requests

headers = {"content-type": "application/json"}
body = [
  {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]
base_url = 'https://petstore.swagger.io/v2'

response =requests.post(f"{base_url}/user/createWithArray", json = body , headers = headers)
data = response.json()
print(data)
assert response.status_code==200
assert response.headers['content-type']=='application/json'
assert data['message'] == 'ok'
