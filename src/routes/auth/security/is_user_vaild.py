from flask import request
import jwt

from src.models.user import User


def is_user_token_valid(token):
    decoded_token = jwt.decode(token, algorithms="HS256", options={"verify_signature": False})
    sub = decoded_token.get("sub")
    if sub is None or "user_id" not in sub:
        return False 
    user_id = sub["user_id"]
    user = User.query.get(user_id)
    if not user:
        return False
    return True