from marshmallow import Schema, fields, post_load
from api.models.action_model import ActionModel
from api.schemas.plan_schema import PlanSchema

class ActionSchema(Schema):
    action_id = fields.Integer()
    plan_id = fields.Integer(allow_none=False)
    description = fields.String(allow_none=False)
    responsible_party = fields.String(allow_none=False)
    start_date = fields.String(allow_none=False)
    end_date = fields.String(allow_none=False)
    plan = fields.Nested(PlanSchema(), dump_only=True)
    
    @post_load
    def make_action(self, data, **kwargs):
        return ActionModel(**data)