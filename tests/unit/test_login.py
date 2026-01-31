from app import app

def test_login_unknown_email():
    client = app.test_client()
    response = client.post('/showSummary', data={'email': 'unknown@test.com'}, follow_redirects=True)

    assert response.status_code == 200
    assert b"Unknown email" in response.data