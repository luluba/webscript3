import os
from flask import Flask
from app import db
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'mysql://root:password@localhost/shopit'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from datetime import datetime 

db = SQLAlchemy(app)

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


db.create_all()
#db.drop_all()