import requests

class PetAPI:
    BASE_URL = 'https://petstore.swagger.io/v2/pet'

    def __init__(self, api_key):
        self.headers = {"Content-Type":"application/json"}
    def create_pet(self, body):
        response = requests.post(self.BASE_URL, data=body, headers=self.headers)