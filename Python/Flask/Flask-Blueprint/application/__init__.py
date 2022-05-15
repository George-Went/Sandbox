from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.database import db
from application.tasks.routes import tasks

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + '../test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Secret"

    
    ## Initilise application
    db.init_app(app)    

    with app.app_context(): # Create a instanced varible for 
        db.create_all()
    
    # Register blueprints
    app.register_blueprint(tasks, url_prefix='/tasks')


    return app 

