import requests

headers = {"content-type":"application/json"}
base_url = "https://petstore.swagger.io/v2/pet/184792"

response = requests.get(base_url, headers = headers)
data =  response.json()
print(data)
assert response.status_code == 200
assert response.headers['content-type']=='application/json'
assert data['category']['id']==1
assert data['category']['name']=='Dogs'
assert data['photoUrls']== ['https://example.com/photo1.jpg']