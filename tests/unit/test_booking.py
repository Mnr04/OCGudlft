import server
from server import app


def test_book_past_competition():
    """
    Test booking for a past competition.
    """
    server.clubs = [{
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    }]
    server.competitions = [{
        "name": "Past Comp",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    }]
    server.history = []

    client = app.test_client()
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Past Comp',
        'places': 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Competition is close" in response.data


def test_purchase_13_places():
    """
    Test that a user cannot book more than 12 places in a single request.
    """
    server.clubs = [{
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "20"
    }]
    server.competitions = [{
        "name": "Future Comp",
        "date": "2028-10-22 13:30:00",
        "numberOfPlaces": "20"
    }]
    server.history = []

    client = app.test_client()
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Future Comp',
        'places': 13
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"No more than 12 places" in response.data


def test_purchase_13_two_times():
    """
    Test that a user cannot take 12 places in multiple requests.
    """
    server.clubs = [{
        "name": "She Lifts",
        "email": "kate@shelifts.co.uk",
        "points": "20"
    }]
    server.competitions = [{
        "name": "Future Comp",
        "date": "2028-10-22 13:30:00",
        "numberOfPlaces": "20"
    }]
    server.history = []

    client = app.test_client()

    client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Future Comp',
        'places': 6
    })

    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Future Comp',
        'places': 7
    }, follow_redirects=True)

    assert b"Error" in response.data


def test_buy_limit():
    """
    Test that a club cannot book places if they dont have enouggh points.
    """
    server.clubs = [{
        "name": "Iron Temple",
        "email": "admin@irontemple.com",
        "points": "4"
    }]
    server.competitions = [{
        "name": "Future Comp",
        "date": "2028-10-22 13:30:00",
        "numberOfPlaces": "20"
    }]
    server.history = []

    client = app.test_client()
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Future Comp',
        'places': 5
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Not enough points to buy" in response.data


def test_points_are_deducted():
    """
    Test that points are correctly remove after a purchase.
    """
    server.clubs = [{
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    }]
    server.competitions = [{
        "name": "Future Comp",
        "date": "2028-10-22 13:30:00",
        "numberOfPlaces": "20"
    }]
    server.history = []

    client = app.test_client()
    client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Future Comp',
        'places': 2
    }, follow_redirects=True)

    club = [c for c in server.clubs if c['name'] == 'Simply Lift'][0]
    assert int(club['points']) == 11


def test_no_book_more_than_available():
    """
    Test that a user cannot book more places than has available.
    """
    server.clubs = [{
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    }]
    server.competitions = [{
        "name": "Small Comp",
        "date": "2028-10-22 13:30:00",
        "numberOfPlaces": "1"
    }]
    server.history = []

    client = app.test_client()
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Small Comp',
        'places': 6
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Not enough places available" in response.data
