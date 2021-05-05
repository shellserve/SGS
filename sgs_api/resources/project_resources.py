#import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from sgs_api.database import db 
from sgs_api.models.project_model import ProjectModel
from sgs_api.schemas.project_schema import ProjectSchema

PROJECT_ENDPOINT = "/sgs_api/projects"
#logger = logging.getLogger(__name__)

class ProjectResource(Resource):
    def get(self, id=None):
        if not id:
            return self._get_all_projects(), 200
        
        try:
            return self._get_project_by_owner(id), 200
        except NoResultFound:
            abort(404, message="No projects by owner!")
        
    def _get_all_projects(self):
        projects = Project.query.all()
        projects_json = [ProjectSchema().dump(project) for project in projects]
        return projects_json
    
    def _get_project_by_owner(owner_id):
        projects = Project.query.filter__by(owner_id=owner_id)
        projects_json = [ProjectSchema().dump(project) for project in projects]
        return projects_json

    def post(self):
        project = ProjectSchema().load(request.get_json())

        try:
            db.session.add(project)
            db.session.commit()

        except IntegrityError as e:
            abort(500, message="unexpected error")
            
        else:
            return project.project_id, 201