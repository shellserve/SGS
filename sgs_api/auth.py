from functools import wraps
from flask import request
from flask_restful import Resource
from sgs_api.models.token_model import TokenModel

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_raw = str(request.headers.get('Authorization'))
        token = TokenModel.query.filter_by(value=token_raw).first()
        if token is not None:
            return func(*args, **kwargs)
        return {"message": "token is invalid or missing"}, 401
    return wrapper

class ProtectedResource(Resource):
    method_decorators = [authenticate]