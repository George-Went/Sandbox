# Import main flask library and thrid party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + '../test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Secret"
db = SQLAlchemy(app)

## Create the database table from model
db.create_all()
db.session.commit()

from app import forms
from app import routes