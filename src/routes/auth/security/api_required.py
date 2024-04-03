import functools

from flask import make_response, request

from src.routes.auth.security.is_api_valid import is_valid

def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if not request.headers.get('api-key'):
            return make_response({
                "success" : -1,
                "message" : "Please provide an API key",
            }, 401)
        else :
            api_key = request.headers.get('api-key')
        if is_valid(api_key):
            return func(*args, **kwargs)
        else :
            return make_response({
                "success" : -1,
                "message" : "Invalid API key",
            }, 401)
    return decorator