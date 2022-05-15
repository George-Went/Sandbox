from logging import debug
from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # the name of the flask app is "app"

app.config['SECRET_KEY'] = 'hello secret'

## fake database of blog posts is actually a python dictionary 
posts = [
    {
        'author': 'george', 
        'title': 'hello world',
        'content': 'first blog post',
        'date_posted': '2020'
    },
    {
        'author': 'homer', 
        'title': 'doh',
        'content': 'eat my shorts',
        'date_posted': '1990'
    }
]



@app.route("/") # Root page of the website 


@app.route("/home") # Root page of the website 
def home():
    return render_template('home.html', posts=posts)


@app.route("/about") # About page
def about(): 
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # pop up message saying that an acount has been created 
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'homer@simpson.com' and form.password.data == 'homer':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if '__name__' == '__main__':
    app.run(debug=True)