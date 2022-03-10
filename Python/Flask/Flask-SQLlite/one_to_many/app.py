from urllib import response
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError, pre_load
## More complex tables can be difficult to manage when tryint to serealize data into a dict / json
## We can use Flask-Marshmellow 

DEBUG = True
app = Flask(__name__)
## generating a "fake" sqlite database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boilerplate.db"

db = SQLAlchemy(app)
ma = Marshmallow(app)


## Set up our models (which are going to be used to create the tables in the database)
## 
class Owner(db.Model):
    __tablename__ = "owner"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    pets = db.relationship('Pet', backref='owner', lazy=True) 
    # This essentially declares a new property on the item model
    
    def __repr__(self):
        return f"Post('{self.id}','{self.name},'{self.address}','{self.pets}')"

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.owner_id}')"

# Marshmallow schemas / serealisers
class OwnerSchema(ma.Schema): 
    id = fields.Int()
    name = fields.Str()
    address = fields.Str()      

class PetSchema(ma.Schema): 
    id = fields.Int()
    name = fields.Str()
    age = fields.Int()
    


## Create the database table from the above models
db.create_all()



## ----------------------------------------------------------
## API URLS
## ----------------------------------------------------------


@app.route("/", methods=["GET"])
def home():
    return """<h1>People(Persons)/Items Database</h1>
<p>A Demo API for getting car details from a database.</p>"""

## READ / VIEW PERSON 
@app.route("/read", methods=["GET"])
def get_owner():  

    db_query = Owner.query.all()
    # print(db_query)
    
    schema = OwnerSchema(many=True)
    result = schema.dump(db_query) # turn db query into json
    
    # return response code
    # print(result)

    return jsonify(result), 200
    # return jsonify({'in': 'progress'}), 200

@app.route("/read2", methods=["GET"])
def get_owner2():  
    
    owners = db.session.query(Pet).all() # Create sqlalchemy query
    print("print each arrray as an object and add it to a big array ")

    
    
    # return response code
    return jsonify(owners), 200

## CREATE PERSON 
@app.route("/createOwner", methods=["POST"])
def create_owner():
    json_data = request.get_json()
    print(json_data)

    new_owner = Owner(name = json_data["name"], address = json_data["address"])
    db.session.add(new_owner)
    db.session.commit()

    response = "new owner added" + str(json_data)

    return response

## CREATE PET 
@app.route("/createPet", methods=["POST"])
def create_pet():
    json_data = request.get_json()
    print(json_data)

    new_pet = Pet(name = json_data["name"], age = json_data["age"], owner_id = json_data["owner_id"])
    db.session.add(new_pet)
    db.session.commit()

    response = "new pet added" + str(json_data)

    return response

## UPDATE / EDIT PERSON
@app.route("/edit")
def edit_car():
    json_data = request.get_json()
    print(json_data)

    ## bind the id in the json to a specific tuple (row) in the database with the same id
    car = db.session.query (Owner).filter(Owner.id == json_data["id"]).first()

    ## Update the row values
    car.name = json_data["name"]
    car.model = json_data["model"]
    car.doors = json_data["doors"]

    ## add the new vaues and commit them to the database 
    db.session.add(car)
    db.session.commit()

    ## send back a response to the use saying that the task completed successfully 
    response = "car " + str(car.id) + " edited" + str(json_data)
    return response

## DELETE CAR
def delete_car():
    json_data = request.get_json()
    print(json_data)

    ## bind the id in the json to a specific tuple (row) in the database with the same id
    car = db.session.query(Owner).filter(Owner.id == json_data["id"]).first()

    db.session.delete(car)
    db.session.commit()

    response = "car " + str(car.id) + "deleted"
    return response




## Alternative methods ------------------------------------------------------------
## Post all data (alternative version)
@app.route("/car2", methods=["GET"])
def get_cars2():  
    
    cars = db.session.query(Owner).all() # Create sqlalchemy query
    print(cars)

    array = [] ## instansiate empty array 
    for car in cars:
        array.append(
            {"id": car.id, 
            "name": car.name,
            "model":car.model, 
            "doors":car.doors
            }
        )
        
    # return response code
    return jsonify(array), 200







## NOTES ON MYSQL Queries 
@app.route("/read2", methods=["GET"])
def extra_queries():  
    
    result = ["done"]

    owners = db.session.query(Owner).all() # Create sqlalchemy query

    ## print entire mysql response - response is 
    print(owners)

    # print each array 
    for x in owners:
        print(x)


    # print each array as an object - still has the nested arrays though 
    print("print each array as an object")
    for a in owners:
        owner_object = {"id": a.id, "name":a.name, "address":a.address, "pets":a.pets}
        print(owner_object)

    # print each arrray as an object and add it to a big array 
    print("print each arrray as an object and add it to a big array ")
    for a in owners:
        owner_object = {"id": a.id, "name":a.name, "address":a.address} ## put the non-array elements into a object
        pets = a.pets # put the array elements into a new varaible 
        print(owner_object)

        # Loop through the new array to get the [backref / relationship] objects in the other table  
        for b in pets:
            pet_object = {"id": b.id, "name":b.name, "age": b.age}
            print(pet_object)

    ## convert query results into a dict 
    print("query results as dict")
    


    # return response code
    return jsonify(result), 200