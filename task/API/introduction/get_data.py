import requests

url="https://reqres.in/api/users?page=2"
response = requests.get(url)
status_code= response.status_code
assert status_code == 200
data = response.json()
print("DATA-",data)
#assert data['id'] == 7
print("status_code is - ",status_code)
print("headers - ",response.headers)
