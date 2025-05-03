from flask import Blueprint, render_template

bp = Blueprint('auth', __name__) # Create a blueprint for the authentication module

@bp.route('/login')
def login():
    return render_template('login.html')