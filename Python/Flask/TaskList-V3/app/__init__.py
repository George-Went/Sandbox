# Import main flask library and thrid party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

## Create the database table from model
db.create_all()
db.session.commit()

from app import routes