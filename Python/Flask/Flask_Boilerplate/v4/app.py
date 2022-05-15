## We can use the models to create the database using flask migrate (flask wrapper for sql-alemibic)
## Ref: https://youtu.be/jTiyt6W1Qpo

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

## Set up our models (which are going to be used to create the tables in the database)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"User('{self.name}', '{self.location}'"


@app.route("/")
def show_all():
    allUsers = User.query.all()
  
    return f'{ str(allUsers) }'

@app.route('/<name>/<location>')
def index(name, location):
    user= User(name=name, location=location) # User(database column = actual data) 
    db.session.add(user)
    db.session.commit()

    return '<h1>added new user: ' + user.name + '</h1>'

app.route('/<name>')
def get_user(name):
    user = User.query.filter_by(name=name).first()
    return f'The user is locatied in: { user.location}'


## Creating the database 
@app.route("/create")
def create_user():
    db.create_all() # Creates the database in the first place 
    ## Create some example users
    user1 = User(name='homer', location='springfield') 
    user2 = User(name='marge', location='springfield')
    ## add the example users
    db.session.add(user1, user2)
    # commit to the database
    db.session.commit()
    
    return "users created" 

if __name__ == '__main__':
    app.run(debug=True)