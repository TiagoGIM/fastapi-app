from pydantic import BaseModel
import bcrypt

class User(BaseModel):
    username: str
    email: str
    password: str
    def set_password(self, password: str):
        self.password = bcrypt.hashpw(password.encode('utf8') ,bcrypt.gensalt())

    def verify_password(self, password: str):
        return bcrypt.hashpw(password.encode('utf8'), self.password) == self.password

class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

class UserResponseDTO(BaseModel):
    username: str
    email: str

class UserLoginDTO(BaseModel):
    username: str
    password: str