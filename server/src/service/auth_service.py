from database import SessionLocal
from model import User

db = SessionLocal()


class AuthService:
    
    @staticmethod
    def login(email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if user and User.verify_password(password, user.password):
            return {"message": "Login is successful", "user_id": user.id}
        else:
            return {"message": "Invalid email or password"}
