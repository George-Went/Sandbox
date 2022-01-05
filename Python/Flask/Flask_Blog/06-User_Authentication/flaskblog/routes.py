from flask import render_template, flash, redirect, url_for
from wtforms.validators import Email
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")  # Create Hashed Password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)  # define a user as a object consisting of the form entries and our newely generated hashed password
        db.session.add(user)  # adding our newely created user
        db.session.commit()  # Commit the above changes to the database
        flash("Your account has been created, you can now log in", "success")  # pop up message saying that an acount has been created
        return redirect(url_for("login"))  # Return user to the login page
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # check if a user == User in our database by checking emails
        if user and bcrypt.check_password_hash(user.password, form.password.data): # if user exists + password they entered into form is valid
            login_user(user, remember=form.remember.data) # login user and adds checkbox asking if they want to be remembered
            flash("you have logged in: " + form.email.data)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger") ## red box that appears up top 
    return render_template("login.html", title="Login", form=form)
