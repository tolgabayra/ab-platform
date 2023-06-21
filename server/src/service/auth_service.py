from database import SessionLocal
from model import User
from util.jwt import Jwt
from util.password import Password

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

    @staticmethod
    def register(name, surname, email, password):
        hashed_password = Password.get_password_hash(password)
        user = User(name=name, surname=surname, email=email, password=hashed_password)
        db.add(user)
        db.commit()
        return user
    
