from marshmallow import Schema, fields, post_load
from sgs_api.models.plan_model import PlanModel
from sgs_api.schemas.project_schema import ProjectSchema

class PlanSchema(Schema):
    plan_id = fields.Integer()
    owner_id = fields.Integer(allow_none=False)
    project_id = fields.Integer(allow_none=False)
    goal = fields.String(allow_none=False)
    project = fields.Nested(ProjectSchema(), dump_only=True)
    @post_load
    def make_project(self, data, **kwargs):
        return PlanModel(**data)