import requests

base_url = "https://gorest.co.in/public/v2/users"
headers = {"Authorization":"Bearer 2bbf50771a8cfb95bf793a3d0dfd8851996b85584c78ccbd3861c8873c8b93c1"}

para = {
    "page": 1,
    "per_page": 1
}
response = requests.get(base_url, params = para, headers = headers)
data = response.json()
print(data)
print(response.status_code)
assert response.status_code == 200