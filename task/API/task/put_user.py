import requests

body={
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userId": 1,
}
headers= {'Content-type': 'application/json; charset=UTF-8'}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1",headers=headers, json=body)
data = response.json()
assert response.status_code == 200
print(data)
assert data["id"] == 1
assert data["title"] == "foo"