# SGS
Social Governance Systems Internship
#
Using the flask framework we can quickley build out a proof of concept.
For now the app is purley a restful api, but this will allow for easy conversion to a GUI.
App layout
*SGS
  * __init__.py -> Empty
  * api.py -> create_app()
  * constants.py -> PROJECT_ROOT, PROJECT_DB
  * database.py -> db
  * models
    * project_model.py
    * user_model.py
    * _plan_model.py_
  * schemas
    * project_schema.py
    * user_schema.py
    * _plan_schema.py_
  * resources
    * project_resource.py
    * user_resource.py
    * _plan_resource.py_

Model files will define specific sql table implementations. Schema files allow client code to interface with Model objects. Resources allow us to define specic reactions to RESTFUL HTTP methods; GET, POST, DELETE, PUT, PATCH. Once a client is capable of creating a sufficinently detailed plan object with a dynamic number of action steps, and other features we deam necassarry.
