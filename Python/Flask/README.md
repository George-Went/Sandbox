# Flask 

## Base Installation 
Ref: https://flask-appbuilder.readthedocs.io/en/latest/installation.html

### Installing python
```
Sudo apt-get install python3
```

### Installing pip
pip is a package manager for python - simiar to how npm is a package manager for node or app-get is a package manager for ubuntu 
```
Sudo apt-get install python3-pip
```

### Setting up Virtual Environments
A virtual python environment (venv) can be used to install different version of packages that your computer already has installed, virtual python environments can be installed using:

To create the virtual environment to run the project on, use
```
pip install virtualenv
```

You can enter the virtual environment by using
```
python3 -m virtualenv venv
```
In a Bash (linux) terminal we can also use 
```
. /venv/bin/activate
```
If successful you should see `(venv)` before your commands on the command line

A virtual environment allows you to run different version of flask on the same computer, it means that you don’t have to worry about conflicting versions of flask or jinja on different applications 
Set your source as the virtual python environment means that you are independent from the python that is running on your machine.

You can leave the virtual environment by using 
```
deactivate
```

### Installing Flask
Once inside the virtual environment install flask
```
(venv) $ ~/CervusDefence$ pip installl flask
```



## Basic program / Hello World
### Creating your first project
Create directory called `HelloWorld` 

If your using an independent development environment (IDE) like VScode, we can open the directory in VScode using 
```
code HelloWorld
```

Add a python file called app.py

We can now create a index route (`/`) in our app that responds with the text "hello world" when opened 
```python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/') # Root page of the website 
def hello():
    return "<h1> Hello World! <h1>"
```

### Running the application
In the terminal run: 
```
export FLASK_APP=app.py
```

Then run 
```
flask run 
```

When a user opens a browser and goes to 
http://localhost:5000/    (you can also use 127.0.0.1:5000)
We can see our sample application 


### Debug mode 
We can run the latest version of code without having to stop and start the server by using flask debug mode 
```
Export FLASK_DEBUG=1
```
This means whenever you save coe in vscode / other ide, it will update the server automatically


### Templating 
We can add html directly into the return string

```python 
from flask import Flask

app = Flask(__name__) # the name of the flask app is "app"

@app.route('/') # Root page of the website 
def hello():
    return "<h2> Hello World! <h2>"

@app.route("/about")
def about(): 
    return "<h1> About Page <h1>"


if '__name__' == '__main__':
    app.run(debug=True)
```

However this looks messy and is a pain in the arse to organise on a large scale 

We can instead use templates, allowing for us to assign html templates with special {{ variable }} names allowing us to import important information into the template 

Templates in flask are done using jinja 2 

We can first create a templates directory 
```
dir templates 
```

Within the templates directory we can create a html template for our home route and our about file 

Note: in VsCode we can type html, then press TAB for a minimal html template

Within our flaskblog app, we now need to import `render_template` from flask
```
from flask import Flask, render_template
```

Instead of returning html strings, we can now return render_templates: 
```
from flask import Flask, render_template

app = Flask(__name__) # the name of the flask app is "app"

@app.route('/') # Root page of the website 
@app.route('/home') # Root page of the website 
def home():
    return render_template('home.html')

@app.route("/about")
def about(): 
    return "<h1> About Page <h1>" # this still uses strings for html generation hehe 


if '__name__' == '__main__':
    app.run(debug=True)
```

And the template used: 
templates/about.html
```
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        <h1> About Page</h1>
    </body>
</html>
```

We can also import variables/arrays/dictionarys   into the html templates by using {{ these symbols }} 

Lets say we have a list of posts in a dictionary 
flaskblog.py 
```
posts = [
    {
        'author': 'george' 
        'title': 'hello world'
        'content': 'first blog post'
        'date_posted': '2020'
    },
    {
        'author': 'homer' 
        'title': 'doh'
        'content': 'eat my shorts'
        'date_posted' : '1990'
    }
]
```

Our render template can look like this 
```
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        <h1> Home Page</h1>
        {% for post in posts %}
            <h1> {{ posts.title }}</h1>
            <p> by {{ posts. author }} on {{ posts.date }} </p>
            <p> {{ posts.content }}</p>
        {% endfor %}
    </body>
</html>
```

And the specified route (in flaskblog.py) is: 
```
@app.route("/home") # Root page of the website 
def home():
    return render_template('home.html', posts=posts)
```

If we view the page source. We can see that instead of having the templates it just has both the user posts.

Changing Titles
We can change specific components of a web page depending if a variable was passed or not. One of the examples of this is by changing the title of a web page (the name in the tab bar) .

```
    <head>
        {% if title %}
            <title>Flask Blog - {{ title }}</title> 
        {% else %}
            <title>Flask Blog</title>
        {% endif %}
    </head>
```


Template Inheritance
Instead of copying html code from html templates, we can use blocks that allow us to create a ‘boilerplate’ html template that we can put individual html code on top of.

Before 

about.html
```
<!DOCTYPE html>
<html>
    <head>
        {% if title %}
            <title>Flask Blog - {{ title }}</title> <!-- loads 'title' string in from a route -->
        {% else %}
            <title>Flask Blog</title>
        {% endif %}
    </head>
    <body>
        {% block %} {% endblock %}
    </body>
</html>
```

After 

about.html
```
{% extends "layout.html" %}
{% block content %}
        <h1> About Page</h1>
{% endblock %}
```

