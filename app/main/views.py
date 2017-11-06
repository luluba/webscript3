from flask import render_template
from . import main

@main.route('/home')
def home():
	return render_template('home.html')

@main.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)
