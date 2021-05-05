from sgs_api.database import db

class PlanModel(db.Model):
    __tablename__ = 'plans'
    plan_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), nullable=False)
    goal = db.Column(db.String(1000), nullable=False)
    
    def __repr__(self):
        return (
            f"***Plan***\n"
            f"plan_id: {self.plan_id}\n"
            f"owner_id: {self.owner_id}\n"
            f"project_id: {self.project_id}\n"
            f"goal {self.goal}\n"
        )