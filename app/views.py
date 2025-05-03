from flask import Blueprint, render_template

bp = Blueprint('main', __name__) # Create a blueprint for the main application

@bp.route('/') # Define the route for the home page
def home():
    return render_template('home.html')