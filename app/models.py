from datetime import datetime 

from . import db

class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.String(255), primary_key=True, nullable=False)
	username = db.Column(db.String(20), nullable=False)
	ip = db.Column(db.String(20), nullable=False)
	device = db.Column(db.String(20), nullable=False)



class Auth(db.Model):
	__tablename__ = "auth"
	id = db.Column(db.String(255), db.ForeignKey('user.id'), primary_key=True, nullable=False )
	email = db.Column(db.String(20), primary_key=True, nullable=False)
	credentials = db.Column(db.String(1000), nullable=True)

class order(db.Model):
	__tablename__ = "order"
	id = db.Column(db.String(255), db.ForeignKey('user.id'), primary_key=True, nullable=False)
	email = db.Column(db.String(20), primary_key=True, nullable=False)
	last_order = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
