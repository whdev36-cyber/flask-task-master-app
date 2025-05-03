from flask import Blueprint, render_template as render, redirect, flash, url_for, request as req
from  flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, UserCreationForm, TaskForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__) # Create a blueprint for the authentication module

@bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have successfully logged in!', category='success')
            next_page = req.args.get('next')
            return redirect(next_page or url_for('main.home'))
        else:
            flash('Invalid password or email, please try again!', category='error')
    return render('login.html', form=form)