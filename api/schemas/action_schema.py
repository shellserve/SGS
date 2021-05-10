from marshmallow import Schema, fields, post_load
<<<<<<< HEAD:api/schemas/action_schema.py
from api.models.action_model import ActionModel
from api.schemas.plan_schema import PlanSchema
=======
from sgs_api.models.action_model import ActionModel
>>>>>>> parent of 0862c3f (Cleaned Up the Model relationships):sgs_api/schemas/action_schema.py

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