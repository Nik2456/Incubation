import requests

url="https://reqres.in"
query_param={'page':'2', 'delay':['3','5']}
request_header = {"Accept": "application/json"}
request_auth = ('user', 'password')
response = requests.get(url, params=query_param, headers=request_header, auth=request_auth)
print(response.url)
print(response.status_code)
