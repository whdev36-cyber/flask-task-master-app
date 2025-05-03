import os
import dotenv

dotenv.load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
