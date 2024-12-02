from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(250), unique=False, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "username": self.username,
            "password": self.password
        }

class User_Favorites(db.Model):
    __tablename__ = 'user_favorites'
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(Users, foreign_keys=[user_id])

    fave_characters_id = db.Column(db.Integer, db.ForeignKey('favorite_characters.id'))
    fave_planets_id = db.Column(db.Integer, db.ForeignKey('favorite_planets.id'))
    fave_vehicles_id = db.Column(db.Integer, db.ForeignKey('favorite_vehicles.id'))
    
    def serialize(self):
        return {
            "fave_characters_id": self.fave_characters_id,
            "fave_planets_id": self.fave_planets_id,
            "fave_vehicles_id": self.fave_vehicles_id
        }
    

class Favorite_Characters(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)

    fave_name = db.Column(db.String(250), db.ForeignKey('characters.name'))
    fave_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    
    def serialize(self):
        return {
            "fave_name": self.fave_name,
            "fave_id": self.fave_id
        }

class Favorite_Planets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)

    fave_name = db.Column(db.String(250),  db.ForeignKey('planets.name'))
    fave_id = db.Column(db.Integer, db.ForeignKey('planets.planet_id'))
    
    def serialize(self):
        return {
            "fave_name": self.fave_name,
            "fave_id": self.fave_id
        }

class Favorite_Vehicles(db.Model):
    __tablename__ = 'favorite_vehicles'
    id = db.Column(db.Integer, primary_key=True)

    fave_name = db.Column(db.String(250), db.ForeignKey('vehicles.name'))
    fave_id = db.Column(db.Integer, db.ForeignKey('vehicles.vehicle_id'))
    
    def serialize(self):
        return {
            "fave_name": self.fave_name,
            "fave_id": self.fave_id
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    
    character_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    eye_color = db.Column(db.String(250), unique=False, nullable=True)
    films = db.Column(db.String(250), unique=False, nullable=True)
    homeworld = db.Column(db.String(250), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "character_id": self.character_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "films": self.films,
            "homeworld": self.homeworld
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    
    planet_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    residents = db.Column(db.String(250), unique=False, nullable=False)
    terrain = db.Column(db.String(250), unique=False, nullable=False)
    climate = db.Column(db.String(250), unique=False, nullable=False)
    surface_water = db.Column(db.Integer, unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    rotational_period = db.Column(db.Integer, unique=False, nullable=False)
    films = db.Column(db.String(250), unique=False, nullable=True)
    url = db.Column(db.String(250), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "planet_id": self.planet_id,
            "name": self.name,
            "population": self.population,
            "residents": self.residents,
            "terrain": self.terrain,
            "climate": self.climate,
            "surface_water": self.surface_water,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "rotational_period": self.rotational_period,
            "films": self.films,
            "url": self.url
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    
    vehicle_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(250), unique=False, nullable=False)
    manufacturer = db.Column(db.String(250), unique=False, nullable=False)
    model = db.Column(db.String(250), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    crew = db.Column(db.Integer, unique=False, nullable=False)
    pilots = db.Column(db.String(250), unique=False, nullable=False)  # Figure out how to make this an array type...
    passengers = db.Column(db.Integer, unique=False, nullable=False)
    length = db.Column(db.Integer, unique=False, nullable=False)
    cargo_capacity = db.Column(db.Integer, unique=False, nullable=False)
    consumables = db.Column(db.String(250), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, unique=False, nullable=False)
    films = db.Column(db.String(250), unique=False, nullable=True)
    url = db.Column(db.String(250), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "vehicle_id": self.vehicle_id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "pilots": self.pilots,
            "passengers": self.passengers,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "films": self.films,
            "url": self.url
        }