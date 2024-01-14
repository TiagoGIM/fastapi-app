from user.user_service import UserService
from user.user_model import UserCreateDTO
import pytest 

@pytest.fixture
def user_service():
    return UserService()



def test_create_user(user_service):
    user_dto = UserCreateDTO(username="testuser", password="testpassword", email="smeemai@email.com")
    created_user = user_service.create_user(user_dto)
    assert created_user.username == "testuser"