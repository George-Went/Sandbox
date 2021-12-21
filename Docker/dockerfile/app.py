from flask import Flask

## Run using `python3 app.py`
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World! This is running in a docker container"


if __name__ == "__main__":
    app.run()
