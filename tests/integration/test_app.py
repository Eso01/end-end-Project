from src.main import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_password_generation(client):
    """Test password generation endpoint"""
    test_data = {
        'min_length': 12,
        'special_chars': 2,
        'numbers': 2,
        'num_passwords': 3
    }
    response = client.post('/generate-passwords', json=test_data)
    assert response.status_code == 200
    assert len(response.json) == 3
