from flask import request
from flask_restful import abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from api.database import db
from api.auth import ProtectedResource
from api.models.action_model import ActionModel
from api.schemas.action_schema import ActionSchema

ACTION_ENDPOINT = "/sgs_api/actions"

class ActionResource(ProtectedResource):
    def get(self, id=None):
        if not id:
            return self._get_all_actions(), 200
        ##TODO: This should be built out a bit to allow for more complex queries
        try:
            return self._get_action_by_plan(id), 200
        except NoResultFound:
            abort(404, message="No actions by owner!")
    
    def _get_all_actions(self):
        actions = ActionModel.query.all()
        actions_json = [ActionSchema().dump(action) for action in actions]
        return actions_json
        
    def _get_action_by_owner(self, plan_id):
        actions = ActionModel.query.filter_by(plan_id=plan_id)
        actions_json = [ActionSchema().dump(action) for action in actions]
        return actions_json

    def post(self):
        action = ActionSchema().load(request.get_json())
        
        try:
            db.session.add(action)
            db.session.commit()
            
        except IntegrityError as e:
            abort(500, message="unexpected error")
            
        else:
            return action.action_id, 201