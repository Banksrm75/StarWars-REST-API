"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Characters, Planets, Vehicles, User_Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



                        # GET all CHARACTERS and a specific character
@app.route("/characters", methods=["GET"])
def get_all_characters():

    # Fetch all records from a particular table/model
    all_characters = Characters.query.all()

    # handle case where there are NO entries in the table
        # use a conditional
    if all_characters is None:
        return jsonify("No records found!"), 404
    else:
        all_characters = list(map(lambda x: x.serialize(), all_characters))
        return jsonify(all_characters), 200

@app.route("/characters/<int:character_id>", methods=["GET"])
def get_character(character_id):
    
    # Get single record based on its primary key
    single_character = Characters.query.get(character_id)

    if single_character is None:
        raise APIException(f'Character ID {character_id} is not found!', status_code = 404)
    single_character = single_character.serialize()
    return jsonify(single_character), 200


                        # GET all PLANETS and a specific planet
@app.route("/planets", methods=["GET"])
def get_all_planets():
    all_planets = Planets.query.all()

    if all_planets is None:
        return jsonify("No records found!"), 404
    else:
        all_planets = list(map(lambda x: x.serialize(), all_planets))
        return jsonify(all_planets), 200

@app.route("/planets/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    single_planet = Planets.query.get(planet_id)

    if single_planet is None:
        raise APIException(f'Planet ID {planet_id} is not found!', status_code = 404)
    single_planet = single_planet.serialize()
    return jsonify(single_planet), 200



                        # GET all VEHICLES and a specific vehicle
@app.route("/vehicles", methods=["GET"])
def get_all_vehicles():
    all_vehicles = Vehicles.query.all()

    if all_vehicles is None:
        return jsonify("No records found!"), 404
    else:
        all_vehicles = list(map(lambda x: x.serialize(), all_vehicles))
        return jsonify(all_vehicles), 200


@app.route("/vehicles/<int:vehicle_id>", methods=["GET"])
def get_vehicle(vehicle_id):
    single_vehicle = Vehicles.query.get(vehicle_id)

    if single_vehicle is None:
        raise APIException(f'Vehicle ID {vehicle_id} is not found!', status_code = 404)
    single_vehicle = single_vehicle.serialize()
    return jsonify(single_vehicle), 200


                        # GET ALL users
@app.route("/users", methods=["GET"])
def get_all_users():
    all_users = Users.query.all()

    if all_users is None:
        return jsonify("No records found!"), 404
    else:
        all_users = list(map(lambda x: x.serialize(), all_users))
        return jsonify(all_users), 200


## USER FAVORITES
                        # GET a user's favorites
@app.route("/favorites/<int:user_id>", methods=["GET"])
def get_user_favorites(user_id):
    
    user_favorites = User_Favorites.query.filter_by(user_id = user_id).all()

    if user_favorites is None:
        raise APIException(f'User ID {user_id} has no favorites yet!', status_code = 404)
    else:
        user_favorites = list(map(lambda x: x.serialize(), user_favorites))
        return jsonify(user_favorites), 200

                        # ADD a user's favorite CHARACTER
@app.route("/favorites/character", methods=["POST"])
def add_favorite_character():

    # retrieve the information found in the BODY portion of the client request
    data = request.get_json()
    requested_character = data["character_id"]
    character = Characters.query.get(requested_character)
    already_on_list = User_Favorites.query.filter_by(user_id = data["user_id"], character_id = requested_character).first()
    print(already_on_list)
    print(f"<User_Favorites {character}>")
    
    # User requests an invalid character_id
    if not character:
        raise APIException(f'That character does not exist!', status_code = 404)
    
    # User requests a character_id that's already on their list
    elif already_on_list == (f"<User_Favorites {character}>"):
        raise APIException(f'{requested_character} is already in your list!', status_code = 404)
    
    else:
        new_favorite_character = User_Favorites(user_id = data["user_id"],  character_id = requested_character)
        db.session.add(new_favorite_character)
        db.session.commit()
        print(requested_character)
        return jsonify("Your favorite character was added!"), 200

    



                        # ADD a user's favorite PLANET
@app.route("/favorites/planet", methods=["POST"])
def add_favorite_planet():

    data = request.get_json()

    new_favorite_planet = User_Favorites(user_id = data["user_id"],  planet_id = data["planet_id"])
    db.session.add(new_favorite_planet)
    db.session.commit()

    return jsonify("Your favorite planet was added!"), 200


                        # ADD a user's favorite VEHICLE
@app.route("/favorites/vehicle", methods=["POST"])
def add_favorite_vehicle():
    
    data = request.get_json()

    new_favorite_vehicle = User_Favorites(user_id = data["user_id"],  vehicle_id = data["vehicle_id"])
    db.session.add(new_favorite_vehicle)
    db.session.commit()

    return jsonify("Your favorite vehicle was added!"), 200


                        # DELETE a user's favorite  CHARACTER
            # @app.route("/favorites/character", methods=["DELETE"])
            # def delete_fav_character():
                
            #     data = request.get_json()

            #     fave_to_delete = User_Favorites(user_id = data["user_id"],  vehicle_id = data["vehicle_id"])
            #     db.session.add(new_favorite_vehicle)
            #     db.session.commit()

            #     return jsonify("Your favorite vehicle was added!"), 200


@app.route("/favorites/character/<int:user_id>/<int:character_id>", methods=["DELETE"])
def delete_fav_character(user_id, character_id):
    
    fave_to_delete = User_Favorites.query.filter_by(user_id = user_id, character_id = character_id).first()
    if fave_to_delete is None:
        return jsonify("I'm sorry, I could not find that character among your favorites!"), 404
    else:
        db.session.delete(fave_to_delete)
        db.session.commit()
        return jsonify("Character successfully deleted from your favorites"), 200
    
    

                        # DELETE a user's favorite  PLANET
@app.route("/favorites/planet/<int:user_id>/<int:planet_id>", methods=["DELETE"])
def delete_fav_planet(user_id, planet_id):
    
    fave_to_delete = User_Favorites.query.filter_by(planet_id = planet_id, user_id = user_id).first()
    if fave_to_delete is None:
        return jsonify("I'm sorry, I could not find that planet among your favorites!"), 404
    else:
        db.session.delete(fave_to_delete)
        db.session.commit()
        return jsonify("Planet successfully deleted from your favorites"), 200

                        # DELETE a user's favorite  VEHICLE
@app.route("/favorites/vehicle/<int:user_id>/<int:vehicle_id>", methods=["DELETE"])
def delete_fav_vehicle(user_id, vehicle_id):
    
    fave_to_delete = User_Favorites.query.filter_by(vehicle_id = vehicle_id, user_id = user_id).first()
    if fave_to_delete is None:
        return jsonify("I'm sorry, I could not find that vehicle among your favorites!"), 404
    else:
        db.session.delete(fave_to_delete)
        db.session.commit()
        return jsonify("Vehicle successfully deleted from your favorites"), 200









# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
