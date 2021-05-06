from flask_login import UserMixin
from sgs_api.database import db

class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
    project = db.relationship('ProjectModel')
    plan = db.relationship("PlanModel")
  
    def __repr__(self):
        return (
            f"***User***\n"
            f"user_id: {self.user_id}\n"
            f"email: {self.email}\n"
            f"name: {self.name}\n"
            )