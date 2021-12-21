from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:password@localhost:5432/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

## ----------------------------------------------------------
## DATABASE MODELS
## ----------------------------------------------------------

## This is a Object Relation model - the mold for incoming json data to `fit into` before being passed on to the database
## Flask_Migrate can take this model and convert it into a database table for us
## Run:
## flask db init - initlises a new table
## flask db migrate - enables migrations from our class "CarsModel"
## flask db upgrade - migrates the models
class CarsModel(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


## ----------------------------------------------------------
## API URLS
## ----------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return """<h1>Car Database</h1>
<p>A Demo API for getting car details from a database.</p>"""


## ------------------------------------------------------------
## Getting all entities in the database, or adding new ones
## ------------------------------------------------------------
@app.route("/cars", methods=["POST", "GET"])
def handle_cars():
    ## if the incoming request is POST
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()  # Data needs to be a json
            new_car = CarsModel(  # json data is converted into database data using the CarsModel model
                name=data["name"], model=data["model"], doors=data["doors"]
            )
            db.session.add(new_car)  # Sets up the sql function
            db.session.commit()  # sends the sql function to the database

            return {"message: " + {new_car.name} + "has been created successfully."}
            # return {"message": f"car {new_car.name} has been created successfully."}
            # Returns a JSON string that uses a f string function - the string is calculated at run time

        else:
            return {"error": "The request payload is not in JSON format"}

    ## If the incoming request is a GET --------------------------------------------------------
    elif request.method == "GET":
        cars = (
            CarsModel.query.all()  # query all the cars in the database using the flask-sqlalchemy function
        )
        results = [
            {"id": car.id, "name": car.name, "model": car.model, "doors": car.doors}
            for car in cars  ## puts the query results into an array
        ]
        return {
            "count": len(results),
            "cars": results,
        }  ## returns text with the assosiated array


## ------------------------------------------------------------
## Getting a specific entity, updating an existing entity or deleting an existing entity
## ------------------------------------------------------------
@app.route("/cars/<car_id>", methods=["GET", "PUT", "DELETE"])
def handle_car(car_id):
    car = CarsModel.query.get_or_404(car_id)
    ## Each of the below functions are based on whether the server recives a GET,PUT or DELETE function
    if request.method == "GET":
        response = {"name": car.name, "model": car.model, "doors": car.doors}
        return {"message": "success", "car": response}

    elif request.method == "PUT":
        data = request.get_json()
        car.name = data["name"]
        car.model = data["model"]
        car.doors = data["doors"]
        db.session.add(car)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}

    elif request.method == "DELETE":
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car {car.name} successfully deleted."}


