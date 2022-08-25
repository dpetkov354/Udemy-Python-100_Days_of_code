from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
# @app.route("/random", methods=["GET"])
# def get_random_cafe():
#     pass
## But GET is allowed by default on all routes.
# So this is much simpler:

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={                            # Transform data into JSON data from the DB
        # Omit the id from the response
        # "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,

        # Put some properties in a sub-category
        "amenities": {
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }
    })


@app.route("/all")
def all():         # Creates a JSON visualization of all the cafes
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_dict = {
                     "id": cafe.id,
                     "name": cafe.name,
                     "map_url": cafe.map_url,
                     "img_url": cafe.img_url,
                     "location": cafe.location,
                     "has_sockets": cafe.has_sockets,
                     "has_toilet": cafe.has_toilet,
                     "has_wifi": cafe.has_wifi,
                     "can_take_calls": cafe.can_take_calls,
                     "seats": cafe.seats,
                     "coffee_price": cafe.coffee_price
                     }

        cafe_list.append(cafe_dict)
    all_cafes = {"cafes": cafe_list}
    all_cafes_json = jsonify(cafes=all_cafes["cafes"])
    return all_cafes_json


@app.route("/search")
def search_cafe():    # Search cafes by location
    location = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=location).all()
    if len(cafe) >= 1:
        return jsonify(cafes=[x.to_dict() for x in cafe])
    else:
        return jsonify(error={'Not Found': "Sorry. we don't have a cafe at that location"})


## HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        form_data = request.form.to_dict()

        def add_data(data):
            for key, value in data.items():
                if value.title() == "True":
                    data[key] = True
                elif value.title() == "False":
                    data[key] = False
            return data

        data = add_data(form_data)
        cafe = Cafe(**data)
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
