import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
history = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [
            club for club in clubs
            if club['email'] == request.form['email']
        ][0]
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )
    except IndexError:
        flash("Unknown email")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [
        c for c in competitions
        if c['name'] == competition
    ][0]

    if foundClub and foundCompetition:
        return render_template(
            'booking.html',
            club=foundClub,
            competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [
        c for c in competitions
        if c['name'] == request.form['competition']
    ][0]
    club = [
        c for c in clubs
        if c['name'] == request.form['club']
    ][0]
    placesRequired = int(request.form['places'])

    competition_date = datetime.strptime(
        competition['date'], "%Y-%m-%d %H:%M:%S"
    )

    if competition_date < datetime.now():
        flash("Competition is close")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )

    if placesRequired > int(competition['numberOfPlaces']):
        flash("Not enough places available.")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )

    if placesRequired > 12:
        flash("No more than 12 places")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )

    if placesRequired > int(club['points']):
        flash("Not enough points to buy")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )

    placesTaken = 0
    for order in history:
        if (order['club'] == club['name'] and
                order['competition'] == competition['name']):
            placesTaken += order['places']

    if placesTaken + placesRequired > 12:
        flash(f"Error: You have already booked {placesTaken} places. "
              f"Max 12 places in total.")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )

    competition['numberOfPlaces'] = (
        int(competition['numberOfPlaces']) - placesRequired
    )

    club['points'] = int(club['points']) - placesRequired

    history.append({
        "club": club['name'],
        "competition": competition['name'],
        "places": placesRequired
    })

    flash('Great-booking complete!')
    return render_template(
        'welcome.html',
        club=club,
        competitions=competitions
    )


@app.route('/dashboard')
def pointsDisplay():
    return render_template('dashboard.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
