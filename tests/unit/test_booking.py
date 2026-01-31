from app import app
import datetime

def test_book_past_competition():
    client = app.test_client()

    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Competition is close" in response.data

def test_purchase_13_places():
    client = app.test_client()

    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Test',
        'places': 13
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"No more than 12 places" in response.data

def test_purchase_13_two_times():
    client = app.test_client()

    client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Test',
        'places': 6
    })

    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Test',
        'places': 7
    }, follow_redirects=True)

    assert b"Error" in response.data

def test_buy_limit():
    client = app.test_client()

    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Test',
        'places': 5
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Not enough points to buy" in response.data
