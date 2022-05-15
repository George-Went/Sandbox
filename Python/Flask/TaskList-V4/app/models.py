from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.id}','{self.content}','{self.date_created}')"

## From example code https://python-adv-web-apps.readthedocs.io/en/latest/flask_db3.html#
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

    def __init__(self, name, style, color, quantity, price, updated):
        self.name = name
        self.style = style
        self.color = color
        self.quantity = quantity
        self.price = price
        self.updated = updated


# Containers Model 
class Container(db.Model):
    __tablename__ = 'containers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    command = db.Column(db.String)
    entrypoint = db.Column(db.String)
    environment = db.Column(db.String)
    network = db.Column(db.String)
    network_mode = db.Column(db.String)
    ports = db.Column(db.String)
    restart_policy = db.Column(db.String)
    volumes = db.Column(db.String)

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.image}','{self.command}','{self.entrypoint}','{self.environment}','{self.network}','{self.network_mode}','{self.ports}','{self.restart_policy}','{self.volumes}')"

# Login 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.password}')"



db.create_all() # Create all tables at runtime (if they dont already exist)
