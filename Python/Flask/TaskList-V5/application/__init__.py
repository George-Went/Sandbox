from flask import Flask


from application.extensions import db, login_manager

from application.main.routes import main
from application.auth.routes import auth
from application.tasks.routes import tasks
from application.crucible.routes import crucible

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + '../test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Secret"
    
    ## Initilise application
    db.init_app(app)
    login_manager.init_app(app)

    # Create a instanced varible for the app (the instance is removed when this function is complete - so i can create the databases)
    with app.app_context(): 
        db.create_all()
    
    # Register blueprints
    app.register_blueprint(main, url_prefix='/', template_folder = 'main/templates')
    app.register_blueprint(auth, url_prefix='/auth', template_folder = 'auth/templates')
    app.register_blueprint(tasks, url_prefix='/tasks', template_folder = 'tasks/templates')
    app.register_blueprint(crucible, url_prefix='/crucible', template_folder = 'crucible/templates')

    return app 

