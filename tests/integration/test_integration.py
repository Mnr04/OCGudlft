import pytest
from app import app, clubs, competitions


def test_fonctionnalite_buy_full():
    """
        un utilisateur arrive, se connecte, achète, et repart.
    """
    client = app.test_client()

    email_test = "john@simplylift.co"
    response = client.post('/showSummary', data={'email': email_test}, follow_redirects=True)
    assert response.status_code == 200

    response = client.post('/purchasePlaces', data={
        'club': "She Lifts",
        'competition': "Test",
        'places': 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    assert b"Points available: 17" in response.data

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200