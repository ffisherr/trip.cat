from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')
