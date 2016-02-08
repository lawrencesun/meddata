from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort
from flask.ext.login import login_user, logout_user, current_user, login_required
from myapp import app, db, lm
from forms import LoginForm, RegistrationForm
from models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
	user = g.user
	return render_template('index.html',
		title = 'Home',
		user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None: 
			login_user(user, form.remember_me.data)
			return redirect(url_for('index'))
		flash('Invalid email address')
	return render_template('login.html',
		title = 'Sign In',
		form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username = form.username.data, 
					email = form.email.data)
		db.session.add(user)
		db.session.commit()
		flash("You can now login.")
		return redirect(url_for('login'))
	return render_template('register.html', 
		form = form)