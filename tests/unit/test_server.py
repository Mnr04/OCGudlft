import pytest
from app import app

def test_launch_server():
    client = app.test_client()
    result = client.get('/')
    assert result.status_code == 200