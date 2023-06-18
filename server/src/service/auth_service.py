from database import SessionLocal
from model import User
from util.jwt import Jwt

db = SessionLocal()


class AuthService:
    @staticmethod
    def login(email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if user and User.verify_password(password, user.password):
            access_token = Jwt.generate_access_token(
                {"id": user.id}, expires_in_minutes=15
            )
            refresh_token = Jwt.generate_refresh_token({"id": user.id}, 3)
            return {"access_token": access_token, "refres_token": refresh_token}
        else:
            return False
