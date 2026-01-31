from app import app
import datetime

def test_book_past_competition_real_data():
    client = app.test_client()

    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Competition is close" in response.data