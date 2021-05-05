from sgs_api.database import db

class ProjectModel(db.Model):
    #if you know sql this is very similar to that
    __tablename__ = 'project'
    project_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    name = db.Column(db.String(100))
    objective = db.Column(db.String(1000))
    
    #__repr__ can be called just to get a quick glance at the model variables
    def __repr__(self):
        return (
            f"***Project***"
            f"project_id: {self.project_id}"
            f"owner_id: {self.owner_id}"
            f"name: {self.name}"
            f"objective: {self.objective}"
            )