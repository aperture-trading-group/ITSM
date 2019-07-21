import os
import tempfile

import pytest
import sys
#sys.path.insert(0, os.path.abspath('../'))

from app import app


@pytest.fixture
def client():
    #app.config['TESTING'] = True
    client = app.test_client()

    #with app.app.app_context():
    #    app.init_db()

    yield client

def test_the_test_message(client):
    """Test the test message."""

    rv = client.get('/api/test/')
    assert b'No entries here so far' not in rv.data
    json_data = rv.get_json()
    assert 'test-message' in json_data
