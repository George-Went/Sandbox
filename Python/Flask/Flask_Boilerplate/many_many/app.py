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

user_channel = db.Table('user_channel',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    following = db.relationship('Channel', secondary=user_channel, backref='followers')

    def __repr__(self):
        return f'<User: {self.name}>'

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f'<Channel: {self.name}>'


# Creates the database
db.create_all() 
## Create a example item 
homer = User(name="Homer")
marge = User(name="Marge")

netflix = Channel(name="Netflix")
appleTV = Channel(name="AppleTV")

## add an example post 
db.session.add_all([homer, marge, netflix, appleTV])

# commit to the database
db.session.commit()

## linking the many to many relationship 
## we can append a database - to "add onto the end" of the user
homer.following.append(netflix)
homer.following.append(netflix)
homer.following.append(netflix)
db.session.commit()