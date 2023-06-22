from fastapi import APIRouter
from service.auth_service import AuthService
from fastapi import Response
from schema.user_schema import LoginUser, RegisterUser
from fastapi import HTTPException

router = APIRouter()
auth_service = AuthService()


@router.post("login")
async def login(user: LoginUser, response: Response):
    data = auth_service.login(email=user.email, password=user.password)
    if data is None:
        raise HTTPException(status_code=404, detail="Invalid email or password")