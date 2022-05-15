"""Initialize Flask app."""
# Import application creation functions
from application import create_app

if __name__ == "__main__":
    app = create_app()                  ## running the application/__init__.py function
    app.run(host='0.0.0.0', debug=True) ## App can run on local networks