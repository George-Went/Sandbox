class Config(object):
    # Configure environment variables
    FLASK_APP = "app.py"
    TESTING = False
    DEBUG = True

    # Database variables
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
