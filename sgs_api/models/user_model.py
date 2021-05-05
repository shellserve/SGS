from flask_login import UserMixin
from sgs_api.database import db

class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return (
            f"***User***"
            f"user_id: {self.user_id}"
            f"email: {self.email}"
            f"name: {self.name}"
            )