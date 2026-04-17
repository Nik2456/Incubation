import requests

base_url = "https://fakerestapi.azurewebsites.net"
headers = {"Accept":"text/plain"}

response = requests.get(f"{base_url}/api/v1/Activities", headers = headers)
data = response.json()
print(data)
assert response.status_code==200
assert response.headers["content-type"] == "application/json"

for ids in data:

    if id in ids:
        assert True

