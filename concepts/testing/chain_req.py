import pytest

@pytest.fixture
def db_connection():
    print("Connecting to DB...")
    return "DB_CONN"

@pytest.fixture
def user_data(db_connection):
    print(f"Fetching user using {db_connection}")
    return {"id": 1, "name": "Shannen"}

def test_user(user_data):
    assert user_data["name"] == "Shannen"
    assert user_data["id"] == 1
    
def test_len(user_data):
    assert len(user_data["name"]) == 7