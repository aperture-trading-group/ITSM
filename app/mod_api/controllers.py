from flask import Blueprint

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')

# Set the route and accepted methods
@mod_api.route('/test/', methods=['GET'])
def test():
    return "hello world"