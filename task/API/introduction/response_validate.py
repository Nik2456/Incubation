import requests

payload = {"email":"peter@klaven","password":"pistol"}
request_header = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/user?page=2"

response = requests.post(url, headers=request_header)
data = response.json()
print(data)
print(response.status_code)
assert response.status_code == 201

