from sqlalchemy import Column, Integer, String
from database import Base
from passlib.context import CryptContext
import uuid

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=str(uuid.uuid4))
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    @staticmethod
    def password_hash(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password:str , hashed_password:str):
        return pwd_context.verify(plain_password, hashed_password)
