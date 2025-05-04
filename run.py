from app import create_app, db

app = create_app() # Create the Flask application instance

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(' * Database activated!')
    app.run(debug=True) # Run the application in debug mode