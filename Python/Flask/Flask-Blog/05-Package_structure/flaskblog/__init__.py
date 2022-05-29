from logging import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # the name of the flask app is "app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "hello secret"  # secret key that is added to forms - allowing us to check that the return values arent trying to execute code
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # this stores the data as a local file in the current directory (the "site.db" file)


db = SQLAlchemy(app)  # we import whis varible into the sqldatabase when creating the sql tables

from flaskblog import routes 

