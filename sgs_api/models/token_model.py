import uuid

from sgs_api.database import db

class TokenModel(db.Model):
    token_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    value = db.Column(db.String(100))
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.value = str(uuid.uuid4())
        
    def __repr__(self):
        return (
                f"id: {self.id}"
                f"user_id: {self.user_id}"
                f"value: {self.value}"
                )