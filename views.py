from flask import render_template
from app import app, db

x = 0

@app.route('/')
def index():
    global x
    x += 1
    return render_template('home.html', licznik=x)

@app.route('/add_tick')
def add_tick():
    response = 'You added a new tick. :)'
    return render_template('home.html', response=response)


@app.route('/statistics')
def statistics():
    x = 'usmiech'
    return render_template('statistics.html', chart=x)

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

