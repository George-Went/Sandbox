from urllib import response
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

DEBUG = True
app = Flask(__name__)
## generating a "fake" sqlite database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boilerplate.db"
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)

## Set up our models (which are going to be used to create the tables in the database)
class Person(db.model):
    __tablename__ = "owner"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.address}')"

class item(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Interger())
    

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.price}')"

class PersonItem(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id", primary_key=True))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), primary_key=True)

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.model}','{self.doors}')"



## Create the database table from the above model
db.create_all()


@app.route("/", methods=["GET"])
def home():
    return """<h1>person Database</h1>
<p>A Demo API for getting person details from a database.</p>"""


## ----------------------------------------------------------
## API URLS
## ----------------------------------------------------------


## PERSON ----------------------------------------------------
## CREATE person 
@app.route("/create", methods=["POST"])
def post_persons():
    json_data = request.get_json()
    print(json_data)

    new_person = personsModel(name = json_data["name"], model = json_data["model"], doors = json_data["doors"])
    db.session.add(new_person)
    db.session.commit()

    response = "new person added" + str(json_data)

    return response

## READ / VIEW person 
@app.route("/person", methods=["GET"])
def get_persons():  
    
    persons = db.session.query(personsModel).all() # Create sqlalchemy query
    
    result = [
        {"id": person.id, "name": person.name, "model":person.model, "doors":person.doors}
        for person in persons
    ]

    # return response code
    return jsonify(result), 200


## UPDATE / EDIT person
@app.route("/edit")
def edit_person():
    json_data = request.get_json()
    print(json_data)

    ## bind the id in the json to a specific tuple (row) in the database with the same id
    person = db.session.query(personsModel).filter(personsModel.id == json_data["id"]).first()

    ## Update the row values
    person.name = json_data["name"]
    person.model = json_data["model"]
    person.doors = json_data["doors"]

    ## add the new vaues and commit them to the database 
    db.session.add(person)
    db.session.commit()

    ## send back a response to the use saying that the task completed successfully 
    response = "person " + str(person.id) + " edited" + str(json_data)
    return response

## DELETE person
def delete_person():
    json_data = request.get_json()
    print(json_data)

    ## bind the id in the json to a specific tuple (row) in the database with the same id
    person = db.session.query(personsModel).filter(personsModel.id == json_data["id"]).first()

    db.session.delete(person)
    db.session.commit()

    response = "person " + str(person.id) + "deleted"
    return response




## Alternative methods ------------------------------------------------------------
## Post all data (alternative version)
@app.route("/person2", methods=["GET"])
def get_persons2():  
    
    persons = db.session.query(personsModel).all() # Create sqlalchemy query
    print(persons)

    array = [] ## instansiate empty array 
    for person in persons:
        array.append(
            {"id": person.id, 
            "name": person.name,
            "model":person.model, 
            "doors":person.doors
            }
        )
        
    # return response code
    return jsonify(array), 200
