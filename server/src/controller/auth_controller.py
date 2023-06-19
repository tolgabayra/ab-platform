from fastapi import APIRouter
from fastapi import Request
from service.auth_service import AuthService
from schema.user_schema import LoginUser, RegisterUser

router = APIRouter()


@router.post("login")
async def login(user: LoginUser):
    pass
