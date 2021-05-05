#import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from flask import Flask
from flask_restful import Api

from sgs_api.database import db
from sgs_api.constants import PROJECT_ROOT, PROJECT_DB
from sgs_api.resources.user_resources import UserResource, USER_ENDPOINT
from sgs_api.resources.project_resources import ProjectResource, PROJECT_ENDPOINT


#TODO RE-Implement logging across different resource files.
"""    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-8s %(messages)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("sgs_api.log"), logging.StreamHandler()],
    )"""
def create_app(db_location):
    #A flask object is our webserver when the .run() method is run.
    #We are able to modify all configurable through the app.config dictonary object 
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    
    #A SQLAlchemy object is a pointer into a sqlite db. We can hook it into our app with inti_app
    db.init_app(app)
    with app.test_request_context():
        #This switches context to allow us to initialize the db tables, based on a schema given to it by .init_app(app)
        db.create_all()
    
    #This initializes a Api component for the app
    #We can add different api resources here passing an end/point and sometimes a get variable
    api = Api(app)
    api.add_resource(ProjectResource, PROJECT_ENDPOINT, f"{PROJECT_ENDPOINT}/<id>")
    api.add_resource(UserResource, USER_ENDPOINT)
    return app

if __name__ == "__main__":
    #give app raw sqlite location
    app = create_app(f"sqlite:///{PROJECT_ROOT}/{PROJECT_DB}")
    app.run(debug=True)