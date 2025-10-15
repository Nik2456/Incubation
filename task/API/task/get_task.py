import requests

url=" https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
assert response.status_code == 200
data = response.json()
user_found = any(user["name"] == "Ervin Howell" for user in data)
assert user_found, "Username 'Ervin Howell' not found in API response"
