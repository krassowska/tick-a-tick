from flask import render_template, request, redirect, flash, url_for
from app import app, db
from models import Tick
import datetime as dt
import json

@app.route('/')
def index():
    ticks = Tick.query.all()

    new_ticks = []
    for tick in ticks:
        new_ticks.append(tick.to_dict())

    ticks = json.dumps(new_ticks)



    return render_template('home.html', ticks=ticks)


@app.route('/add_tick', methods=['GET', 'POST'])
def add_tick():
    if request.method == 'POST':
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        date = dt.datetime.strptime(request.form['date'], '%Y-%m-%d')
        age = request.form['age']
        is_male = (True if request.form['sex'] == 'male' else False)
        is_test = (False if request.form['is_test'] == 'real_tick' else True)
        new_tick = Tick(
            longitude=longitude,
            latitude=latitude,
            sex=is_male,
            age=age,
            is_test=is_test,
            date=date
        )
        db.session.add(new_tick)
        db.session.commit()


        tick_added = f'You added a new tick caught on { dt.datetime.date(date) }. You are {age} years old.'
        flash(tick_added)

        return redirect(url_for('index'), code=302)
    else:
        info = ''
        return render_template('add_tick.html', info=info)

@app.route('/ticks')
def ticks():
    ticks = Tick.query.all()
    return render_template('ticks_table.html', ticks=ticks)

@app.route('/tick_statistics')
def tick_statistics():
    ticks = Tick.query.all()

    new_ticks = []
    for tick in ticks:
        new_ticks.append(tick.to_dict())

    ticks = json.dumps(new_ticks)

    ticks_count = Tick.query.count()
    female_count = Tick.query.filter_by(sex=False).count()
    male_count = Tick.query.filter_by(sex=True).count()
    percent_female = female_count * ticks_count / 100
    percent_male = male_count * ticks_count / 100

    female_median_age = Tick.query.filter_by(sex=False).count()
    male_median_age = Tick.query.filter_by(sex=True).count()

    return render_template(
        'tick_statistics.html',
        ticks_count=ticks_count,
        ticks=ticks,
        female_count=female_count,
        male_count=male_count,
        percent_female=percent_female,
        percent_male=percent_male,
        female_median_age=female_median_age,
        male_median_age=male_median_age
    )

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

