from app import app
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models import db, User
from .forms import LoginForm
from urllib.parse import urlparse, urljoin

routes = Blueprint('routes', __name__)

def is_safe(url):
    reference = urlparse(request.host_url)
    test = urlparse(urljoin(request.hot_url, reference))
    return test.scheme in ('http', 'https') and \
        reference.netloc == test.netloc

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.passsword.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page and is_safe(next_page) else redirect(url_for('index'))
        else:
            flash('Login Attempt Failed')
    return render_template('login.html', title='Login', form=form)