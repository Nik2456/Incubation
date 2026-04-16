import requests

base_url = "https://petstore.swagger.io/v2"

headers = {"content-type": "application/json"}

def method(username,password):

    response =requests.get(f"{base_url}/user/login?username={username}&password={password}", headers= headers)

    data =response.json()
    print(data)
    assert response.status_code==200
    assert 'logged in user' in data['message']
    assert response.headers["content-type"] == "application/json"

method("ABC","abc@1234")
