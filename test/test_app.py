from app.app import app
import pytest


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode(
        'utf-8') == "Welcome to the AWS Learning Platform!"
