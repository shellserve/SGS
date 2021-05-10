from api.database import db

class ActionModel(db.Model):
    __tablename__ = 'actions'
    action_id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.plan_id'), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    responsible_party = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    end_date = db.Column(db.String(20), nullable=False)
    
    plan = db.relationship('PlanModel')

    def __repr__(self):
        return (
            f"***ActionStep***\n"
            f"action_id: {self.action_id}\n"
            f"plan_id: {self.plan_id}\n"
            f"description: {self.description}\n"
        )