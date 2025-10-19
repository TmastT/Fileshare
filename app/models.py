from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    id: so.Mapped[int] = sa.Column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = sa.Column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = sa.Column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = sa.Column(sa.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)