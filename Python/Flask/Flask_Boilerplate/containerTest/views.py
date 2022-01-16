from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db, Container, Group, GroupContainer
from app import app



if __name__ == '__main__':
    app.run(debug=True)