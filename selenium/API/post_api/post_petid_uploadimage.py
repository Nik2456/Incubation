import requests
headers = {"Content-Type": "multipart/form-data"}
base_url='https://petstore.swagger.io/v2'

def method(pet_id):
    response = requests.post(f"{base_url}/pet/{pet_id}/uploadImage", headers = headers)
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'

method(9223372036854775807)