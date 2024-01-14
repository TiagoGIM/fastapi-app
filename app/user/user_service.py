from app.user.user_model import User , UserCreateDTO , UserLoginDTO
from app.user.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_dto: UserCreateDTO):
        user = User(**user_dto.dict())
        return self.user_repository.create_user(user)

    def update_user(self, user_id: int, updated_user_dto: UserCreateDTO):
        updated_user = User(**updated_user_dto.dict())
        return self.user_repository.update_user(user_id, updated_user)
    
    def get_users(self):
        return self.user_repository.get_all()
    
    def login(self, user_login:  UserLoginDTO):
        found_user = self.user_repository.find_user_by_username(user_login.username)
        return  found_user.verify_password(user_login.password) if found_user else None