from flask import Flask

## Run using `python3 app.py`
## or 
## export FLASK_APP=app
## flask run
DEBUG = True
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
