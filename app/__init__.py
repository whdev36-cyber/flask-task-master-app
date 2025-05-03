from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
# login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static',
                static_url_path='/')  # Initialize Flask application
    app.config.from_object('config.Config')  # Load configuration from config.py

    # Initialize extensions
    db.init_app(app) # Initialize SQLAlchemy

    # login_manager.init_app(app) # Initialize Flask-Login
    # login_manager.login_view = 'auth.login' # Set the login view for Flask-Login
    # login_manager.login_message = 'Please log in to access this page.' # Set the login message for Flask-Login
    # login_manager.login_message_category = 'info' # Set the login message category for Flask-login

    # Register blueprints
    from . import views, auth
    app.register_blueprint(views.bp, url_prefix='/') # Register the main blueprint
    app.register_blueprint(auth.bp, url_prefix='/') # Register the auth blueprint
    # app.register_blueprint(admin.bp) # Register the admin blueprint

    return app # Return the Flask application instance
