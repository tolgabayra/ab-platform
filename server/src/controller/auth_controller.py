from fastapi import APIRouter
from fastapi import Request
from service.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("login")
async def login(request: Request):
    data = await request.json()


