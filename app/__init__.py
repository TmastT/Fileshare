from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_app():
    from app.models import User
    login = LoginManager(app)
    login.login_view = 'login'
    login.login_message_category = 'info'

    from . import models
    from . import routes

    app.register_blueprint(routes.routes)

    @login.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
    return app
