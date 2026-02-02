import server
from server import app


def test_fonctionnalite_buy_full():
    """
        Test complet : Login -> Achat -> Logout
    """

    server.clubs = [{
        "name": "Test Club", "email": "test@club.com", "points": "20"
        }]
    server.competitions = [{
        "name": "Test Comp",
        "date": "2028-10-22 13:30:00",
        "numberOfPlaces": "25"
        }]
    server.history = []

    client = app.test_client()

    email_test = "test@club.com"
    response = client.post('/showSummary', data={
        'email': email_test},
        follow_redirects=True)

    assert response.status_code == 200

    response = client.post('/purchasePlaces', data={
        'club': "Test Club",
        'competition': "Test Comp",
        'places': 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

    assert b"Points available: 19" in response.data

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
