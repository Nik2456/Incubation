import pytest
import requests

def test_get_activities_id():
    base_url = "https://fakerestapi.azurewebsites.net"
    headers = {"Accept": "text/plain"}

    response = requests.get(f"{base_url}/api/v1/Activities/2", headers=headers)
    data = response.json()
    print(data)

    assert response.status_code == 200
    assert data['id'] == 2
    assert data['title'] == 'Activity 2'