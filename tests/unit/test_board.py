import server
from server import app

def test_points_board_display():
    server.clubs = [
        {"name": "Club A", "email": "a@a.com", "points": "10"},
        {"name": "Club B", "email": "b@b.com", "points": "20"},
        {"name": "Club C", "email": "c@c.com", "points": "30"}
    ]

    client = app.test_client()
    response = client.get('/dashboard')

    assert response.status_code == 200

    assert b"Club A" in response.data
    assert b"Club B" in response.data
    assert b"Club C" in response.data
    assert b"10" in response.data