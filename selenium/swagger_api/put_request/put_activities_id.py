import requests

base_url = "https://fakerestapi.azurewebsites.net"
headers = {"Accept":"text/plain", "content-type": "application/json"}
body = {
    "id": 10,
    "title": "ABC",
    "dueDate": "2026-04-17T05:27:56.784Z",
    "completed": True
}
response = requests.put(f"{base_url}/api/v1/Activities/2", headers = headers, json = body)
data = response.json()
print(data)
print(response.status_code)
assert response.status_code==200
assert data['title'] == "ABC"
assert "id" in data
assert data['id'] == 10