layout.html
```
<!DOCTYPE html>
<html>
    <head>
        {% if title %}
            <title>Flask Blog - {{ title }}</title> <!-- loads 'title' string in from a route -->
        {% else %}
            <title>Flask Blog</title>
        {% endif %}
    </head>
    <body>
        {% block %} {% endblock %}
    </body>
</html>
```

Using Bootstrap with flask
Thanks to the usage of block content, we only have to put the bootstrap content in our <head> tag in the layout.html file: 
```
<!DOCTYPE html>
<html>
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

        {% if title %}
            <title>Flask Blog - {{ title }}</title> <!-- loads 'title' string in from a route -->
        {% else %}
            <title>Flask Blog</title>
        {% endif %}
    </head>
    <body>
        {% block content %} {% endblock %}
    </body>
</html>
```

We can also add a navigation form for the site utilising the block content features of jinja2 
navigation.html
```
<header class="site-header">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="#">Flask Blog</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/about">About</a>
            </div>
            <!-- Navbar right side -->
            <div class="navbar-nav">
                <a class="nav-link" href="/login">Login</a>
                <a class="nav-link" href="/register">Register</a>
            </div>
        </div>
</header>
```

Static Resources and CSS

Adding personal CSS 
As css is one of the few things in the site that is not generated, but is considered a “static” resource, it can be put into a separate directory known as `static` (it’s not a template or a python script).

We can then link our css file to the layout.html page so that it is included in the head of every html page we develop (as long as it it uses {% extends layout.html %} at the start.

```
<link rel = "stylesheet" type="text/css" href = "{{ url_for('static', filename='main.css')}}">
```
Instead of writing the file location, we can 

Flask Forms
While we can make forms from scratch (including validation etc) we can instead use wtf-forms which does a lot of this for us.
```
Pip install flask-wtf
```
We can first create a new python file called `forms.py` and we can start writing up the forms as a python class- this is where the form is handled.  

Forms.py
```
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class RegistrationForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
```

We can also add in some validation, allowing us to be able to set string length limits, check emails and see if one form entry is equal to another:
forms.py
```
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
```


We can also add a secret key - for “remember me” and other types of forms that use cookies, a secret key can stop modified cookies and cross site scripting. We can set a secret key by using an “app.config” setting - python app configurations.

```
app.config['SECRET_KEY'] = 'hello secret'
```

We can also use the python interpreter in a command line (bash) to generate a string of random characters

```bash
Import secrets
secrets.token_hex(16)
``` 
This will output 16 random characters that you can use for a secret key 

Creating templates for forms. 
Now that we have some form classes set up, we can set up the front-end html so that a user can see these forms on a page 







Databases
Helpful: https://realpython.com/python-sqlite-sqlalchemy/
We are using the flask_sqlalchemy addons 

There are three most important components in writing SQLAlchemy code:

A Table that represents a table in a database.
A mapper that maps a Python class to a table in a database.
A class object that defines how a database record maps to a normal Python object.


A common object relation mapper (ORM) used with flask for accessing databases is SQLalchemy 

Installing sqlAlchemy 
We can use pip to install flask-sqlAlchemy into our (virtual) environment by using 
```
Pip install flask-sqlaclhemy
```

Faking a database
Instead of setting up and running a sql database, we can just fake it by using a sqlite database 

flaskblog.py
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
```

Sqlalchemy models 
Sqlachemy uses models to help move data from the webserver to the database  
We can also use in-memory-only database using sqlite - this allows us to store a file in the directory of the application instead of having to connect to an actual database

We can view models as a blueprint for form data to go into before being transported into the database


Creating a model 
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
```


Setting up the database from our models
We can use our class models to create the database tables for us! 
First we need to tell where our database is imported into
```
From flaskblog import db
```
Then we need to create the databases to store our tables on
```
db.create_all()
```
Then we can import our models 
```
From flaskblog import User 
```


Note: if using the debug mode to update models, make sure to remove and rebuild the site.db file if the models are changed, otherwise you can run into errors where the session doesnt import the latest version.




















Setting up an API backend for testing API calls 
From: https://flask-appbuilder.readthedocs.io/en/latest/rest_api.html

So we can access websites in ways that aren’t through a browser, curl is one of them we  can use in a terminal

Curl google.com

What you get back is the HTML code that your browser would normally render into a user interface.

We can make web pages that are specifically for sending text instead of a user interface, what’s more, we can send text that fits the protocols for types of data transportation - specifically xml and JSON.

This is known as a API - Application programming interface - a back door into a website that allows users to get data without having to screen scrape a website 



Endpoints are where your use ends up at, such as a login page that renders a form and some css
When the page just spits out JSON data at you, you’ve probably reach what is known as a API endpoint - designed for tools like curl to use, and not the human eye 

Defining custom api endpoints: 
Starting from a new flask-appbuilder skeleton, we can add the below code into the views.py, creating a new API endpoint that can be accessed by using 

Instead of rendering a web page, we can instead send back JSON data 

In views.py 
from flask_appbuilder.api import BaseApi, expose
from . import appbuilder


class ExampleApi(BaseApi):

    resource_name = 'example'

    @expose('/greeting')
    def greeting(self):
        return self.response(200, message="Hello")


appbuilder.add_api(ExampleApi)

When the user goes to curl http://localhost:5000/api/v1/exampleapi/greeting they will get a 
{ message: Hello} 












