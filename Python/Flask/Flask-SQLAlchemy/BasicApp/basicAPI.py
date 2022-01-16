from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite3"  ## Fake database
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column("student_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))


def __init__(self, name, city, addr):
    self.name = name
    self.city = city
    self.addr = addr


## Website root shows all students in database
@app.route("/")
def show_all():
    return render_template("show_all.html", students=students.query.all())


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        if (
            not request.form["name"]
            or not request.form["city"]
            or not request.form["addr"]
        ):
            flash("Please enter all the fields", "error")
        else:
            student = students(
                request.form["name"], request.form["city"], request.form["addr"]
            )

            db.session.add(student)
            db.session.commit()
            flash("Record was successfully added")
            return redirect(url_for("show_all"))
    return render_template("new.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


## Add Records
