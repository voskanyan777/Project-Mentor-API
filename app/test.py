from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_user_profiles():
    response = client.get('profile/v1/user_profiles?limit=10&offset=0')
    assert response.status_code == 200
