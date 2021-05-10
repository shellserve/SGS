from marshmallow import Schema, fields, post_load
<<<<<<< HEAD:api/schemas/project_schema.py
from api.models.project_model import ProjectModel
=======
from sgs_api.models.project_model import ProjectModel
from sgs_api.schemas.user_schema import UserSchema

>>>>>>> parent of 0862c3f (Cleaned Up the Model relationships):sgs_api/schemas/project_schema.py
class ProjectSchema(Schema):
    #Our schema extends the marshmallow library, 
    # this allows us to impement basic pre & post processing validation
    project_id = fields.Integer()
    owner_id = fields.String(allow_none=False)
    name = fields.String(allow_none=False)
    objective = fields.String(allow_none=False)
    
    #TODO Create feature to pull user_id from email field then append project record to User projects
    
    @post_load
    #This is run after the input data has been processed.
    def make_project(self, data, **kwargs):
        return ProjectModel(**data)
