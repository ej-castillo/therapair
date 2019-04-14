from flask_sqlalchemy import SQLAlchemy
import therapair

db = therapair.theradb
current_therapist = None

class Therapist(db.Model):
    email_and_phone = db.Column(db.String(45), primary_key = True)
    address = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.Boolean)
    bio = db.Column(db.Text)
    qualifications = db.Column(db.Text)
    specialties = db.Column(db.String(150))
    profile_picture = db.Column()
    #specialties is a long ass string with plus signs or commas to split by
    # TODO: figure out what the hell a relationship is
    user_reviews = db.relationship('Review', backref = 'therapist', lazy = True)
    

    def __repr__(self):
        return self.name + " " + self.email_and_phone
    

def add_therapist(em, ph, ad, nm, gn, bi, qu, sp):
    therapist = Therapist(email=em, phone=ph, address=ad, name=nm, gender=gn, bio=bi, qualifications=qu, specialties=sp)
    db.session.add(therapist)
    db.session.commit()

def query_therapist(addy):
    current_therapist = db.query.filter_by(address=addy).first()

def get_specialties():
    if current_therapist is not None:
        list_specialties = current_therapist.specialties.split(",")
        for specialty in list_specialties:
            yield specialty

class Review(db.Model):
    user = db.Column(db.String(30), unique = True)
    therapist = db.Column(db.String(25))
    anonymity = db.Column(db.Boolean)
    rating = db.Column(db.Integer, nullable = False)
    description_of_usage = db.Column(db.String(90))
    explanation = db.Column(db.Text)

def add_review(user, anonymity, rating, description_of_usage, explanation):
    review = Review(user, anonymity, rating, description_of_usage, explanation)
    db.session.add(review)
    db.session.commit()