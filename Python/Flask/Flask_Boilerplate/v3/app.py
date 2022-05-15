from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boilerplate.db"  ## Fake database
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"User('{self.id}','{self.name}', '{self.location}', '{self.date_created}')"



## Website root shows all students in database
@app.route("/")
def show_all():
    return render_template("show_all.html", users=User.query.all())

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


if __name__ == "__main__":
    app.run(debug=True)