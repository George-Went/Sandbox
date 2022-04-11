from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
db = SQLAlchemy()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__)

    # Initialize Plugins
    db.init_app(app)


    with app.app_context():
        # Include our Routes
        from .home import routes
        from .tasks import routes

        db.create_all() #Create sql tables from data models

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(tasks.task_bp)

        return app