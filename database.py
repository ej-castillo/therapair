from flask_sqlalchemy import SQLAlchemy
import therapair

db = therapair.therapistsdb
current_therapist = None

class Therapist(db.model):
    email_and_phone = db.Column(db.String(45), primary_key = True)
    address = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.Boolean)
    bio = db.Column(db.Text)
    qualifications = db.Column(db.PickleType)
    specialties = db.Column(db.PickleType)

    def __repr__(self):
        return self.name + " " + self.email_and_phone
    
def add_therapist(email, phone, address, name, gender, bio, qualifications, specialties):
    therapist = Therapist(email, phone, address, name, gender, bio)
    #TODO: determine how to turn qualifications and specialties into python lists
    db.session.add(therapist)
    db.session.commit()

def query_therapist(address):
    current_therapist = db.
