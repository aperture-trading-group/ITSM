# Import flask and template operators
from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return "404"

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_api.controllers import mod_api as api_module

# Register blueprint(s)
app.register_blueprint(api_module)
# app.register_blueprint(xyz_module)
# ..
