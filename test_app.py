import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from GitHub Actions and Jenkins CI/CD Pipeline!" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_version(client):
    response = client.get('/version')
    assert response.status_code == 200
    data = response.get_json()
    assert data['version'] == '1.0.0'

def test_invalid_endpoint(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
