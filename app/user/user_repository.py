from ..user.user_model import UserCreateDTO, User
class UserRepository:
    users = []

    def create_user(self, user: UserCreateDTO):
        user_hashed = User(**user.dict())
        user_hashed.set_password(user.password)
        self.users.append(user_hashed)
        return user

    def update_user(self, user_id: int, updated_user: UserCreateDTO):

        userExits = self.find_user_by_id(user_id)
        

        if userExits:
            self.users[user_id-1] = updated_user
            return updated_user
        return None
        
    def find_user_by_id(self, id):
        if 0 < id <= len(self.users):
            return self.users[id-1]
        return None
    
    def find_user_by_username(self, username):
        user = filter(lambda user: user.username == username , self.users)
        return next(user,None)

    def get_all(self):
        print(self.users)
        return self.users