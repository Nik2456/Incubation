import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()
assert response.status_code == 200

