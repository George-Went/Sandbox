## To Run
## export FLASK_APP=__init.py
## flask run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # set database varaible

def create_app():
    #Flask Config varaibles
    app = Flask(__name__)
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True

    # Initilise database
    db.init_app(app)

    # Import Blueprints
    from .api.routes import api
    from .site.routes import site

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(site)
    
    return app

if __name__ == "__main__":
    create_app().run()