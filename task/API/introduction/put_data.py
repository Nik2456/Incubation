import json

import requests

file=open('post_data.json','r')
input_data=file.read()
payload=json.loads(input_data)
request_header = {"x-api-key": "reqres-free-v1"}
url="https://reqres.in/api/users"
response = requests.put(url, headers=request_header, data=payload)
status_code = response.status_code
print(status_code)
print(response.json())
print(response.url)