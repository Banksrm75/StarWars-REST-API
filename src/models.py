from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.email
    
    def serialize(self):
        return {
            "user_id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    eye_color = db.Column(db.String(250), unique=False, nullable=True)
    
    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "character_id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    terrain = db.Column(db.String(250), unique=False, nullable=False)
    climate = db.Column(db.String(250), unique=False, nullable=False)
    surface_water = db.Column(db.Integer, unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    rotational_period = db.Column(db.Integer, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "planet_id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "surface_water": self.surface_water,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "rotational_period": self.rotational_period
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(250), unique=False, nullable=False)
    manufacturer = db.Column(db.String(250), unique=False, nullable=False)
    model = db.Column(db.String(250), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    length = db.Column(db.Float, unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "vehicle_id": self.id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed
        }
    

class User_Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship(Users)

    
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    character = db.relationship(Characters)

    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    planet = db.relationship(Planets)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=True)
    vehicle = db.relationship(Vehicles)

    # def __repr__(self):
    #         return '<User_Favorites %r>' % self.character
        
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
        }
    
