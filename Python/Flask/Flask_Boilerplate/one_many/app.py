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


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pubished_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('posts', lazy=True))
    ## db.relationship (table, backref(table))
    ## "backref" or back-referance just means that aswell as Post pointing to catagory, catagory also points to post 
    ## two tables pointing at eachother 

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


# Creates the database
db.create_all() 
## Create a example category 
catagory1 = Category(name='Python')

## create a example post (note that we added a catagory which instead of being a single variable, is a entire object)
Post(title='Hello Python!', body='Python is pretty cool', category=catagory1)

## add an example post 
post1 = Post(title='Snakes', body='Ssssssss')

## appened 
catagory1.posts.append(post1)

# we only have to add one of the objects - all other objects assosiated/ related with it will be added as well
db.session.add(catagory1)

# commit to the database
db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)