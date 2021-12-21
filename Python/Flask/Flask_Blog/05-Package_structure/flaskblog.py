from logging import debug
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for

from forms import RegistrationForm, LoginForm
from models import User, Post

app = Flask(__name__)  # the name of the flask app is "app"

app.config["SECRET_KEY"] = "hello secret"  # secret key that is added to forms - allowing us to check that the return values arent trying to execute code
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # this stores the data as a local file in the current directory (the "site.db" file)

db = SQLAlchemy(app)  # we import whis varible into the sqldatabase when creating the sql tables



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
