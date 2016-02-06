from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort
from myapp import app, db
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'A'}
	return render_template('index.html',
		title = 'Home',
		user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for ' + (form.email.data))
		return redirect('/index')
	return render_template('login.html',
		title = 'Sign In',
		form = form)
