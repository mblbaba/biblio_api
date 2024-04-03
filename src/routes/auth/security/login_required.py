import functools

from flask import make_response, request

from src.routes.auth.security.is_user_vaild import is_user_token_valid

def login_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        access_tokken = request.headers.get("access-tokken")
        if not access_tokken:
            response = {
                "message" : "you need to login fisrt",
                "success" : -1
            }
            return make_response(response, 401)
        
        elif not is_user_token_valid(access_tokken):
            response = {
                "message" : "Invalid access token",
                "success" : -1
            }
            return make_response(response, 401)
        else :
            return func(*args, **kwargs)
    return decorator