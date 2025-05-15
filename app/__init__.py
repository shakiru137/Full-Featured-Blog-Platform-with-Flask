from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    # Register blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.blog import bp as blog_bp
    app.register_blueprint(blog_bp)
    
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)
    
    return app

from app import models
