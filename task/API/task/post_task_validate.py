import requests

payload={"name":"test","salary":"123","age":"23"}
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
url_get = "https://dummy.restapiexample.com/api/v1/employees"
response_before = requests.get(url_get, headers=headers)
data_before = response_before.json()
count_before = len(data_before.get("data", []))
print("Initial Employee Count:", count_before)

url="https://dummy.restapiexample.com/api/v1/create"
response = requests.post(url,headers=headers,json=payload)
data = response.json()
print(response.status_code)

response_after = requests.get(url_get, headers=headers)
data_after = response_after.json()
count_after = len(data_after.get("data", []))
print("Updated Employee Count:", count_after)
