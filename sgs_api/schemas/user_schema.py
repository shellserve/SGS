from marshmallow import Schema, fields, post_load
from sgs_api.models.user_model import UserModel

class UserSchema(Schema):
    email = fields.String(allow_none=False)
    password = fields.String(allow_none=False)
    name = fields.String(allow_none=False)

    @post_load
    def make_user(self, data, **kwargs):
        return UserModel(**data)
