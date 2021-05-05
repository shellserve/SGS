from marshmallow import Schema, fields, post_load
from sgs_api.models.project_model import ProjectModel

class ProjectSchema(Schema):
    owner_id = fields.String(allow_none=False)
    name = fields.String(allow_none=False)
    objective = fields.String(allow_none=False)

    @post_load
    def make_project(self, data, **kwargs):
        return ProjectModel(**data)
