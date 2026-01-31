from app import app

def test_points_board_display():
    client = app.test_client()

    response = client.get('/dashboard')

    assert response.status_code == 200


    assert b"Simply Lift" in response.data
    assert b"Iron Temple" in response.data
    assert b"She Lifts" in response.data