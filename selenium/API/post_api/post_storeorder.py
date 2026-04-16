import requests
headers = {"Content-Type": "application/json"}
body= {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2026-04-16T05:14:24.562Z",
  "status": "placed",
  "complete": True
}
base_url='https://petstore.swagger.io/v2'

response = requests.post(f"{base_url}/store/order", headers = headers , json = body)
data = response.json()
print(data)
assert response.status_code==200
assert response.headers['content-type']== 'application/json'
assert data['status']== 'placed'
assert data['complete'] == True