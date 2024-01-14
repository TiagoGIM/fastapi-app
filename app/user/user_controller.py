from fastapi import APIRouter, HTTPException
from ..user.user_service import UserService
from ..user.user_model import UserResponseDTO, User , UserLoginDTO

router = APIRouter(
    prefix="/users",
    tags=["users"]
)
user_service = UserService()

@router.post("/")
def create_user(user: User):
    created_user = user_service.create_user(user)
    return {"message": "User created successfully", "user": created_user.dict()}

@router.put("/{user_id}", response_model=UserResponseDTO)
async def update_user(user_id: int, updated_user: User):
    updated_user = user_service.update_user(user_id, updated_user)
    return updated_user

@router.get("/")
def get_users():
    return user_service.get_users()

@router.post("/login")
async def login(user_login : UserLoginDTO):
   return user_service.login(user_login)