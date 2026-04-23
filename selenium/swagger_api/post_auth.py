import requests
import json

base_url = "https://gorest.co.in/public/v2/users"
headers = {"Authorization":"Bearer 2bbf50771a8cfb95bf793a3d0dfd8851996b85584c78ccbd3861c8873c8b93c1"}
json_file=open("C:/Users/NikhilBavane/PycharmProjects/PythonProject/Incubation/selenium/swagger_api/body.json")
json_body = json.load(json_file)
response = requests.post(f"{base_url}", headers = headers, json = json_body)
data = response.json()
print(data)
print(response.status_code)
assert response.status_code == 201

getresponse = requests.get(base_url + '/'+ str(data['id']), headers = headers)
print(getresponse.json())