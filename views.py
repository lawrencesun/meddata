from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort
from myapp import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'A'}
	return render_template("index.html",
		title = 'Home',
		user = user)