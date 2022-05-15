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












## Notes on API Testing

### API types

There are currently `7` API calls in the crucible software:
All of the API links can be found under `http://localhost:5000/api/v1` (When running locally)

- `list_running_containers`
- `list_all_containers`
- `get_container` (Gets container telemetary data - not the container itself)
- `run_container`
- `start_container`
- `stop_container`
- `remove_container`

Sending a request to an API:

```python
def test rest_api_get():
     response = requests.get(<rest_api_url>)
     assert response.status_code == 200 ## assert allows us to test if a condition is true or false - in this case we check if the api returns a 200 (success)
```

## Notes on Thunderclient

Reference: https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client

Thunderclient is a VSCode extension that allows for REST API commands to be sent to a website - We can use it to test our api commands.

Our API commands are currently under:

```
http://localhost:5000/api/v1
```

So an example API call for listing all runnning containers would be:

```
http://localhost:5000/api/v1/docker_api/list_running_containers
```

The above api request will return with a 200 response (success) and also a json file listing all the currently running docker containers

## Notes on Pytest

Referance: https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/

We can use dockers API by importing their library

```python
import docker
```

We can start with testing a rest api

```python
def test_rest_api_get():
    # API url
    url = "http://localhost:5000/api/v1/docker_api/list_running_containers"
    response = requests.get(url)
    ## assert allows us to test if a condition is true or false - in this case we check if the api returns a 200 (success)
```

This (Should) just return a 200 in the flask logs:
"GET /api/v1/docker_api/list_running_containers HTTP/1.1" 200 -

Or if run in pytest a green fullstop (in a vscode terminal) like so:

```
ubuntu@DESKTOP-I1LC6AA:~/crucible/api/src$ pytest -k test_rest_api
=======================test session starts ================================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/ubuntu/crucible/api/src
collected 9 items / 8 deselected / 1 selected

test/test__docker_api.py            .              [100%]
=================== 1 passed, 8 deselected in 0.05s =========================
```

We can also print the logs running when using pytest by using `-s`:

```
pytest -k test_list_running -s
```

## Docker API / Docker SDK Python

SDK Referance: https://docker-py.readthedocs.io/en/stable/index.html
API Referance: https://docs.docker.com/engine/api/sdk/examples/

For the test scripts we referance the docker api as `client`

```python
client = docker.from_env()
```

### Running a container

Note that running a container is launching a new container - not starting up an existing one.

```python
client = docker.from_env() # Default docker socket to connect to
print(client.containers.run("alpine", ["echo", "hello", "world"]))
```

### Put it all together

Testing that we can get the metadata for a container

```python
def test_get_container(get_headers):

    # api query parameters
    container_details = {
        "id_name": "crucible_db_1", # name of the container (using db as example container)
    }

    # craft url with container parameters
    response = requests.post(
        URL + "/docker_api/get_container",
        headers=get_headers,
        data=json.dumps(container_details),
    )

    # We now have a url to use: http://localhost:5000/api/v1/docker_api/get_container?id_name=crucible_ab_1

    #Response to above request
    print ("GET_CONTAINER Reponse:")
    print(response.text)

    # Test to mkae sure returned json object matches what we expected
    assert (
        response.json()["message"]["Name"] == "/crucible_db_1"
    )
```

Testing that we can build and run a container

```python
def test_run_container(get_headers):
    container_details = {
        # Suggest changing to a superset container that doesnt exit immediately
        "image": "alpine:latest",
        "command": "sleep 10", # container will otherwise complete its task an exit immedielty
        "name": "docker_api_testing",
    }

    response = requests.post(
        URL + "/docker_api/run_container",
        headers=get_headers,
        # Collects all json object data about the docker containers and returns it as a string
        data=json.dumps(container_details),
    )
    print ("Reponse:")
    print(response.text)

    # Checks if the name of the docker container started up is the same as the one specified in "container details"
    assert (
        response.json()["message"]["Name"] == "/docker_api_testing"
    )

    # Checks if the docker container is running
    test_client = client.containers.get("/docker_api_testing")
    assert test_client.status == "running"

    # Remove docker container called "docker_api_testing"
    test_client.stop() # stops "docker_api_testing"
    test_client.remove() # removes running container
```




