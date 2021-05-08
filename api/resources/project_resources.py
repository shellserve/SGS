#import logging

from flask import request
from flask_restful import abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from api.database import db
from api.auth import ProtectedResource 
from api.models.project_model import ProjectModel
from api.schemas.project_schema import ProjectSchema
#Need to define an end point.
PROJECT_ENDPOINT = "/apiv1/projects"
#logger = logging.getLogger(__name__)

class ProjectResource(ProtectedResource):
    #this is the GET handler function. It is used to switch the incoming get to private handlers.
    def get(self, id=None):
        if not id:
            return self._get_all_projects(), 200
        
        try:
            return self._get_project_by_owner(id), 200
        except NoResultFound:
            abort(404, message="No projects by owner!")
    
    def _get_all_projects(self):
        projects = ProjectModel.query.all()
        projects_json = [ProjectSchema().dump(project) for project in projects]
        return projects_json
    
    
    def _get_project_by_owner(self, owner_id):
        projects = ProjectModel.query.filter_by(owner_id=owner_id)
        projects_json = [ProjectSchema().dump(project) for project in projects]
        return projects_json

    def post(self):
        #Uses the Marshmallow Schema.load() to initalize our ProjectSchema object
        # request.get_json() is a flask method that allows us to pull in POST json data an returns a pythonic dictonary.
        # The load method runs the build_project() function returning a processed ProjectModel
        project = ProjectSchema().load(request.get_json())

        try:
            # Add our ProjectModel object into the DB. 
            db.session.add(project)
            db.session.commit()

        except IntegrityError as e:
            abort(500, message="unexpected error")
            
        else:
            return project.project_id, 201