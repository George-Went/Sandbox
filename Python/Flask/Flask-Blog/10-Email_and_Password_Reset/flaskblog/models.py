from datetime import datetime
from flaskblog import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer # allows us to generate tokens that last 30 seconds 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User Models
class User(db.Model, UserMixin):  # we can import UserMixin from the flask-login classes 
    id = db.Column(db.Integer, primary_key=True)  # id is a primary key
    username = db.Column(db.String(20), unique=True, nullable=False)  # username has to be: 20 chars, unique, not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")  # default value
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)  # the lazy argument means that sql aclehmy will load the data from the db one object at a time

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec) # generate token
        return s.dumps({'user_id': self.id}).decode('utf_8')

    @staticmethod 
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try: 
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self,):  # this is how our object is printed when someone requets the object
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

# Generates sqlite database from tables 
db.create_all()