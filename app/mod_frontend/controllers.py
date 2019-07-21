from flask import Blueprint, render_template

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_frontend = Blueprint('frontend', __name__, url_prefix='/')

# Set the route and accepted methods
@mod_frontend.route('/')
@mod_frontend.route('/dashboard/', methods=['GET'])
def dashboard():
    return render_template("mod_frontend/dashboard.html")