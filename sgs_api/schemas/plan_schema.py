from marshmallow import Schema, fields, post_load
from sgs_api.models.plan_model import PlanModel

class PlanSchema(Schema):
    plan_id = fields.Integer()
    owner_id = fields.Integer(allow_none=False)
    project_id = fields.Integer(allow_none=False)
    goal = fields.String(allow_none=False)
    
    @post_load
    def make_project(self, data, **kwargs):
        return PlanModel(**data)