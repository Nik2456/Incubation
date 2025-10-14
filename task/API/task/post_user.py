import requests

body={
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userId": 1,
}
headers= {'Content-type': 'application/json; charset=UTF-8'}

response = requests.post("https://jsonplaceholder.typicode.com/posts",headers=headers, json=body)
data = response.json()
assert response.status_code == 201
assert data["id"] == 101
assert data["title"] == "foo"
assert data["body"] == "bar"
assert data["userId"] == 1