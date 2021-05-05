from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from sgs_api.database import db
from sgs_api.models.plan_model import PlanModel
from sgs_api.schemas.plan_schema import PlanSchema

PLAN_ENDPOINT = "/sgs_api/plans"

class PlanResource(Resource):
    def get(self, id=None):
        if not id:
            return self._get_all_plans(), 200
        ##TODO: This should be built out a bit to allow for more complex queries
        try:
            return self._get_plan_by_owner(id), 200
        except NoResultFound:
            abort(404, message="No projects by owner!")
    
    def _get_all_plans(self):
        plans = PlanModel.query.all()
        plans_json = [PlanSchema().dump(plan) for plan in plans]
        return plans_json
        
    def _get_plan_by_owner(self, owner_id):
        plans = PlanModel.query.filter_by(owner_id=owner_id)
        plans_json = [PlanSchema().dump(plan) for plan in plans]
        return plans_json

    def post(self):
        plan = PlanSchema().load(request.get_json())
        
        try:
            db.session.add(plan)
            db.session.commit()
            
        except IntegrityError as e:
            abort(500, message="unexpected error")
            
        else:
            return plan.plan_id, 201