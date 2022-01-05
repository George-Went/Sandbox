from logging import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager, login_manager

app = Flask(__name__)  # the name of the flask app is "app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "hello secret"  # secret key that is added to forms - allowing us to check that the return values arent trying to execute code
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # this stores the data as a local file in the current directory (the "site.db" file)


db = SQLAlchemy(app)  # we import this varible into the sqldatabase when creating the sql tables
bcrypt = Bcrypt(app) # this variable is used when we want to use bcrypts hashing methods 
login_manager = LoginManager(app)

## These create the database from our models - and then commits it to the running sqllite database 
db.create_all()
db.session.commit()


from flaskblog import routes 

