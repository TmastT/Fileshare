from flask import Flask

def create_app():
    app = Flask(__name__)

    # Config
    app.config.from_pyfile('config.py', silent=True)

    # Blueprints

    return app