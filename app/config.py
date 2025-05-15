import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Hardcoded for local development
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:oluwasegun137@localhost:5432/flaskblog'

    # Optional: use an environment variable for production
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
