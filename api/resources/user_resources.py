#import logging
import string
import random

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash

from api.database import db 
from api.auth import ProtectedResource
from api.models.user_model import UserModel 
from api.models.token_model import TokenModel
from api.schemas.user_schema import UserSchema

LOGIN_ENDPOINT = "/sgs_api/login"
LOGOUT_ENDPOINT = "/sgs_api/logout"
SIGNUP_ENDPOINT = "/sgs_api/signup"
DEV_TOKEN = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(248))
#logger = logging.getLogger(__name__)
class LoginResource(Resource):
    def get(self, session=None):
        pass
    
    def post(self):
        request_json = request.get_json()
        if ('email' in request_json or 'name' in request_json) and 'password' in request_json:
            user = UserModel.query.filter_by(email=request_json['email'], name=request_json['name']).first()
            if user is None:
                return {'message':'Incorrect Credentials!'}, 404
            if check_password_hash(user.password, request_json['password']):
                token = TokenModel(user.user_id)
                try:
                    db.session.add(token)
                    db.session.commit()
                    return {
                        "token": token.value
                    }                    
                except IntegrityError as e:
                    abort(500, message='unexpected error')
            else:
                return {'message':'Incorrect Credentials!'}, 404
        else:
            return {'message':'No Credentials!'}, 400

class LogoutResource(ProtectedResource):
    def get(self):
        #TODO: Duplicate code from auth.py consider reduction
        token_raw = str(request.headers.get('Authorization'))

        try:
            token = TokenModel.query.filter_by(value=token_raw).delete()            
            db.session.commit()
        
        except IntegrityError as e:
            abort(500, message="unexpected error")
            
        else:
            return 201   

class SignupResource(Resource):
    def get(self, session=None):
        pass
    
    def post(self):
        request_json = request.get_json()
        request_json['password'] = generate_password_hash(request_json['password'])
        user = UserSchema().load(request_json)
        
        try:
            db.session.add(user)
            db.session.commit()
        
        except IntegrityError as e:
            abort(500, message="unexpected error")
            
        else:
            return 201          