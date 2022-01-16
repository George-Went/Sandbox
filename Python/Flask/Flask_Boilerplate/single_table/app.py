from os import name
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

DEBUG = True
app = Flask(__name__)
## generating a "fake" database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boilerplate.db"
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)

# Basic model to bind to a sql table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self): # __repr__ returns a printable representation of the object
        return f"User('{self.id}','{self.name}', '{self.email}'"
        # return '<User %r>' % self.username


## Removes existing database if one exists 
db.session.query(User).delete()
db.session.commit()

# Creates the database
db.create_all() 
## Create some example users
user1 = User(name='homer', email='homer@springfield.com') 
user2 = User(name='marge', email='marge@springfield.com')
## add the example users
db.session.add(user1)
db.session.add(user2)
# commit to the database
db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)