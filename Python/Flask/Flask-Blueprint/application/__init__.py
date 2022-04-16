from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.database import db
from application.tasks.routes import tasks

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

    ## Initilise application
    db.init_app(app)    

    # Registar blueprints
    app.register_blueprint(tasks, url_prefix='/tasks')
    
    # add example data to database
    
    return app 


 
