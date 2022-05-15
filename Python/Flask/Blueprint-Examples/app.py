"""Initialize Flask app."""
# Import application creation functions
from application import db, create_app, models 

if __name__ == "__main__":
    app = create_app()                  ## running the application/__init__.py function
    db.create_all(app=create_app())
    app.run(host='0.0.0.0', debug=True) ## App can run on local networks