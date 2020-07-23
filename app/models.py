from app import db


class User(db.Model):
	id    = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True)
	trips = db.relationship('Trip', backref='user', lazy='dynamic')


class Trip(db.Model):
	id  = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	description = db.Column(db.Text)
	user_id = db.Column(db.Integer,   db.ForeignKey('user.id'))


class Orginizer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True)


class Partner(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True)
	rate = db.Column(db.Integer) 
