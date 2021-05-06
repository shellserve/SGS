from marshmallow import Schema, fields, post_load
from sgs_api.models.action_model import ActionModel

class ActionSchema(Schema):
    action_id = fields.Integer()
    plan_id = fields.Integer(allow_none=False)
    description = fields.String(allow_none=False)
    responsible_party = fields.String(allow_none=False)
    start_date = fields.String(allow_none=False)
    end_date = fields.String(allow_none=False)
    
    @post_load
    def make_action(self, data, **kwargs):
        return ActionModel(**data)