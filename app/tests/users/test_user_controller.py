from fastapi.testclient import TestClient
from pytest import fixture
from app.user.user_service import UserService
from main import app

client = TestClient(app)


@fixture
def mock_user_service(monkeypatch):

    mock_instance = UserService()
    monkeypatch.setattr("app.user.user_controller.UserService", lambda: mock_instance)

    return mock_instance


def test_get_all_users():
    response =  client.get("/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "email" : "luan"
    }
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"
    assert "user" in response.json()

def test_update_user(mock_user_service):

    user_data = {
        "username": "updateduser",
        "password": "updatedpassword",
        "email": "1231"
    }

    mock_user_service.update_user = user_data


    response = client.put("api/users/1", json=user_data)

    # Verificar as asserções
    assert response.status_code == 200
    assert "username" in response.json()
    assert response.json()["username"] == "updateduser"
