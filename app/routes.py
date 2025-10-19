from app import app
from flask import render_template
from app.models import db, User


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title='Home')