## -----------------------------------
## Setting up a sqllite database 
## -----------------------------------

## If your creating the database for the first time
## In a python3 terminal :
##  from app import db
##  db.create_all()
##  exit()

## We can add user in a python3 terminal using:
## >>> from app import db,User
## >>> user1 = User(name='homer', location='springfield')
## >>> db.session.add(user1)
## >>> db.session.commit()
## >>> exit()

from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

DEBUG = True
app = Flask(__name__)
## generating a "fake" sqlite database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boilerplate.db"
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)

## Set up our models (which are going to be used to create the tables in the database)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"User('{self.id}','{self.name}', '{self.location}', '{self.date_created}')"

## Setting up the Routing 
@app.route("/")
def show_all():
    allUsers = User.query.all()
  
    return f'{ str(allUsers) }' # Displays all Users

if __name__ == '__main__':
    app.run(debug=True)