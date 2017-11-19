from flask import render_template
from flask_login import current_user
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@main.route('/user/<name>')
def user(name):
	return render_template('user.html')

@main.route('/profile')
def profile():
  	pass

@main.route('/setting')
def setting():
	pass



   	  

