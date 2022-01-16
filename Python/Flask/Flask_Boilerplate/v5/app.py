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


class UserItem(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')),
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    
    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"UserItem('{self.user_id}','{self.item_id}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    order = db.relationship('Item', secondary=UserItem, backref='order') # the back ref is like a 

    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"User('{self.id}','{self.name}','{self.order}')"

class Item(db.model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"Item('{self.id}','{self.name}')"

