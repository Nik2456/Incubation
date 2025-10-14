import requests

body={
  "id": 22,
  "category": {
    "id": 1,
    "name": "Vishal"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 2,
      "name": "Mayur"
    }
  ],
  "status": "available"
}
headers= {'Content-type': 'application/json'}

response = requests.post("https://jsonplaceholder.typicode.com/posts",headers=headers, json=body)
data = response.json()
assert response.status_code == 201
assert data["id"] == 101, "ID does not match"
assert data["name"] == "doggie", "Name mismatch"
assert data["status"] == "available", "Status mismatch"
assert data["category"]["id"] == 1, "Category ID mismatch"
assert data["category"]["name"] == "Vishal", "Category name mismatch"
assert isinstance(data["tags"], list), "tags should be a list"
assert data["tags"][0]["id"] == 2, "Tag ID mismatch"
assert data["tags"][0]["name"] == "Mayur", "Tag name mismatch"
