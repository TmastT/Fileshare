from flask import render_template
from . import create_app

app = None

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

