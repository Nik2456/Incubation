from Incubation.task.api_429.handle_rate_limit import get_with_retry


def test_rate_limit_handling(requests_mock):
    url = "https://api.example.com/data"

    requests_mock.get(
        url,
        [
            {"status_code": 429, "headers": {"Retry-After": "1"}},
            {"status_code": 429, "headers": {"Retry-After": "1"}},
            {"status_code": 200, "json": {"message": "success"}}
        ],
    )


    response = get_with_retry(url, max_retries=3, default_wait=1)
    assert response.status_code == 200
    assert response.json() == {"message": "success"}

url = "https://api.example.com/data"
response = get_with_retry(url)
print(response.json())

