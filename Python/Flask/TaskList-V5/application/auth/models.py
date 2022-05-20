from application.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


#UserMixin Gives us access to 4 methods: 
# is_authenticated: Checks to see if the current user is already authenticated, thus allowing them to bypass login screens.
# is_active: If your app supports disabling or temporarily banning accounts, 
#               we can check if "user.is_active()" to handle a case where their account exists, but has been banned
# is_anonymous: Many apps have a case where user accounts aren't entirely black-and-white, and anonymous 
#               users have access to interact without authenticating (for some reason). 
# get_id: Fetches a unique ID identifying the user.

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, nullable=True)
    last_login = db.Column(db.DateTime, nullable=True) 
    
    def set_password(self, password):
        # Encrypt password with hash
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        # Check encrypted password
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User('{self.id}','{self.name}','{self.email}','{self.password}','{self.created_on}','{self.last_login}')"