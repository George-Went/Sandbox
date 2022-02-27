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
## An Person can have multiple Items (its a shoppping list database)
class PersonModel(db.model):
    __tablename__ = "owner"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    def __repr__(self):
        return f"Post('{self.id}','{self.name}')"

class ItemModel(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    person_id = db.coloumn(db.Interger, db.Foreign.key('person.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.person_id}')"

## Create the database table from the above model
db.create_all()


@app.route("/", methods=["GET"])
def home():
    return """<h1>Car Database</h1>
<p>A Demo API for getting car details from a database.</p>"""


## ----------------------------------------------------------
## API URLS
## ----------------------------------------------------------

## CREATE PERSON 
@app.route("/create", methods=["POST"])
def post_cars():
    json_data = request.get_json()
    print(json_data)

    new_person = PersonModel(name = json_data["name"])
    db.session.add(new_person)
    db.session.commit()

    response = "new person added" + str(json_data)

    return response

## READ / VIEW PERSON 
@app.route("/person", methods=["GET"])
def get_person():  
    
    cars = db.session.query(PersonModel).all() # Create sqlalchemy query
    
    result = [
        {"id": car.id, "name": car.name, "model":car.model, "doors":car.doors}
        for car in cars
    ]

    # return response code
    return jsonify(result), 200


## UPDATE / EDIT PERSON
@app.route("/edit")
def edit_car():
    json_data = request.get_json()
    print(json_data)

    ## bind the id in the json to a specific tuple (row) in the database with the same id
    car = db.session.query (PersonModel).filter(PersonModel.id == json_data["id"]).first()

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
    car = db.session.query(PersonModel).filter(PersonModel.id == json_data["id"]).first()

    db.session.delete(car)
    db.session.commit()

    response = "car " + str(car.id) + "deleted"
    return response




## Alternative methods ------------------------------------------------------------
## Post all data (alternative version)
@app.route("/car2", methods=["GET"])
def get_cars2():  
    
    cars = db.session.query(PersonModel).all() # Create sqlalchemy query
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
