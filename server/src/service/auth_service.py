from database import SessionLocal
from model import User

db = SessionLocal()

class AuthService:
    @staticmethod
    def login(email: str, password: str):
        pass