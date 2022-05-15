from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db


DEBUG = True
app = Flask(__name__)

## generating a "fake" database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boilerplate.db"
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)

#Generating Models 
class Groups(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')),
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))


@app.route("/", methods=["GET"])
#@protect()
def get_groups(self):  

    

    groups = db.session.query(Groups).all() 

    return self.response(200, result=groups)


# Add a new group
@app.route("/add", methods=["POST"])
# @protect()   
def addGroup(self):
    
    

    data = request.get_json()
    
    new_group = Groups(name = data["name"])
    db.session.add(new_group)
    db.session.commit()

    return self.response(200)

# Remove and existing group
@app.route("/delete", methods=["POST"])
# @protect()   
def addGroup(self):
    
    data = request.get_json()
    
    new_group = Groups(name = data["name"])
    db.session.delete(new_group)
    db.session.commit()

    return self.response(200)  

# Edit an new group
@app.route("/edit/<int:group_id>", methods=["POST"])
# @protect()   
def addGroup(self,group_id):
    
  

    ## bind variables to json values 
    data = request.get_json()

    # Find group
    group = db.session.query(Group).filter(Group.id == group_id).first()
    
    print(group.id)
    print(group.name)
    print(request.get_json(["name"]))
    print(data["name"])

    group.name = data["name"]

    print(group.name)
    
    db.session.commit()

    result = ("ok : " + group.name)
    return self.response(200, result=result)


@app.route("/alternate1", methods=["GET"])
#@protect()
def get_groups(self):  

    from app import db
    
    result = []

    # Create sqlalchemy query
    groups = db.session.query(Group).all() 

    for group in groups:
        result.append(group.name)
    

    # return response code
    return self.response(200, result=result)


@app.route("/alternate2", methods=["GET"])
#@protect()
def get_groups(self):  

    from app import db
    
    # Create sqlalchemy query
    groups = db.session.query(Group).all() 

    # for group in groups:
    #     print(group.id)
    #     print(group.name)
    result = [
        {"id": group.id, "name": group.name}
        for group in groups
    ]

    # return response code
    return self.response(200, result=result)
