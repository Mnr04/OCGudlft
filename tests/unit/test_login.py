import server
from server import app


def test_launch_server():
    """
    Test if the server launches correctly.
    """
    client = app.test_client()
    result = client.get('/')
    assert result.status_code == 200


def test_login_unknown_email():
    """
    Test login with an unkwnow email.
    """
    server.clubs = [{
        "name": "Club Test",
        "email": "test@club.com",
        "points": "10"
    }]

    client = app.test_client()
    response = client.post(
        '/showSummary',
        data={'email': 'unknown@test.com'},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Unknown email" in response.data


def test_login_valid_email():
    """
    Test login with a valid email.
    """
    server.clubs = [{
        "name": "Club Test",
        "email": "test@club.com",
        "points": "10"
    }]

    client = app.test_client()
    response = client.post(
        '/showSummary',
        data={'email': 'test@club.com'},
        follow_redirects=True
    )

    assert response.status_code == 200
