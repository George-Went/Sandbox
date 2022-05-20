from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# This is a file we can import into blueprint models to allop access to SQLAlchemy functions
db = SQLAlchemy()
login_manager = LoginManager()