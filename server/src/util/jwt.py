from jose import jwt
from datetime import datetime, timedelta
import os


class Jwt:
    @staticmethod
    def generate_access_token(payload: dict, expires_in_minutes: int = 15):
        secret = os.getenv("JWT_SECRET_KEY")
        expires_at = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
        payload["exp"] = expires_at
        token = jwt.encode(payload, f"{secret}", algorithm="HS256")
        return token

    @staticmethod
    def generate_refresh_token(payload: dict, expires_in_days: int = 30):
        secret = os.getenv("SECRET_KEY")
        expires_at = datetime.utcnow() + timedelta(days=expires_in_days)
        payload["exp"] = expires_at
        token = jwt.encode(payload, f"{secret}", algorithm="HS256")
        return token
