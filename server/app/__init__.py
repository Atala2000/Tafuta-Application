from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Ensure the path to config.py is correct
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), '../config.py'))

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import and register blueprints
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.items import bp as items_bp
    app.register_blueprint(items_bp, url_prefix='/items')

    return app