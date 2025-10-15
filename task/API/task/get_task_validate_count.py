import requests
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

url="https://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url,headers=headers)
data = response.json()
employees = data.get("data", [])
count = len(employees)
assert response.status_code == 200
assert count ==24
assert response.headers["Content-Type"] == "application/json"
assert data["status"]=="success"
