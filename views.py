from flask import render_template, request
from app import app, db
from models import Tick
import datetime as dt

x = 0

@app.route('/')
def index():
    global x
    x += 1
    return render_template('home.html', licznik=x)


@app.route('/add_tick', methods=['GET', 'POST'])
def add_tick():
    if request.method == 'POST':
        cities_locations = {'Warsaw': {'longitude': 52.22977, 'latitude': 21.01178}}
        tick_city = request.form['location'] # Warszawa
        tick_location = cities_locations[tick_city]
        date = dt.datetime.strptime(request.form['date'], '%Y-%m-%d')
        age = request.form['age']
        new_tick = Tick(
            longitude=tick_location['longitude'],
            latitude=tick_location['latitude'],
            sex=True,
            age=age,
            is_test=True,
            date=date
        )

        db.session.add(new_tick)
        db.session.commit()

        response = f'You added a new tick from { tick_city }, catched on { date }. You are {age} years old.'
        return render_template('add_tick.html', response=response)
    else:
        response = ''
        return render_template('add_tick.html', response=response)

@app.route('/ticks')
def ticks():
    ticks = Tick.query.all()
    return render_template('ticks_table.html', ticks=ticks)

@app.route('/tick_statistics')
def tick_statistics():
    x = 'usmiech'
    return render_template('tick_statistics.html', chart=x)

@app.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

