import pytest

@pytest.fixture
def connect_db():
    print("Connecting to DB...")
    yield "DB connection"
    print("Closing DB...")
    
def test_query(connect_db):
    assert connect_db == "DB connection"
    
