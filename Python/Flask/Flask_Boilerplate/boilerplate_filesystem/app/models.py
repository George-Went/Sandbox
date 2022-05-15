from app import db
from datetime import datetime



# User Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id is a primary key
    username = db.Column(
        db.String(20), unique=True, nullable=False
    )  # username has to be: 20 chars, unique, not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(20), nullable=False, default="default.jpg"
    )  # default value
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship(
        "Post", backref="author", lazy=True
    )  # the lazy argument means that sql aclehmy will load the data from the db one object at a time

    def __repr__(
        self,
    ):  # this is how our object is printed when someone requets the object
        return f"User('{self.username}', '{self.email}'"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
    )  # model knows that user_id is a foreign key


def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"


