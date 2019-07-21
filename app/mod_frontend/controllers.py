from flask import Blueprint, render_template

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_frontend = Blueprint('frontend', __name__, url_prefix='/')

# Set the route and accepted methods
@mod_frontend.route('/')
@mod_frontend.route('/dashboard/', methods=['GET'])
def dashboard():
    """
    Returns test string.

        **Example request**:

        .. sourcecode:: http

          GET /api/test1 HTTP/1.1

        **Example response**:

        .. sourcecode:: http

          HTTP/1.1 200 OK

          mod_frontend:dashboard

        :status 200:
        :returns: mod_frontend:dashboard.html
    """
    return render_template("mod_frontend/dashboard.html")
