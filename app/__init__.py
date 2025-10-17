from flask import Flask, render_template
from .models import db

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py', silent=True)

    @app.route('/index')
    def index():
        return render_template('base.html', app_name=app.config.get('APP_NAME', 'File Sharing App'))


    return app
