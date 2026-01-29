import pytest
from app import app, clubs, competitions

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fonctionnalité_buy():
    """
    un utilisateur arrive, se connecte, achète, et repart.
    """

    client = app.test_client()
    email_test = "john@simplylift.co"
    response = client.post('/showSummary', data={'email': email_test})

    assert response.status_code == 200

    club_name = clubs[0]['name']
    competition_name = competitions[0]['name']

    response = client.post('/purchasePlaces', data={
        'club': club_name,
        'competition': competition_name,
        'places': 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

    assert b"Points available: 12" in response.data

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200