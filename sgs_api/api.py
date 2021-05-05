#import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from flask import Flask
from flask_restful import Api

from sgs_api.database import db
from sgs_api.constants import PROJECT_ROOT, PROJECT_DB
from sgs_api.resources.project_resources import ProjectResource, PROJECT_ENDPOINT
from sgs_api.resources.user_resources import UserResource, USER_ENDPOINT
"""    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-8s %(messages)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("sgs_api.log"), logging.StreamHandler()],
    )"""
def create_app(db_location):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    
    api = Api(app)
    api.add_resource(ProjectResource, PROJECT_ENDPOINT, f"{PROJECT_ENDPOINT}/<id>")
    api.add_resource(UserResource, USER_ENDPOINT)
    return app

if __name__ == "__main__":
    app = create_app(f"sqlite:///{PROJECT_ROOT}/{PROJECT_DB}")
    app.run(debug=True)