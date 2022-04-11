from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.tasks.routes import tasks

def create_app():  
    # Creating the flask application 
    app = Flask(__name__)          
    app.config.from_object('config') 
    
    db = SQLAlchemy()
    # Setup database tables
    db.create_all()                 

    # Register Blueprints
    app.register_blueprint(tasks, url_prefix="/tasks")

    return app

