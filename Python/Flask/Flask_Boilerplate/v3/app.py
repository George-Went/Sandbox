from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///people.sqlite3"  ## Fake database
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def __init__(self, username, email):
    self.username = username
    self.email = email


db.create_all()
db.session.commit()

# Creating entries for our database 
homer = Person(username='Homer', email='homer@simpson.com')
marge = Person(username='Marge', email='marge@simpson.com')

db.session.add(homer)
db.session.add(marge)
db.session.commit()

result = print(Person.query.all())


## Website root shows all students in database
@app.route("/")
def show_all():
    print(result)
    return render_template("show_all.html", person=Person.query.all())

if __name__ == "__main__":
    app.run(debug=True)