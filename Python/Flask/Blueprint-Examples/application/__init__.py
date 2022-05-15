from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import blueprints
from .tasks.routes import tasks
from .main.routes import main
from .models import 

db = SQLAlchemy()

## Factory function to create application
def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + '../test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Secret"

    
    ## Initilise application
    db.init_app(app)    


    # Register blueprints
    app.register_blueprint(tasks, url_prefix='/tasks')
    app.register_blueprint(main)
    
    return app 

