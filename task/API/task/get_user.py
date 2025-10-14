import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
assert response.status_code == 200
assert data[0]["name"] == "Leanne Graham", "Name mismatch in API response"
assert data[0]["email"] == "Sincere@april.biz", "Email mismatch in API response"