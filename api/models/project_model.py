from api.database import db

class ProjectModel(db.Model):
    #if you know sql this is very similar to that
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(100))
    objective = db.Column(db.String(1000))
    
    plan = db.relationship("PlanModel")
    #__repr__ can be called just to get a quick glance at the model variables
    def __repr__(self):
        return (
            f"***Project***\n"
            f"project_id: {self.project_id}\n"
            f"owner_id: {self.owner_id}\n"
            f"name: {self.name}\n"
            f"objective: {self.objective}\n"
            )