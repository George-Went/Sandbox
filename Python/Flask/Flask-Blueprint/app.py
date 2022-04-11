"""Initialize Flask app."""
from flask import Flask

# Application entry point
from application import create_app

app = create_app() ## running the application/__init__.py function

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)