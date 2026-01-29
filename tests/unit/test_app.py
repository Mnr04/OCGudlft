import pytest
from app import app

def test_launch_server():
    client = app.test_client()
    result = client.get('/')
    assert result.status_code == 200

def test_login_valid_email():
    client = app.test_client()
    email_test = "john@simplylift.co"
    response = client.post('/showSummary', data={'email': email_test})
    assert response.status_code == 200

def test_login_invalid_email():
    client = app.test_client()
    response = client.post('/showSummary', data={'email': 'wrong@test.com'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Unknown email" in response.data

def test_purchase_places():
    client = app.test_client()

    response = client.post('/purchasePlaces', data={
        'club': "Simply Lift",
        'competition': "Spring Festival",
        'places': 1
    }, follow_redirects=True)

    assert b"Points available: 12" in response.data

def test_purchase_13_places():
    client = app.test_client()

    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'New Classic',
        'places': 13
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Error" in response.data

def test_purchase_13_two_times():
    client = app.test_client()

    client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'New Classic',
        'places': 6
    })

    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'New Classic',
        'places': 7
    }, follow_redirects=True)

    assert b"Error" in response.data