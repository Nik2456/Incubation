import requests

base_url = "https://petstore.swagger.io/v2"

headers = {"content-type": "application/json"}

def get_method(orderid):

    response = requests.get(f"{base_url}/store/order/{orderid}", headers=headers)
    data = response.json()
    print(data)
    assert response.status_code==200
    assert data['id'] == 5
    assert data['status'] == 'placed'
    assert data['complete'] == True
    assert response.headers['content-type'] == 'application/json'

get_method(5)