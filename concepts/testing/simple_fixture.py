import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

@pytest.mark.skip(reason = "Test not needed at this time")
def test_feature():
    assert True
    
@pytest.fixture
def sample_string():
    return "Test string"

def test_sum(sample_data):
    assert sum(sample_data) == 10
    assert sum(sample_data) < 20
    
def test_str(sample_string):
    assert sample_string[0] == 'T'

@pytest.mark.skipif(condition=False, reason="Feature not implemented")
def test_sample():
    assert True