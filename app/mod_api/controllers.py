from flask import Blueprint

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')

# Set the route and accepted methods
@mod_api.route('/test/', methods=['GET'])
def test():
    """
    Returns test string.

        **Example request**:

        .. sourcecode:: http

          GET /api/test1 HTTP/1.1
          Accept: application/json

        **Example response**:

        .. sourcecode:: http

          HTTP/1.1 200 OK
          Content-Type: application/json

          {"test-message": "Hello world."}

        :query sort: No sorting.
        :query q: N/A
        :resheader Content-Type: application/json
        :status 200: posts found
        :returns: :class:`app.mod_api.StatusMessage`
    """
    return {"test-message": "Hello world."}