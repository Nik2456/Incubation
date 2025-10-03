

def test_login(sample_data):
    assert sample_data["username"] == "test_user"
    assert sample_data["password"] == "secret"