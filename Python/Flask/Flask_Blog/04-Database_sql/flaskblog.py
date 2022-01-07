from logging import debug
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)  # the name of the flask app is "app"

app.config["SECRET_KEY"] = "hello secret"  # secret key that is added to forms - allowing us to check that the return values arent trying to execute code
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # this stores the data as a local file in the current directory (the "site.db" file)

db = SQLAlchemy(app)  # we import whis varible into the sqldatabase when creating the sql tables

# User Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id is a primary key
    username = db.Column(db.String(20), unique=True, nullable=False)  # username has to be: 20 chars, unique, not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")  # default value
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)  # the lazy argument means that sql aclehmy will load the data from tsavhe db one object at a time

    def __repr__(self,):  # this is how our object is printed when someone requets the object
        return f"User('{self.username}', '{self.email}'"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column( db.Integer, db.ForeignKey("user.id"), nullable=False
    )  # model knows that user_id is a foreign key

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



## fake database of blog posts is actually a python dictionary
posts = [
    {
        "author": "george",
        "title": "hello world",
        "content": "first blog post",
        "date_posted": "2021",
    },
    {
        "author": "homer",
        "title": "doh",
        "content": "eat my shorts",
        "date_posted": "1990",
    },
]


@app.route("/")  # Root page of the website
def root():
    return "hello!"


@app.route("/home")  # Root page of the website
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")  # About page
def about():
    return render_template("about.html", title="about")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f"Account created for {form.username.data}!", "success"
        )  # pop up message saying that an acount has been created
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "homer@simpson.com" and form.password.data == "homer":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


if "__name__" == "__main__":
    app.run(debug=True)
