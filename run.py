# Run a test server.
from app import app
print("http://127.0.0.1:8080/api/test/")
app.run(host='0.0.0.0', port=8080, debug=True)