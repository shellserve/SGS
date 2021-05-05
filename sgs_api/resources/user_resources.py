#import logging
import string
import random

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash

from sgs_api.database import db 
from sgs_api.models.user_model import UserModel 
from sgs_api.schemas.user_schema import UserSchema

USER_ENDPOINT = "/sgs_api/auth"
DEV_TOKEN = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(248))
#logger = logging.getLogger(__name__)

class UserResource(Resource):
    def get(self, email=None, password=None):
        try:
            return _get_api_key(email, password)
        except NoResultFound:
            abort(404, message="Incorrect Credentials")
            
    def _get_api_key(self, email, password):
        user = UserModel.query.filter__by(email=email, password=generate_password_hash(password, 'sha256'))
        user_json = UserSchema().dump(user)
        
        if not user_json:
            #logger.warning("Incorrect Credentials Attempted!")
            raise NoResultFound
        
        #logger.warning("Login Success!")
        return DEV_TOKEN
    
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
            return user.user_id, 201

        
        
            